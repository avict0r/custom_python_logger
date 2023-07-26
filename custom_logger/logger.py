import logging
import logging.config
from enum import Enum
from .handlers import ConsoleHandler, FileHandler, EmailHandler


class LogLevels(Enum):
    NONSET = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


class CustomLogger:
    def __init__(self, logger_name: str = 'root',
                 level: LogLevels = LogLevels.WARNING,
                 handlers: list = None,
                 console_format: str = "%(log_color)s%(name)s: %(asctime)s | %(levelname)s "
                                       "| %(filename)s:%(lineno)s | %(process)d >>> %(message)s",
                 file_path: str = 'default.log',
                 file_format: str = "[ %(levelname)s ] | %(asctime)s | %(message)s",
                 email_settings: dict | None = None):

        """
        CustomLogger constructor.

        Args:
            logger_name (str): Name of the logger. Default is 'root'.
            level (LogLevels): The minimum log level to display. Default is LogLevels.WARNING.
            handlers (list): List of logging.Handler instances to be added to the logger.
            console_format (str): Format string for console logs. Default format includes log colors.
            file_path (str): File path for log file including the file name. Default is 'default.log'.
            file_format (str): Format string for log file. Default is "[ %(levelname)s ] | %(asctime)s | %(message)s".
        """

        self._level = level.value

        # Console handler formatting
        self._console_format = console_format

        # File handler formatting
        self._filename = file_path
        self._file_format = file_format

        # Generating named logger and setting the minimum log level to display
        self._logger = logging.getLogger(name=logger_name)
        self._logger.setLevel(level=self._level)

        if handlers:
            self._add_handler(handlers)
        else:
            console_handler = ConsoleHandler(format_str=self._console_format)
            file_handler = FileHandler(file_path=self._filename, format_str=self._file_format)
            self._add_handler([console_handler, file_handler])

    # LOG levels
    def debug(self, message: str) -> None:
        """
        Log a message with DEBUG log level.

        Args:
            message (str): The message to be logged.
        """
        self._logger.debug(msg=message)

    def info(self, message: str) -> None:
        """
        Log a message with INFO log level.

        Args:
            message (str): The message to be logged.
        """
        self._logger.info(msg=message)

    def warning(self, message: str) -> None:
        """
        Log a message with WARNING log level.

        Args:
            message (str): The message to be logged.
        """
        self._logger.warning(msg=message)

    def error(self, message: str) -> None:
        """
        Log a message with ERROR log level.

        Args:
            message (str): The message to be logged.
        """
        self._logger.error(msg=message)

    def critical(self, message: str) -> None:
        """
        Log a message with CRITICAL log level.

        Args:
            message (str): The message to be logged.
        """
        self._logger.critical(msg=message)

    # Change Log level threshold
    def set_level(self, level: LogLevels):
        """
        Change the log level threshold.

        Args:
            level (LogLevels): The new log level to set.
        """
        self._level = level.value
        self._logger.setLevel(level=self._level)

    # Handler manager
    def _add_handler(self, handlers: list) -> None:
        """
        Add a list of logging.Handler instances to the logger.

        Args:
            handlers (list): List of logging.Handler instances to be added.
        """
        for handler in handlers:
            if isinstance(handler, logging.Handler):
                self._logger.addHandler(handler)
            else:
                raise ValueError("Handler should be an instance of logging.Handler")
