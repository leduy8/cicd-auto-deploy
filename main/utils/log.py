import json
import logging
import sys

from main import config


class LoggerService:
    @staticmethod
    def _setup_logger(name):
        logger = logging.getLogger(name)
        logger.setLevel(config.LOGGING_LEVEL)

        formatter = logging.Formatter("[%(asctime)s][%(name)s][%(levelname)s] %(message)s")

        handler = logging.StreamHandler(stream=sys.stdout)
        handler.setFormatter(formatter)

        if not logger.hasHandlers():
            logger.addHandler(handler)
        logger.propagate = False

        return logger

    __LOGGERS = {}

    def __init__(self, name):
        try:
            config.LOGGING_LEVEL
        except AttributeError:
            raise ValueError("Logging level not defined in the configuration.")

        if name in self.__LOGGERS:
            self.logger = self.__LOGGERS[name]
        else:
            self.logger = self._setup_logger(name)
            self.__LOGGERS[name] = self.logger

    def info(self, message, **kwargs):
        return self._log(level=logging.INFO, message=message, **kwargs)

    def debug(self, message, **kwargs):
        return self._log(level=logging.DEBUG, message=message, **kwargs)

    def warning(self, message, **kwargs):
        return self._log(level=logging.WARNING, message=message, **kwargs)

    def error(self, message, **kwargs):
        return self._log(level=logging.ERROR, message=message, **kwargs)

    def exception(self, message, **kwargs):
        # Only be used when there's an exception
        return self._log(level=logging.CRITICAL, message=message, **kwargs)

    def _log(self, level, message, data=None):
        # Won't call this function to log, use other logs instead
        if data:
            message = f"{message} | {json.dumps(data, default=str)}"

        if level == logging.CRITICAL:
            self.logger.exception(message)
        else:
            self.logger.log(level, message)
