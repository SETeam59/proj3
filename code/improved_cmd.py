import subprocess
import re
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
from prompt_toolkit.history import FileHistory

# List of predefined GITS commands for auto-complete
GITS_COMMANDS = [
    "hello_world", "cmd_history", "set", "add", "commit", "create", "upstream", "profile", "sync",
    "super-reset", "rebase", "reset", "push", "checkout", "unstage", "status", "diff",
    "init", "all-branch", "remote-branch", "commit_with_test", "stats", "commit_tree",
    "tag", "describe"
]

# Function to execute GITS command
def execute_gits_command(text):
    command = re.findall(r'[^"\s]+|"[^"]*"', text)
    command_list = ['python3', 'code/gits.py'] + command

    try:
        # Execute the GITS command and capture the output
        result = subprocess.check_output(command_list, stderr=subprocess.STDOUT, text=True)
        print(result)
        save_command_to_history(text)
    except subprocess.CalledProcessError as e:
        print("Error: " + e.output)
    except Exception as e:
        print("An error occurred: " + str(e))

# Function to save command to history
def save_command_to_history(command):
    with open('command_history.txt', 'a') as file:
        file.write(command + '\n')

# Custom style for syntax highlighting
style = Style.from_dict({
    'prompt': '#00ff00',
    'commands': '#0000ff',
    'output': '#ff0000',
})

# Completer for auto-suggestions
completer = WordCompleter(GITS_COMMANDS)

# Main loop using prompt_toolkit
while True:
    user_input = prompt('> ',
                        completer=completer,
                        style=style,
                        history=FileHistory('command_history.txt'),
                        mouse_support=True)

    if user_input.lower() == 'exit':
        break

    execute_gits_command(user_input)
