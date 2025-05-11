import json
from typing import Self
from enum import Enum
from ..bridge_base import BridgeBase
from ..logger import logger
        

class RCMessage:
    def __init__(self, msg_id, msg_type, msg_data):
        self.msg_id: int = msg_id
        self.msg_type: int = msg_type
        self.msg_data: dict = msg_data

    def __str__(self):
        return f"Message: {self.msg_id} {self.msg_type} {self.msg_data}"

class RiichiCityBridge(BridgeBase):
    def __init__(self):
        super().__init__()

    def preprocess(self, content: bytes) -> RCMessage | None:
        """Preprocess the content and returns RCMessage.
        
        Args:
            content (bytes): Content to be preprocessed.

        Returns:
            RCMessage: RCMessage object.
        """
        # Convert first 4 byte to int
        msg_len = int.from_bytes(content[:4], byteorder='big')
        # Check if the message is complete
        if len(content) != msg_len:
            logger.warning(f"Message is not complete, expected {msg_len} bytes, got {len(content)} bytes")
            logger.warning(f"Message: {content.hex(' ')}")
            return
        # Check next 4 byte is 00 0f 00 01
        # Still don't know what this means.
        if content[4:8] != b'\x00\x0f\x00\x01':
            logger.warning("Message is unknown format, expected 00 0f 00 01")
            logger.warning(f"Message: {content.hex(' ')}")
            return
        # Convert next 4 byte to int
        msg_id = int.from_bytes(content[8:12], byteorder='big')
        # Convert next 2 byte to int
        msg_type = int.from_bytes(content[12:14], byteorder='big')
        # Check next 1 byte is 01
        # Still don't know what this means.
        if content[14] != 1:
            logger.warning("Message is unknown format, expected 01")
            logger.warning(f"Message: {content.hex(' ')}")
            return
        # Load json data from the rest of the message
        # if there are no data, it will be empty
        if len(content) == 15:
            msg_data = {}
        else:
            msg_data = json.loads(content[15:].decode('utf-8'))
        logger.debug({
            "msg_id": msg_id,
            "msg_type": msg_type,
            "msg_data": msg_data
        })

        return RCMessage(msg_id, msg_type, msg_data)

    def parse(self, content: bytes) -> None | list[dict]:
        """Parses the content and returns MJAI command.

        Args:
            content (bytes): Content to be parsed.

        Returns:
            None | list[dict]: MJAI command.
        """
        rc_msg = self.preprocess(content)
        if rc_msg is None:
            return None
        return None

    def build(self, command: dict) -> None | bytes:
        pass


