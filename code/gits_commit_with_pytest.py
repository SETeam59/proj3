#!/usr/bin/python3

from subprocess import Popen, PIPE


def gits_commit_func_with_pytest(args):
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

        print(stdout_as_str)
        if "failed" in stdout_as_str:
            answer = input("The unit test cases failed, do you still wish to commit? Y/N ")
            if answer=='Y':
                subprocess_command = list()
                subprocess_command.append("git")
                subprocess_command.append("commit")
                commit_message = args.m
                if not commit_message:
                    print("ERROR: gits commit message not present, aborting")
                    return False
                subprocess_command.append("-m")
                subprocess_command.append(commit_message)
                if not args.amend:
                    # do nothing
                    pass
                else:
                    subprocess_command.append("--amend")

                print('Performing commit...')
                print(subprocess_command)
                process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
                stdout, stderr = process.communicate()
                # stdout_as_str = stdout.decode("utf-8")
                # print(stdout_as_str)
                
            else:
                print('Commit aborted')
                return False

        else:
            subprocess_command = list()
            subprocess_command.append("git")
            subprocess_command.append("commit")
            commit_message = args.m
            if not commit_message:
                print("ERROR: gits commit message not present, aborting")
                return False
            subprocess_command.append("-m")
            subprocess_command.append(commit_message)
            if not args.amend:
                # do nothing
                pass
            else:
                subprocess_command.append("--amend")

            print('Performing commit...')
            print(subprocess_command)
            process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate()

    except Exception as e:
        print("ERROR: gits commit command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True