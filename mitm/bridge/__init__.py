# __init__.py
from .bridge_base import BridgeBase
from .amatsuki import AmatsukiBridge
from .majsoul import MajsoulBridge
from .tenhou import TenhouBridge

__all__ = ['BridgeBase', 'AmatsukiBridge', 'MajsoulBridge', 'TenhouBridge']