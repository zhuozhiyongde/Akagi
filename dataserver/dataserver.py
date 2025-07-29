import asyncio
import json
from threading import Thread
from aiohttp import web, WSMsgType
from .logger import logger

class DataServer(Thread):
    def __init__(self, external_port=8765):
        super().__init__()
        self.daemon = True
        self.external_port = external_port
        self.clients: dict[str, dict] = {} # {clientId: {"ws": ws, "missed_pongs": 0}}
        self.latest_data = None
        self.loop = None
        self.runner = None
        self.running = False
        self.keep_alive_task = None

    async def keep_alive(self):
        while True:
            await asyncio.sleep(10)
            if not self.clients:
                continue

            logger.debug(f"Running keep-alive for {len(self.clients)} clients")
            zombie_client_ids = []
            for client_id, client_data in self.clients.items():
                ws = client_data['ws']
                if ws.closed:
                    zombie_client_ids.append(client_id)
                    continue
                
                if client_data['missed_pongs'] >= 2:
                    logger.warning(f"Client {client_id} missed 3 pongs, closing connection.")
                    await ws.close(code=1000, message='Pong timeout')
                    zombie_client_ids.append(client_id)
                    continue
                
                try:
                    await ws.ping()
                    client_data['missed_pongs'] += 1
                except ConnectionResetError:
                    logger.warning(f"Connection reset for {client_id}, marking as zombie.")
                    zombie_client_ids.append(client_id)

            for client_id in zombie_client_ids:
                if client_id in self.clients:
                    del self.clients[client_id]
            
            logger.debug(f"Keep-alive check finished. {len(zombie_client_ids)} zombie clients removed.")

    def run(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        
        try:
            app = web.Application()
            app.router.add_get('/', self.websocket_handler)
            
            self.runner = web.AppRunner(app)
            self.loop.run_until_complete(self.runner.setup())
            
            site = web.TCPSite(self.runner, '0.0.0.0', self.external_port)
            self.loop.run_until_complete(site.start())
            
            logger.info(f"DataServer WebSocket listening on 0.0.0.0:{self.external_port}")
            self.running = True
            self.keep_alive_task = self.loop.create_task(self.keep_alive())
            self.loop.run_forever()
        finally:
            if self.keep_alive_task:
                self.keep_alive_task.cancel()
            if self.runner:
                self.loop.run_until_complete(self.runner.cleanup())
            logger.info("DataServer event loop stopped.")

    def stop(self):
        if self.running and self.loop and self.loop.is_running():
            logger.info("Stopping DataServer...")
            self.loop.call_soon_threadsafe(self.loop.stop)
            logger.info("DataServer stop signal sent.")
        self.running = False

    async def _update_data_async(self, data):
        self.latest_data = data
        if self.clients:
            message = json.dumps(data)
            logger.debug(f"Broadcasting to {len(self.clients)} clients: {message}")
            coros = [client['ws'].send_str(message) for client in self.clients.values()]
            await asyncio.gather(*coros, return_exceptions=True)

    def update_data(self, data):
        if self.loop and self.running:
            asyncio.run_coroutine_threadsafe(self._update_data_async(data), self.loop)

    async def websocket_handler(self, request):
        client_id = request.query.get('clientId')
        if not client_id:
            logger.warning("Client connected without clientId, rejecting.")
            return web.HTTPBadRequest(text="clientId is required")

        ws = web.WebSocketResponse()
        await ws.prepare(request)

        if client_id in self.clients:
            logger.warning(f"Client {client_id} already connected. Closing old connection.")
            old_ws = self.clients[client_id]['ws']
            await old_ws.close(code=1001, message='Going Away. New connection established.')
        
        self.clients[client_id] = {'ws': ws, 'missed_pongs': 0}
        logger.info(f"WebSocket client {client_id} connected from {request.remote}")

        if self.latest_data:
            await ws.send_str(json.dumps(self.latest_data))

        client_id_for_closure = client_id # Capture for finally block
        try:
            async for msg in ws:
                if msg.type == WSMsgType.PONG:
                    logger.debug(f"Received pong from {client_id_for_closure}")
                    if client_id_for_closure in self.clients:
                        self.clients[client_id_for_closure]['missed_pongs'] = 0
                elif msg.type == WSMsgType.ERROR:
                    logger.error(f"WebSocket connection for {client_id_for_closure} closed with exception {ws.exception()}")
        finally:
            # Only remove the client if the connection being closed is the current one
            if client_id_for_closure in self.clients and self.clients[client_id_for_closure]['ws'] is ws:
                del self.clients[client_id_for_closure]
                logger.info(f"WebSocket client {client_id_for_closure} disconnected from {request.remote}")
            else:
                logger.info(f"Old WebSocket connection for {client_id_for_closure} already replaced, no action needed.")

        return ws