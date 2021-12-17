import inspect
import logging, coloredlogs


class CreateLogger:

    @staticmethod
    def logger_creation(file_name):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        if not logger.handlers:
            f_handler = logging.FileHandler(file_name + ".log")
            f_format = logging.Formatter("%(asctime)s || %(levelname)s || %(message)s")
            f_handler.setFormatter(f_format)

            logger.addHandler(f_handler)
        logger.setLevel(logging.INFO)

        return logger
