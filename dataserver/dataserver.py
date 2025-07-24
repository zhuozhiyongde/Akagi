import asyncio
import json
from threading import Thread
from aiohttp import web, WSMsgType
from .logger import logger

class DataServer(Thread):
    def __init__(self, external_port=8765):
        super().__init__()
        self.external_port = external_port
        self.websockets = set()
        self.latest_data = None
        self.loop = None
        self.runner = None
        self.running = False

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
            self.loop.run_forever()
        finally:
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
        if self.websockets:
            message = json.dumps(data)
            logger.debug(f"Broadcasting to {len(self.websockets)} clients: {message}")
            coros = [ws.send_str(message) for ws in self.websockets]
            await asyncio.gather(*coros, return_exceptions=True)

    def update_data(self, data):
        if self.loop and self.running:
            asyncio.run_coroutine_threadsafe(self._update_data_async(data), self.loop)

    async def websocket_handler(self, request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        self.websockets.add(ws)
        logger.info(f"WebSocket client connected from {request.remote}")

        if self.latest_data:
            await ws.send_str(json.dumps(self.latest_data))

        try:
            async for msg in ws:
                if msg.type == WSMsgType.ERROR:
                    logger.error(f"WebSocket connection closed with exception {ws.exception()}")
        finally:
            self.websockets.remove(ws)
            logger.info(f"WebSocket client disconnected from {request.remote}")

        return ws