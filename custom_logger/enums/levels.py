from enum import Enum


class LogLevels(Enum):
    NONSET = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50