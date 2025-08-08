import queue
import mitmproxy.http
import mitmproxy.websocket
from mitmproxy import proxy, options, ctx
from mitmproxy.tools.dump import DumpMaster
from .bridge import UnifiedBridge
from .mitm_abc import ClientWebSocketABC
from .logger import logger

activated_flows: list[str] = [] # store all flow.id ([-1] is the recently opened)
mjai_messages: queue.Queue[dict] = queue.Queue() # store all messages
unified_bridges: dict[str, UnifiedBridge] = dict() # flow.id -> UnifiedBridge


class ClientWebSocket(ClientWebSocketABC):
    def __init__(self):
        pass

    def websocket_start(self, flow: mitmproxy.http.HTTPFlow):
        assert isinstance(flow.websocket, mitmproxy.websocket.WebSocketData)
        global activated_flows, mjai_messages, unified_bridges
        logger.info(f"WebSocket connection opened: {flow.id}")
        
        activated_flows.append(flow.id)
        unified_bridges[flow.id] = UnifiedBridge()

    def websocket_message(self, flow: mitmproxy.http.HTTPFlow):
        assert isinstance(flow.websocket, mitmproxy.websocket.WebSocketData)
        global activated_flows,mjai_messages, unified_bridges
        if flow.id in activated_flows:
            msg = flow.websocket.messages[-1]
            if msg.from_client:
                logger.debug(f"<- Message: {msg.content}")
            else: # from server
                logger.debug(f"-> Message: {msg.content}")
            mjai_msg = unified_bridges[flow.id].parse(msg.content, msg.from_client) # We need from_client here because tenhou's bridge needs it.
            if mjai_msg:
                for msg in mjai_msg:
                    logger.info(f"<- MJAI Message: {msg}")
                    mjai_messages.put(msg)
        else:
            logger.error(f"WebSocket message received from unactivated flow: {flow.id}")

    def websocket_end(self, flow: mitmproxy.http.HTTPFlow):
        global activated_flows, mjai_messages, unified_bridges
        if flow.id in activated_flows:
            logger.info(f"WebSocket connection closed: {flow.id}")
            activated_flows.remove(flow.id)
            unified_bridges.pop(flow.id)
        else:
            logger.error(f"WebSocket connection closed from unactivated flow: {flow.id}")


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
