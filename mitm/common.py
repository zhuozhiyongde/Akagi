import mitmproxy.addonmanager
import mitmproxy.http
import mitmproxy.log
import mitmproxy.tcp
import mitmproxy.websocket
from .logger import logger

activated_flows: list[str] = [] # store all flow.id ([-1] is the recently opened)
messages_dict: dict[str, bytes] = dict() # flow.id -> Queue[flow_msg]

class ClientWebSocket:
    def __init__(self):
        pass

    def websocket_start(self, flow: mitmproxy.http.HTTPFlow):
        assert isinstance(flow.websocket, mitmproxy.websocket.WebSocketData)
        global activated_flows,messages_dict
        logger.info(f"WebSocket connection opened: {flow.id}")
        
        activated_flows.append(flow.id)
        messages_dict[flow.id]=[]

    def websocket_message(self, flow: mitmproxy.http.HTTPFlow):
        assert isinstance(flow.websocket, mitmproxy.websocket.WebSocketData)
        global activated_flows,messages_dict
        if flow.id in activated_flows:
            msg = flow.websocket.messages[-1]
            if msg.from_client:
                logger.debug(f"<- Message: {msg.content}")
            else: # from server
                logger.debug(f"-> Message: {msg.content}")
            messages_dict[flow.id].append(msg.content)
        else:
            logger.error(f"WebSocket message received from unactivated flow: {flow.id}")

    def websocket_end(self, flow: mitmproxy.http.HTTPFlow):
        global activated_flows,messages_dict
        if flow.id in activated_flows:
            logger.info(f"WebSocket connection closed: {flow.id}")
            activated_flows.remove(flow.id)
            messages_dict.pop(flow.id)
        else:
            logger.error(f"WebSocket connection closed from unactivated flow: {flow.id}")
