"""
@Description : This py file is a wrapper on top of python logging module.
@ Author : Sam Mathew
@ Created on : 25/12/2019
@ Modified on : 28/12/2019

"""

# Global imports
import logging
import sys
import os


# Local imports
from trello_auto.core.environment import Environment as EV


class Log(object):

    @staticmethod
    def capture_log():
        """ Capture event logs
        parameter : Path to the event logs
        return : logger instance
        """
        path = EV.REPORT_PATH
        device_name = "trello_auto"

        log = logging.getLogger(path)
        log.setLevel(logging.DEBUG)
        log.handlers = []

        # create file handler which logs even debug messages
        log_file_name = os.path.join(path, "trello_auto.log")

        fh = logging.FileHandler(log_file_name)
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)

        # Create formatter and add it to the handler
        formatter = logging.Formatter(
            '%(asctime)s - {0} - %(levelname)s - %(message)s'.format(
                device_name),
            "%Y-%m-%d %H:%M:%S")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add the handlers to the logger
        log.addHandler(fh)
        log.addHandler(ch)

        log.handlers[-1]

        return log
