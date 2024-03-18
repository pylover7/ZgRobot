import logging
from datetime import datetime
from loguru import logger

class Logger:
    def __init__(self, level: str = "DEBUG"):
        logging.getLogger().handlers.clear()
        self.logger = logger
        self.logger.add(
            f"log/{datetime.now().strftime('%Y-%m-%d')}.log",
            rotation="10 MB",
            retention="10 days",
            compression="zip",            format="{time} | {level} | {message}",
            level=level,
        )

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
    

zglogger = Logger()
