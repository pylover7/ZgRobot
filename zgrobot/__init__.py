__version__ = '2.0.1'
__author__ = 'pylover'
__license__ = 'MIT'

__all__ = ["ZgRoBot"]

try:
    from zgrobot.robot import ZgRoBot
except ImportError:  # pragma: no cover
    pass  # pragma: no cover
