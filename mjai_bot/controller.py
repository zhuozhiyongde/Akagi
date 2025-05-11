import os
import json
import importlib
from .base.bot import Bot
from .logger import logger


class Controller(object):
    def __init__(self):
        self.available_bots: list[type[Bot]] = []
        self.available_bots_names: list[str] = []
        self.bot: Bot | None = None
        self.list_available_bots()
        self.bot: Bot = self.available_bots[0]() if self.available_bots else None

    def list_available_bots(self) -> list[type[Bot]]:
        bots = []
        bots_names = []
        # Get the current package folder
        current_dir = os.path.dirname(__file__)
        for item in os.listdir(current_dir):
            if item.startswith("__"):
                continue
            if item == "base":
                continue
            dir_path = os.path.join(current_dir, item)
            # Check if folder and has a bot.py file
            if os.path.isdir(dir_path) and os.path.exists(os.path.join(dir_path, "bot.py")):
                try:
                    # Import the bot module using a relative import
                    module = importlib.import_module(f".{item}.bot", package=__package__)
                    if hasattr(module, "Bot"):
                        bot_class = getattr(module, "Bot")
                        bots.append(bot_class)
                        bots_names.append(item)
                except Exception as e:
                    # Logging error or handling exception
                    logger.error(f"Error importing bot from {item}: {e}")
        self.available_bots = bots
        self.available_bots_names = bots_names
        return bots

    def react(self, events: list[dict]) -> dict:
        if not self.bot:
            logger.error("No bot available")
            return {"type": "none"}
        ans = self.bot.react(json.dumps(events, separators=(",", ":")))
        return json.loads(ans)

    def choose_bot_index(self, bot_index: int) -> bool:
        if 0 <= bot_index < len(self.available_bots):
            self.bot = self.available_bots[bot_index]()
            return True
        return False
    
    def choose_bot_name(self, bot_name: str) -> bool:
        if bot_name in self.available_bots_names:
            index = self.available_bots_names.index(bot_name)
            self.bot = self.available_bots[index]()
            return True
        return False
