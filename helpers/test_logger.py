import logging

import os
import sys


class TestLogger:
    __logger = None
    __log_file_name = 'logs.log'

    @classmethod
    def get_logger(cls):
        if not cls.__logger:
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

           # file_handler = logging.FileHandler(cls.__log_file_name)
           # file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            cls.__logger = logging.getLogger()
            cls.__logger.setLevel(logging.DEBUG)

            #cls.__logger.addHandler(file_handler)
            cls.__logger.addHandler(console_handler)

        return cls.__logger

    @classmethod
    def delete_all_logs(cls):
        if cls.__log_file_name in os.listdir(os.path.join('..', 'log')):
            os.remove(os.path.join('..', 'log', cls.__log_file_name))
