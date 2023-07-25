import logging
import logging.config
from .enums.levels import LogLevels
from .enums.handlers import HandlerType
from .handlers import ConsoleHandler, FileHandler, EmailHandler


# TODO: logFormatter
class CustomLogger:
    def __init__(self, logger_name: str = 'custom_logger',
                 level: LogLevels = LogLevels.DEBUG,
                 handler_type: HandlerType = HandlerType.CONSOLE,
                 console_format: str = "[ %(levelname)s ] | %(asctime)s | %(message)s",
                 filename: str = 'default.log',
                 file_format: str = "[ %(levelname)s ] | %(asctime)s | %(message)s",
                 email_settings: dict | None = None):

        self._level = level.value
        self._handler_type = handler_type

        # Console handler formatting
        self._console_format = console_format

        # File handler formatting
        self._filename = filename
        self._file_format = file_format

        # Email handler formatting
        self._email_settings = email_settings

        # Generating named logger and setting the minimum log level to display
        self._logger = logging.getLogger(name=logger_name)
        self._logger.setLevel(level=self._level)

        self._add_handler()

    # LOG levels
    def debug(self, message: str) -> None:
        self._logger.debug(msg=message)

    def info(self, message: str) -> None:
        self._logger.info(msg=message)

    def warning(self, message: str) -> None:
        self._logger.warning(msg=message)

    def error(self, message: str) -> None:
        self._logger.error(msg=message)

    def critical(self, message: str) -> None:
        self._logger.critical(msg=message)

    # Change Log level threshold
    def set_level(self, level: LogLevels):
        self._level = level.value
        self._logger.setLevel(level=self._level)

    # Handler manager
    def _add_handler(self) -> None:
        if self._handler_type is HandlerType.CONSOLE:
            console_handler = ConsoleHandler(format_str=self._console_format)
            self._logger.addHandler(console_handler)

        elif self._handler_type is HandlerType.FILE:
            file_handler = FileHandler(filename=self._filename, format_str=self._file_format)
            self._logger.addHandler(file_handler)

        elif self._handler_type is HandlerType.EMAIL and self._email_settings:
            email_handler = EmailHandler(
                mailhost=self._email_settings['mailhost'],
                fromaddr=self._email_settings['fromaddr'],
                toaddrs=self._email_settings['toaddrs'],
                subject=self._email_settings.get('subject', 'Log Message'),
                credentials=self._email_settings.get('credentials'),
                format_str=self._file_format
            )
            self._logger.addHandler(email_handler)

        else:
            raise ValueError("Unknown handler type")
