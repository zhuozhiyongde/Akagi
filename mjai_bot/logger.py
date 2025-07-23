from __future__ import annotations

import loguru
from loguru import logger as main_logger
from datetime import datetime
from pathlib import Path

# Log to: "./Logs/mjai_controller_<timestamp>.log"
log_path: Path = Path().cwd() / "logs" / f"mjai_controller_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logger: loguru.Logger = main_logger.bind(module="mjai_controller")
main_logger.add(log_path, level="DEBUG", filter=lambda record: record["extra"].get("module") == "mjai_controller")