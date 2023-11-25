import json
import os

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
SETTINGS_PATH = os.path.join(CURR_DIR, '..', 'configurations', 'nicknames.json')

def read_nicknames_settings():
    try:
        with open(SETTINGS_PATH, 'r') as file:
            settings = json.load(file)
    except FileNotFoundError:
        settings = {}
    
    return settings

def write_nickname_settings(nicknames):
    with open(SETTINGS_PATH, 'w') as file:
        json.dump(nicknames, file, indent=2)


def nickname_default(args):
    print()
    print("Welcome to gits nicknames!")
    print("For any gits command, you can use your own nickname!")
    print("Choose between add, remove, update, and list")
    print()

def add_nickname(args):
    nicknames = read_nicknames_settings()
    nicknames[args.n] = args.c
    write_nickname_settings(nicknames)
    print(f"Add nickname {args.n} for command {args.c}")
   

def remove_nickname(args):
    nicknames = read_nicknames_settings()
    if args.nickname in nicknames:
        del nicknames[args.nickname]
        write_nickname_settings(nicknames)
        print(f"Nickname '{args.nickname}' removed.")
    else:
        print(f"Nickname '{args.nickname}' not found.")

def update_nickname(args):
    nicknames = read_nicknames_settings()
    if args.o in nicknames:
        nicknames[args.n] = nicknames.pop(args.o)
        write_nickname_settings(nicknames)
        print(f"Nickname '{args.o}' updated to {args.n}.")
    else:
        print(f"Nickname '{args.o}' not found.")

def list_nickname(args):
    nicknames = read_nicknames_settings()
    # Go through every nickname in the settings
    if len(args.nicknames) == 0:
        for n, c in nicknames.items():
            print(f"{n} -> {c}")
    # Go though every nickname listed by the user
    else:
        invalid = []
        for n in args.nicknames:
            print(f"{n} -> {nicknames[n]}") if n in nicknames else invalid.append(n)
        for i in invalid:
            print(f"Invalid nickname: {i}")
