import random
import numpy as np
from .base import ThinkerBase
from .logger import logger

def softmax(xs: list[float], temperature: float = 0.3) -> list[float]:
    """Compute softmax values for each set of scores in xs with temperature scaling."""
    if temperature <= 0:
        raise ValueError("Temperature must be positive.")
    max_x = max(xs)
    exps = np.exp((np.array(xs) - max_x) / temperature)
    sum_of_exps = np.sum(exps)
    return (exps / sum_of_exps).tolist()

class Thinker(ThinkerBase):
    """
    Simulates human-like decision-making delays for an autoplay bot.

    This class tracks the game state and calculates a realistic delay for each action,
    allowing the bot to mimic a human player's reaction time. It's designed to be
    compatible with the Akagi application by overriding some methods from `mjai.Bot`.
    """
    def __init__(self):
        super().__init__()
    
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

        if input is None and input_list is None:
            logger.warning("MJAI message is None, why are we thinking?")
            return 0.0

        if input is None:
            if len(input_list) == 0:
                logger.warning("MJAI message list is empty, why are we thinking?")
                return 0.0
            input = input_list[-1]

        softmax_q = []

        if 'meta' in input:
            meta = input['meta']
            if 'q_values' in meta:
                q_values = meta['q_values']
                if len(q_values) >= 2:
                    sorted_q = sorted(q_values, reverse=True)
                    softmax_q = softmax(sorted_q)

        max_delay = 8.0
        total_delay = 0.0

        ADD_RANDOM_DELAY = True
        ADD_RANDOM_DELAY_MAX = 3.0
        ADD_RANDOM_DELAY_MIN = 1.0
        FIRST_TILE_DISCARD = 4.0
        CAN_RIICHI_THINK = 2.0
        CLOSE_Q_THRESHOLD = 0.005
        TWO_CLOSE_Q_THINK = 2.0
        CONFIDENT_Q_THRESHOLD = 0.995
        CONFIDENT_Q_MAX_DELAY = 2.0
        KAN_THINK = 0.5

        # ==========================================
        # Example 1: No delay after riichi accepted
        if (
            self.self_riichi_accepted
            and not (self.can_agari or self.can_kakan or self.can_ankan)
            and self.can_discard
        ):
            return 0.0
        
        # ==========================================
        # Example 2: If this is the first tile discarded in the round
        #   - Most of the game has a sort tehai animation
        #   - Add a delay to deal with the animation
        if self.last_kawa_tile is None:
            total_delay += FIRST_TILE_DISCARD
        
        # ==========================================
        # Example 3: If we can declare a riichi
        #   - Add a delay to think if we should declare riichi
        if self.can_riichi:
            total_delay += CAN_RIICHI_THINK
        
        # ==========================================
        # Example 4: (Advanced) If meta-information contains in mjai_msg,
        #            we get q_value from it, if there exists two q_values
        #            that are very close to each other, we add a delay 
        #            to simulate like we are thinking between two choices.
        if len(softmax_q) >= 2:
            if abs(softmax_q[0] - softmax_q[1]) < CLOSE_Q_THRESHOLD:
                total_delay += TWO_CLOSE_Q_THINK

        # ==========================================
        # Example 5: (Advanced) If One of the q_values is very close to 1.0,
        #            we can assume that the bot is very sure about its decision,
        #            we can reduce the max_delay to a smaller value.
        if len(softmax_q) >= 1:
            if softmax_q[0] > CONFIDENT_Q_THRESHOLD:
                max_delay = CONFIDENT_Q_MAX_DELAY

        # ==========================================
        # Example 6: If we are going to kan, add a small delay
        if 'type' in input:
            if input['type'] in ['ankan', 'kakan', 'daiminkan']:
                total_delay += KAN_THINK

        # ==========================================
        # Example 7: Add a random delay to simulate human reaction time
        if ADD_RANDOM_DELAY:
            total_delay += random.uniform(ADD_RANDOM_DELAY_MIN, ADD_RANDOM_DELAY_MAX)

        # Clamp the total delay to be within [0, max_delay]
        total_delay = min(max(total_delay, 0.0), max_delay)

        return total_delay
