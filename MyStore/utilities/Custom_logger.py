import inspect
import logging


def CustomLogger(loglevel = logging.DEBUG):

    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("automation.log", mode= 'a')
    file_handler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                                  datefmt= '%d/%m/%y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
