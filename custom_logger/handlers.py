import sys
import logging
import logging.handlers
import colorlog

log_colors = {
    'DEBUG': 'white',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

stdout = colorlog.StreamHandler(stream=sys.stdout)


class ConsoleHandler(logging.StreamHandler):
    """Custom console logging handler with color support."""

    def __init__(self, format_str: str, log_colors: dict = log_colors, level: int = logging.DEBUG):
        """
        Initialize the ConsoleHandler.

        Args:
            format_str (str): The format string for log messages.
            level (int, optional): The log level for the handler. Default is logging.DEBUG.
            log_colors (dict): Dictionary containing log level names as keys and color names as values.

                Example: {
                    'DEBUG': 'cyan',
                    'INFO': 'green',
                    'WARNING': 'yellow',
                    'ERROR': 'red',
                    'CRITICAL': 'bold_red'
                }
        """
        super().__init__()
        formatter = colorlog.ColoredFormatter(format_str, log_colors=log_colors)
        self.setFormatter(formatter)
        self.setLevel(level)


class FileHandler(logging.FileHandler):
    """Custom file logging handler."""

    def __init__(self, file_path: str, format_str: str, level: int = logging.WARNING):
        """
        Initialize the FileHandler.

        Args:
            file_path (str): File path for the log file.
            format_str (str): The format string for log messages.
            level (int, optional): The log level for the handler. Default is logging.WARNING.
        """
        super().__init__(file_path)
        formatter = logging.Formatter(format_str)
        self.setFormatter(formatter)
        self.setLevel(level)


class EmailHandler(logging.handlers.SMTPHandler):
    """Custom email logging handler."""

    def __init__(self, mailhost: str, fromaddr: str, toaddrs: list, subject: str, credentials: tuple,
                 format_str: str, level: int = logging.ERROR):
        """
        Initialize the EmailHandler.

        Args:
            mailhost (str): The SMTP server to send the emails.
            fromaddr (str): The sender email address.
            toaddrs (list): List of recipient email addresses.
            subject (str): Subject line for the email.
            credentials (tuple): Tuple containing username and password for SMTP authentication.
            format_str (str): The format string for log messages.
            level (int, optional): The log level for the handler. Default is logging.ERROR.
        """
        super().__init__(mailhost, fromaddr, toaddrs, subject, credentials)
        formatter = logging.Formatter(format_str)
        self.setFormatter(formatter)
        self.setLevel(level)
