import logging
import logging.handlers


class ConsoleHandler(logging.StreamHandler):
    def __init__(self, format_str: str):
        super().__init__()

        log_colors = {
            'DEBUG': 'white',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }

        formatter = logging.Formatter(format_str)
        self.setFormatter(formatter)


class FileHandler(logging.FileHandler):
    def __init__(self, filename: str, format_str: str):
        super().__init__(filename)
        formatter = logging.Formatter(format_str)
        self.setFormatter(formatter)


class EmailHandler(logging.handlers.SMTPHandler):
    def __init__(self, mailhost: str, fromaddr: str, toaddrs: list, subject: str, credentials: tuple,
                 format_str: str):
        super().__init__(mailhost, fromaddr, toaddrs, subject, credentials)
        formatter = logging.Formatter(format_str)
        self.setFormatter(formatter)
