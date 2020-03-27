import logging

import os


class TestLogger:
    __logger = None
    __log_file_name = 'logs.log'

    @classmethod
    def get_logger(cls):
        if not cls.__logger:
            log_file = logging.FileHandler(os.path.join('..', 'log', '{}'.format(cls.__log_file_name)))
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            log_file.setFormatter(formatter)
            cls.__logger = logging.getLogger()
            cls.__logger.setLevel(logging.DEBUG)
            cls.__logger.addHandler(log_file)

        return cls.__logger

    @classmethod
    def delete_all_logs(cls):
        if cls.__log_file_name in os.listdir(os.path.join('..','log')):
            os.remove(os.path.join('..','log',cls.__log_file_name))






