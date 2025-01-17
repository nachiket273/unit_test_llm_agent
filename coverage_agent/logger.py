"""
Custom Logger Class for logging stuff.
"""
from datetime import datetime
import logging
import pathlib


class Logger:
    """
    Custom logger class that writes the logs to file
    and STDOUT
    """
    @classmethod
    def get_logger(cls, path: str) -> logging.Logger:
        """
        Returns Logger with FileLogger and StreamLogger

        Args:
            path(str) : Path to Log Directory

        Example:
            >>> path = './log'
            >>> clogger = Logger.get_logger(path)

        Return:
            Logger object with FileHnadler and StreamHandler
        """
        log_dir = pathlib.Path(path)
        if not log_dir.exists():
            raise FileNotFoundError(f"Log directory {path} doesn't exists.")
        if not log_dir.is_dir():
            raise Exception(f"Path {path} is not a directory.")

        today = datetime.now().strftime('%Y%m%d')
        clogger = logging.getLogger(__name__)
        clogger.setLevel(logging.DEBUG)

        log_file = log_dir.joinpath(today + ".log")
        if clogger.handlers:
            clogger.handlers.clear()

        fmt = logging.Formatter("%(asctime)s - %(levelname)s"
                                " - %(message)s")

        # File handler for writing to log file
        file_handler = logging.FileHandler(log_file, mode='a')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(fmt)
        clogger.addHandler(file_handler)

        # Stream handler for logging to console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(fmt)
        clogger.addHandler(console_handler)

        return clogger


cust_logger = Logger.get_logger('./log')
