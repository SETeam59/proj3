import subprocess
from subprocess import PIPE

def my_git_squash(args):
    try:
        squash_command = list()
        squash_command.append("git")
        squash_command.append("reset")
        squash_command.append("--soft")
        
        commit_message = args.m
        num_commits_to_squash = args.n

        print(commit_message)
        print(num_commits_to_squash)

        if not commit_message:
            print("ERROR: Commit message not provided, aborting")
            return False

        if not num_commits_to_squash:
            print("ERROR: Please provide the number of commits to squash")
            return False

        squash_command.append(f"HEAD~{num_commits_to_squash}")

        process_reset = subprocess.Popen(squash_command, stdout=PIPE, stderr=PIPE)
        stdout_reset, stderr_reset = process_reset.communicate()
        print(stdout_reset.decode("utf-8"))

        # Stage changes
        stage_command = list()
        stage_command.append("git")
        stage_command.append("add")
        stage_command.append(".")

        process_stage = subprocess.Popen(stage_command, stdout=PIPE, stderr=PIPE)
        stdout_stage, stderr_stage = process_stage.communicate()
        print(stdout_stage)

        # Commit squashed changes
        commit_command = list()
        commit_command.append("git")
        commit_command.append("commit")
        commit_command.append("-m")
        commit_command.append(commit_message)

        process_commit = subprocess.Popen(commit_command, stdout=PIPE, stderr=PIPE)
        stdout_commit, stderr_commit = process_commit.communicate()
        print(stdout_commit.decode("utf-8"))
        print("Squash completed. Check your new git log.")

    except Exception as e:
        print("ERROR: An exception occurred during git squash")
        print("ERROR: {}".format(str(e)))
        return False

    return True
