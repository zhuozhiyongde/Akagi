from __future__ import annotations

import loguru
from loguru import logger as main_logger
from datetime import datetime
from pathlib import Path

# Log to: "./Logs/rpc_client_<timestamp>.log"
log_path = Path().cwd() / "logs" / f"rpc_client_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logger: loguru.Logger = main_logger.bind(module="rpc_client")
main_logger.add(log_path, level="DEBUG", filter=lambda record: record["extra"].get("module") == "rpc_client")

import time
import queue
import asyncio
import threading
from settings.settings import settings, MITMType


class Client(object):
    def __init__(self):
        self.messages: queue.Queue[dict] = None
        self.running = False
        self._thread = None

    def start(self):
        if self.running:
            return
        match settings.mitm.type:
            case MITMType.AMATSUKI:
                from mitm.amatsuki import start_proxy, mjai_messages
                self._thread = threading.Thread(target=lambda: asyncio.run(start_proxy(settings.mitm.host, settings.mitm.port)))
                self._thread.start()
                self.messages = mjai_messages
            case MITMType.MAJSOUL:
                from mitm.majsoul import start_proxy, mjai_messages
                self._thread = threading.Thread(target=lambda: asyncio.run(start_proxy(settings.mitm.host, settings.mitm.port)))
                self._thread.start()
                self.messages = mjai_messages
            case MITMType.RIICHI_CITY:
                from mitm.riichi_city import start_proxy, mjai_messages
                self._thread = threading.Thread(target=lambda: asyncio.run(start_proxy(settings.mitm.host, settings.mitm.port)))
                self._thread.start()
                self.messages = mjai_messages
            case MITMType.TENHOU:
                from mitm.tenhou import start_proxy, mjai_messages
                self._thread = threading.Thread(target=lambda: asyncio.run(start_proxy(settings.mitm.host, settings.mitm.port)))
                self._thread.start()
                self.messages = mjai_messages
            case _:
                raise ValueError(f"Unknown MITM type: {settings.mitm.type}")
        self.running = True

    def stop(self):
        if not self.running:
            return
        match settings.mitm.type:
            case MITMType.AMATSUKI:
                from mitm.amatsuki import stop_proxy
                stop_proxy()
            case MITMType.MAJSOUL:
                from mitm.majsoul import stop_proxy
                stop_proxy()
            case MITMType.RIICHI_CITY:
                from mitm.riichi_city import stop_proxy
                stop_proxy()
            case MITMType.TENHOU:
                from mitm.tenhou import stop_proxy
                stop_proxy()
            case _:
                raise ValueError(f"Unknown MITM type: {settings.mitm.type}")
        self.messages = None
        self.running = False
        self._thread.join()
        self._thread = None

    def dump_messages(self) -> list[dict]:
        ans: list[dict] = []
        while not self.messages.empty():
            message = self.messages.get()
            logger.debug(f"Message: {message}")
            ans.append(message)
        return ans
