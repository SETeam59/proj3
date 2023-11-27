#!/usr/bin/python3

from subprocess import Popen, PIPE

def gits_unit_test_check(args):
    """
    Function that commit files as staged in the git command line internface
    Performs operation as similar to git commit command.
    Future additions : user can specify if the commit should be rejected , if the unit test fails.
    """
    try:
        subprocess_command = list()
        subprocess_command.append("pytest")
        subprocess_command.append("test")
        process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()

        stdout_as_str = stdout.decode("utf-8")

        # print(stdout_as_str)
        if "failed" in stdout_as_str:
            answer = input("The unit test cases failed, do you still wish to commit? Y/N ")
            if answer=='Y':
                Popen('python3 gits_commit.py')
            else:
                print('Commit aborted')
                return False


    except Exception as e:
        print("ERROR: gits unit test check caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
