import threading
import asyncio
import queue
import time
import mitmproxy.http
import mitmproxy.log
import mitmproxy.tcp
import mitmproxy.websocket
from mitmproxy import proxy, options, ctx
from mitmproxy.tools.dump import DumpMaster
from .bridge import AmatsukiBridge
from .mitm_abc import ClientWebSocketABC
from .logger import logger

activated_flows: list[str] = [] # store all flow.id ([-1] is the recently opened)
mjai_messages: queue.Queue[dict] = queue.Queue() # store all messages
amaruki_bridges: dict[str, AmatsukiBridge] = dict() # flow.id -> AmatsukiBridge


class ClientWebSocket(ClientWebSocketABC):
    def __init__(self):
        pass

    def websocket_start(self, flow: mitmproxy.http.HTTPFlow):
        assert isinstance(flow.websocket, mitmproxy.websocket.WebSocketData)
        global activated_flows, mjai_messages, amaruki_bridges
        logger.info(f"WebSocket connection opened: {flow.id}")
        
        activated_flows.append(flow.id)
        amaruki_bridges[flow.id] = AmatsukiBridge()

    def websocket_message(self, flow: mitmproxy.http.HTTPFlow):
        assert isinstance(flow.websocket, mitmproxy.websocket.WebSocketData)
        global activated_flows,mjai_messages, amaruki_bridges
        if flow.id in activated_flows:
            msg = flow.websocket.messages[-1]
            if msg.from_client:
                logger.debug(f"<- Message: {msg.content}")
            else: # from server
                logger.debug(f"-> Message: {msg.content}")
            mjai_msg = amaruki_bridges[flow.id].parse(msg.content)
            if mjai_msg:
                for msg in mjai_msg:
                    logger.info(f"<- MJAI Message: {msg}")
                    mjai_messages.put(msg)
        else:
            logger.error(f"WebSocket message received from unactivated flow: {flow.id}")

    def websocket_end(self, flow: mitmproxy.http.HTTPFlow):
        global activated_flows, mjai_messages, amaruki_bridges
        if flow.id in activated_flows:
            logger.info(f"WebSocket connection closed: {flow.id}")
            activated_flows.remove(flow.id)
            amaruki_bridges.pop(flow.id)
        else:
            logger.error(f"WebSocket connection closed from unactivated flow: {flow.id}")

    def request(self, flow: mitmproxy.http.HTTPFlow):
        logger.debug(f"Request: {flow.request.pretty_url}")
        logger.debug(f"Request Method: {flow.request.method}")
        logger.debug(f"Request Headers: {flow.request.headers}")
        logger.debug(f"Request Content: {flow.request.content}")
        if flow.request.pretty_url == "https://lobby.amatsukimahjong.com/game/game_heart":
            # Send a reply from the proxy without sending the request to the remote server.        
            # This prevents the client from disconnecting due to server error
            logger.info("Heartbeat request intercepted")
            flow.response = mitmproxy.http.Response.make(
                200,  # (200 OK)
                b'{"status":0,"errorCode":0}',  # (response body)
                {"Content-Type": "application/json"}  # (headers)
            )

    def response(self, flow: mitmproxy.http.HTTPFlow):
        # Patch the heartbeat response
        # This prevents the client from disconnecting due to server error
        logger.debug(f"Response: {flow.request.pretty_url}")
        logger.debug(f"Response Code: {flow.response.status_code}")
        if flow.request.pretty_url == "https://lobby.amatsukimahjong.com/game/game_heart":
            if flow.response.status_code != 200:
                flow.response.status_code = 200
                flow.response.content = b'{"status":0,"errorCode":0}'
                logger.info("Heartbeat response intercepted")
            try:
                res_json: dict = flow.response.json()
                if res_json.get("status") != 0 or res_json.get("errorCode") != 0:
                    flow.response.status_code = 200
                    flow.response.content = b'{"status":0,"errorCode":0}'
                    logger.info("Heartbeat response intercepted")
            except Exception as e:
                logger.error(f"Failed to parse heartbeat response: {e}")
                flow.response.status_code = 200
                flow.response.content = b'{"status":0,"errorCode":0}'
                logger.info("Heartbeat response intercepted")


async def start_proxy(host, port):
    opts = options.Options(listen_host=host, listen_port=port)
    master = DumpMaster(
        opts,
        with_termlog=False,
        with_dumper=False,
    )
    master.addons.add(ClientWebSocket())
    logger.info(f"Starting MITM proxy server at {host}:{port}")
    await master.run()
    logger.info("MITM proxy server stopped")
    return master

def stop_proxy():
    ctx.master.shutdown()

addons = [
    ClientWebSocket()
]
