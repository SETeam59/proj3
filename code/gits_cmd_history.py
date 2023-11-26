#!/usr/bin/python3

import gits_logging
from subprocess import Popen, PIPE


def gits_cmd_history_func(args):
    """
    Function that shows history of commands
    """
    try:
        # Assuming `gits_logger` is a logger instance
        gits_logging.gits_logger.info("Showing command history...")

        # Read command history from the file
        with open('command_history.txt', 'r') as file:
            command_history = file.readlines()

        # Print command history
        for command in command_history:
            print(command.strip())

    except Exception as e:
        gits_logging.gits_logger.error("gits_cmd_history_func caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits_cmd_history_func caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
