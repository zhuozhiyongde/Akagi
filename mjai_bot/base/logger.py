from __future__ import annotations

import loguru
from loguru import logger as main_logger
from datetime import datetime
from pathlib import Path

# Log to: "./Logs/mjai_base_<timestamp>.log"
log_path: Path = Path().cwd() / "logs" / f"mjai_base_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logger: loguru.Logger = main_logger.bind(module="mjai_base")
main_logger.add(log_path, level="DEBUG", filter=lambda record: record["extra"].get("module") == "mjai_base")