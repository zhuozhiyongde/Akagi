import json
import traceback
from mjai import Bot
from dataclasses import dataclass
from mjai.mlibriichi.state import ActionCandidate, PlayerState  # type: ignore
from .logger import logger

class ThinkerBase(Bot):
    """
    Simulates human-like decision-making delays for an autoplay bot.

    This class tracks the game state and calculates a realistic delay for each action,
    allowing the bot to mimic a human player's reaction time. It's designed to be
    compatible with the Akagi application by overriding some methods from `mjai.Bot`.
    """
    def __init__(self):
        super().__init__()
        self.is_3p = False

    def _react(self, input: dict = None, input_list: list[dict] = None) -> None:
        try:
            if input:
                events = [input]
            elif input_list:
                events = input_list
            else:
                raise ValueError("Empty input")
            if len(events) == 0:
                raise ValueError("Empty events")
            for event in events:
                if event["type"] == "start_game":
                    self.player_id = event["id"]
                    self.player_state = PlayerState(self.player_id)
                    self.is_3p = False
                    self.__discard_events = []
                    self.__call_events = []
                    self.__dora_indicators = []
                if event["type"] == "start_kyoku":
                    if (
                        # event["bakaze"] == "E" and
                        # event["honba"] == 0 and
                        # event["kyoku"] == 1 and
                        # event["kyotaku"] == 0 and
                        # event["oya"] == 0 and
                        # event["scores"][3] == 0
                        event["scores"][0] == 35000 and
                        event["scores"][1] == 35000 and
                        event["scores"][2] == 35000 and
                        event["scores"][3] == 0
                    ):
                        self.is_3p = True
                if event["type"] == "start_kyoku" or event["type"] == "dora":
                    self.__dora_indicators.append(event["dora_marker"])
                if event["type"] == "dahai":
                    self.__discard_events.append(event)
                if event["type"] in [
                    "chi",
                    "pon",
                    "daiminkan",
                    "kakan",
                    "ankan",
                ]:
                    self.__call_events.append(event)
                # This is a patch for Three-Player-Mahjong, since the
                # smly/mjai library does not support 3P Mahjong.
                if event["type"] == "nukidora":
                    logger.debug(f"Event: {event}")
                    replace_event = {
                        "type": "dahai",
                        "actor": event["actor"],
                        "pai": "N",
                        "tsumogiri": self.last_self_tsumo == "N" and event["actor"] == self.player_id,
                    }
                    self.__discard_events.append(replace_event)
                    self.action_candidate = self.player_state.update(
                        json.dumps(replace_event)
                    )
                    continue

                logger.debug(f"Event: {event}")
                self.action_candidate = self.player_state.update(
                    json.dumps(event)
                )

        except Exception as e:
            logger.error(f"Exception: {str(e)}")
            logger.error(traceback.format_exc())

    def react(self, input: dict = None, input_list: list[dict] = None) -> float:
        """
        React to the game state update.

        This method processes the input events, updates the internal game state,
        and calculates a delay to simulate human-like reaction time.
        Returns:
            float: The calculated delay in seconds.
        """
        self._react(input=input, input_list=input_list)
        delay = self.think(input=input, input_list=input_list)
        return delay
    
    @property
    def can_act_3p(self) -> bool:
        """
        Check if the bot can act in 3-player mode.
        """
        return (
            self.can_discard or
            self.can_riichi or
            self.can_pon or
            self.can_agari or
            self.can_ryukyoku or
            self.can_kan 
            # self.tehai_vec34[9*3+3] > 0 # nukidora
        )
    
    def think(self, input: dict = None, input_list: list[dict] = None) -> float:
        """
        Compute and return the delay (seconds) after base state update.
        Subclasses MUST implement this method.

        For the avaliable parameters in this Bot, please refer to mjai.Bot class.
        https://github.com/smly/mjai.app/blob/main/python/mjai/bot/base.py

        Args:
            input (dict): The MJAI message to process.
            input_list (list[dict]): A list of MJAI messages to process.
            Only one of input or input_list should be provided.

        Returns:
            float: The calculated delay in seconds.
        """
        raise NotImplementedError("Subclasses must implement this method.")