from .logger import logger
from settings.settings import settings, MITMType
    
class AutoPlay(object):
    def __init__(self):
        pass
        
    @property
    def target_window(self) -> None:
        """
        Returns the target window object.
        The target window is the first visible window in the list of windows.
        """
        return None

    def set_bot(self, bot):
        """
        Args:
            bot (AkagiBot): The AkagiBot instance to be used.

        Returns:
            None: No return value.
        """
        pass

    def set_autoplay(self):
        """
        Args:
            autoplay (AutoPlayBase): The AutoPlayBase instance to be used.

        Returns:
            None: No return value.
        """
        match settings.mitm.type:
            case MITMType.AMATSUKI:
                return
            case MITMType.MAJSOUL:
                return
            case MITMType.RIICHI_CITY:
                return
            case MITMType.TENHOU:
                return
            case _:
                logger.error(f"Unknown MITM type: {settings.mitm.type}")
                return

    def get_windows(self) -> list:
        """
        Returns a list of WindowObject instances for all visible windows.
        Each WindowObject contains the window handle (hwnd) and window name.
        """
        return []
    
    def select_window(self, hwnd: int) -> None:
        """
        Selects a window by its handle (hwnd).
        """
        pass

    def check_window(self) -> bool:
        """
        Checks if the target window is valid and visible.
        Returns True if the target window is valid, False otherwise.
        """
        return False
    
    def auto_select_window(self) -> None:
        """
        Automatically selects the window based on the current settings.
        """
        pass

    def act(self, mjai_msg: dict) -> bool:
        """
        Given a MJAI message, this method processes the message and performs the corresponding action.

        Args:
            mjai_msg (dict): The MJAI message to process.

        Returns:
            bool: True if the action was performed, False otherwise.
        """
        return False
