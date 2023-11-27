#!/usr/bin/python3

from subprocess import Popen, PIPE


def gits_all_branch_func(args):
    """
    Function to list all the branches.
    Performs operation as similar to git
    branch command
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("branch")
        subprocess_command.append("-a")
        process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        stdout = stdout.decode("utf-8")
        
        branches = list(filter(None, stdout.split("\n")))
        for branch in branches:
            print(branch)

    except Exception as e:
        print("ERROR: gits branch command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
