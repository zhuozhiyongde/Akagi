# __init__.py
from .bridge_base import BridgeBase
from .amatsuki import AmatsukiBridge
from .majsoul import MajsoulBridge
from .riichi_city import RiichiCityBridge
from .tenhou import TenhouBridge

__all__ = ['BridgeBase', 'AmatsukiBridge', 'RiichiCityBridge', 'MajsoulBridge', 'TenhouBridge']