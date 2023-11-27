import subprocess
import time


def get_commit_usernames():
    try:
        # Get the last 20 commits and extract unique author names
        commit_log = subprocess.run(['git', 'log', '--format=%an', '-20'],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
        usernames = set(commit_log.strip().split('\n'))
        return list(usernames)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return []


def get_commits_for_user(username):
    try:
        # Get the last 20 commits for a specific user
        commit_log = subprocess.run(
            ['git', 'log', '--oneline', f'--author={username}', '-20'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
        return commit_log.strip().split('\n')

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return []


def gits_visualizer(args):
    try:
        print("Animating commit history...")

        # Get unique usernames from the last 20 commits
        usernames = get_commit_usernames()

        # ASCII art representation of a commit
        commit_art = [
            "   O",
            "  /|\\",
            "  / \\",
        ]

        # Display an animated representation of the commit history for each user
        for username in usernames:
            print("\033c")  # Clear the terminal

            # Display ASCII art and username
            print("\n".join(commit_art))
            print(f"{username} commits:")
            time.sleep(1)  # Adjust the delay as needed

            # Display commit messages for the specific user
            commits = get_commits_for_user(username)
            for commit in commits:
                print(commit)
                time.sleep(0.2)  # Adjust the delay between commits

            time.sleep(1)  # Adjust the delay before switching to the next user

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"ERROR: An exception occurred: {e}")
        return False

    return True
