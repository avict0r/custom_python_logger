import json
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
    _created_loggers = set()  # Class-level set to store created logger names

    def __init__(self, logger_name: str = 'root',
                 level: LogLevels = LogLevels.WARNING,
                 handlers: list = None,
                 console_format: str = "%(log_color)s%(name)s: %(asctime)s | %(levelname)s "
                                       "| %(filename)s:%(lineno)s | %(process)d >>> %(message)s",
                 file_path: str = 'default.log',
                 file_format: str = "[ %(levelname)s ] | %(asctime)s | %(message)s",
                 is_from_config: bool = False):

        """
        CustomLogger constructor.

        Args:
            logger_name (str): Name of the logger. Default is 'root'.
            level (LogLevels): The minimum log level to display. Default is LogLevels.WARNING.
            handlers (list): List of logging.Handler instances to be added to the logger.
            console_format (str): Format string for console logs. Default format includes log colors.
            file_path (str): File path for log file including the file name. Default is 'default.log'.
            file_format (str): Format string for log file. Default is "[ %(levelname)s ] | %(asctime)s | %(message)s".
            is_from_config (bool, optional): Set to True if the logger is being created from a configuration file.
                                            Default is False.

        Raises:
            ValueError: If the logger with the same name already exists.

        Note:
            If 'handlers' is provided, the 'console_handler' and 'file_handler' will not be added automatically
            (unless 'is_from_config' is True). It's recommended to either pass 'handlers' or set 'is_from_config' to True,
            but not both.

        Example:
            # Create a custom logger with default configuration
            logger = CustomLogger()

            # Create a custom logger with a custom level and format, and add custom handlers
            console_handler = ConsoleHandler(format_str="%(asctime)s - %(message)s")
            file_handler = FileHandler(file_path="app.log", format_str="[%(levelname)s] - %(asctime)s - %(message)s")
            logger = CustomLogger(logger_name="my_logger", level=LogLevels.DEBUG, handlers=[console_handler,
             file_handler])
        """
        self._logger_name = logger_name
        self._level = level.value

        # Console handler formatting
        self._console_format = console_format

        # File handler formatting
        self._filename = file_path
        self._file_format = file_format

        self._is_from_config = is_from_config

        # Generating named logger and setting the minimum log level to display
        if self._logger_name not in CustomLogger._created_loggers:
            self._logger = logging.getLogger(name=self._logger_name)
            self._logger.setLevel(level=self._level)
            CustomLogger._created_loggers.add(self._logger_name)  # Add logger name to the set
        else:
            raise ValueError("Logger already exists")

        if handlers:
            self._add_handler(handlers)
        elif not self._is_from_config:
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

    @classmethod
    def from_config_json(cls, json_file_path: str):
        """
        Create a CustomLogger instance using a JSON configuration file.

        Args:
            json_file_path (str): File path to the JSON configuration file.

        Returns:
            CustomLogger: CustomLogger instance initialized based on the configuration in the JSON file.
        """
        with open(json_file_path, 'r') as json_file:
            config_data = json.load(json_file)

        logger_name = config_data.get('logger_name', 'root')
        level = LogLevels[config_data.get('level', 'WARNING').upper()]
        console_format = config_data.get('console_format', "%(log_color)s%(name)s: %(asctime)s | %(levelname)s "
                                                           "| %(filename)s:%(lineno)s | %(process)d >>> %(message)s")
        file_path = config_data.get('file_path', 'default.log')
        file_format = config_data.get('file_format', "[ %(levelname)s ] | %(asctime)s | %(message)s")
        handlers_data = config_data.get('handlers')

        logger = cls(logger_name=logger_name, level=level, console_format=console_format, file_path=file_path,
                     file_format=file_format, is_from_config=True)

        handlers = []
        for handler_data in handlers_data:
            handler_type = handler_data.get('type')
            handler_level = LogLevels[handler_data.get('level', 'WARNING').upper()]
            handler_format_str = handler_data.get('format_str')

            if handler_type == 'ConsoleHandler':
                log_colors = handler_data.get('log_colors', {})
                handler = ConsoleHandler(format_str=handler_format_str, log_colors=log_colors,
                                         level=handler_level.value)
            elif handler_type == 'FileHandler':
                filename = handler_data.get('filename', 'app.log')
                handler = FileHandler(file_path=filename, format_str=handler_format_str,
                                      level=handler_level.value)
            elif handler_type == 'EmailHandler':
                mailhost = handler_data.get('mailhost')
                fromaddr = handler_data.get('fromaddr')
                toaddrs = handler_data.get('toaddrs', [])
                subject = handler_data.get('subject', 'Log Message')
                credentials = handler_data.get('credentials', [])
                handler = EmailHandler(mailhost=mailhost, fromaddr=fromaddr, toaddrs=toaddrs, subject=subject,
                                       credentials=credentials, format_str=handler_format_str,
                                       level=handler_level.value)
            else:
                raise ValueError(f"Unknown handler type: {handler_type}")

            handler.setLevel(handler_level.value)
            handlers.append(handler)

        logger._add_handler(handlers)

        return logger
