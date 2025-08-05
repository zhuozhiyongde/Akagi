import re
import json
from enum import Enum
from typing import Self
from ..bridge_base import BridgeBase
from ..logger import logger

from ..amatsuki import AmatsukiBridge
from ..majsoul import MajsoulBridge
from ..riichi_city import RiichiCityBridge
from ..tenhou import TenhouBridge


class GameType(Enum):
    AMATSUKI = "amatsuki"
    MAJSOUL = "majsoul"
    RIICHI_CITY = "riichi_city"
    TENHOU = "tenhou"
    UNKNOWN = "unknown"


class UnifiedBridge(BridgeBase):
    def __init__(self):
        super().__init__()
        self.game_type: GameType = GameType.UNKNOWN
        self.bridge = None

    def parse(self, content: bytes) -> None | list[dict]:
        logger.debug(f"<- {content}")
        if self.game_type == GameType.UNKNOWN:
            if self.is_amatsuki(content):
                self.game_type = GameType.AMATSUKI
                self.bridge = AmatsukiBridge()
            elif self.is_majsoul(content):
                self.game_type = GameType.MAJSOUL
                self.bridge = MajsoulBridge()
            elif self.is_riichi_city(content):
                self.game_type = GameType.RIICHI_CITY
                self.bridge = RiichiCityBridge()
            elif self.is_tenhou(content):
                self.game_type = GameType.TENHOU
                self.bridge = TenhouBridge()
            else:
                logger.error("Unknown game type")
                return None
        if self.bridge is None:
            logger.error("Bridge is not initialized")
            return None
        try:
            parsed_content = self.bridge.parse(content)
            if parsed_content is not None:
                logger.debug(f"-> {parsed_content}")
            return parsed_content
        except Exception as e:
            logger.error(f"Error in parse: {e}")
            return None
    
    def build(self, command: dict) -> None | bytes:
        pass

    def find_type(self, content: bytes) -> str:
        try:
            pass
        except Exception as e:
            logger.error(f"Error in find_type: {e}")
            return "unknown"
        
    def is_amatsuki(self, content: bytes) -> bool:
        # If content starts with (CONNECT|CONNECTED|SEND|SUBSCRIBE|UNSUBSCRIBE|MESSAGE)\n then it is Amatsuki
        return re.match(rb"^(CONNECT|CONNECTED|SEND|SUBSCRIBE|UNSUBSCRIBE|MESSAGE)\n", content) is not None
    
    def is_majsoul(self, content: bytes) -> bool:
        # If content starts with \x01|\x02|\x03 then it is Majsoul
        return re.match(rb"^\x01|\x02|\x03", content) is not None
    
    def is_riichi_city(self, content: bytes) -> bool:
        # If content[4:8] == b"\x00\x0f\x00\x01" then it is Riichi City
        msg_len = int.from_bytes(content[:4], byteorder='big')
        return content[4:8] == b"\x00\x0f\x00\x01" and len(content) == msg_len
    
    def is_tenhou(self, content: bytes) -> bool:
        # If content starts with b"<" or b"{"tag":" then it is Tenhou
        return content.startswith(b"<") or content.startswith(b'{"tag":"') 
