import logging
import random

class MyLogger():
    LEVEL_MAP = {'debug': logging.DEBUG, 'info': logging.INFO, 'warning': logging.WARNING, 'error': logging.ERROR,
                 'critical': logging.CRITICAL}
    def __init__(self, level: str, filename: str):
        self.logger = logging.getLogger(str(random.random()))
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(filename=filename, encoding='utf-8')
        file_handler.setLevel(MyLogger.LEVEL_MAP[level])

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(logging.StreamHandler())
        self.logger.addHandler(file_handler)
        self.levels = {'debug': self.logger.debug, 'warning': self.logger.warning, 'info': self.logger.info,
                       'error': self.logger.error, 'critical': self.logger.critical}

    def log(self, level, text):
        self.levels[level](text)
