from __future__ import annotations

import loguru
from loguru import logger as main_logger
from datetime import datetime
from pathlib import Path

# Log to: "./Logs/akagi_<timestamp>.log"
log_path = Path().cwd() / "logs" / f"akagi_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logger: loguru.Logger = main_logger.bind(module="akagi")
main_logger.add(log_path, level="DEBUG", filter=lambda record: record["extra"].get("module") == "akagi")
