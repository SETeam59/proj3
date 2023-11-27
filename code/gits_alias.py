import subprocess
from subprocess import PIPE


def default_alias(args):
    print("default alias")


def add_alias(args):
    try:
        cmd = ['git', 'config', '--global', f'alias.{args.a}', args.c]
        process = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE)
        process.communicate()
        print(f'{args.a} -> {args.c}')
        return True
    except Exception as e:
        print("ERROR: gits alias command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False


def remove_alias(args):
    try:
        cmd = ['git', 'config', '--global', '--unset', f'alias.{args.alias}']
        process = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE)
        process.communicate()
        print(f'Removed alias.{args.alias}')
        return True
    except Exception as e:
        print("ERROR: gits alias command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False


def update_alias(args):
    try:
        command = subprocess.check_output(['git', 'config', '--get', f'alias.{args.old}'], universal_newlines=True).strip()
        remove_process = subprocess.Popen(['git', 'config', '--global', '--unset', f'alias.{args.old}'], stdout=PIPE, stderr=PIPE)
        add_process = subprocess.Popen(['git', 'config', '--global', f'alias.{args.new}', command], stdout=PIPE, stderr=PIPE)
        remove_process.communicate()
        add_process.communicate()
        print(f"Replaced {args.old} with {args.new}")
        return True
    except Exception as e:
        print("ERROR: gits alias command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False


def list_alias(args):
    try:
        if len(args.aliases) == 0:
            result = []
            try:
                result = subprocess.check_output(['git', 'config', '--get-regexp', '^alias'], universal_newlines=True).strip()
            except Exception:
                pass
            if len(result) == 0:
                print("No current aliases")
                return False
            lines = result.split('\n')
            for line in lines:
                match = line.split(' ', 1)
                if len(match) == 2:
                    alias_name = match[0]
                    command = match[1]
                    print(f"{alias_name} -> {command}")
        else:
            invalid = []
            for n in args.aliases:
                result = subprocess.check_output(['git', 'config', '--get-regexp', f'^alias.{n}'], universal_newlines=True).strip()
                if result:
                    lines = result.split('\n')
                    for line in lines:
                        match = line.split(' ', 1)
                        if len(match) == 2:
                            alias_name = match[0]
                            command = match[1]
                            print(f"{alias_name} -> {command}")
                else:
                    invalid.append(n)
            for i in invalid:
                print(f"Invalid alias: {i}")
        return True
    except Exception as e:
        print("ERROR: gits alias command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
