from __future__ import annotations

import loguru
from loguru import logger as main_logger
from datetime import datetime
from pathlib import Path

# Log to: "./Logs/autoplay_<timestamp>.log"
log_path: Path = Path().cwd() / "logs" / f"autoplay_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logger: loguru.Logger = main_logger.bind(module="autoplay")
main_logger.add(log_path, level="DEBUG", filter=lambda record: record["extra"].get("module") == "autoplay")