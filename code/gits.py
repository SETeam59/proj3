#!/usr/bin/python3

import sys
import argparse
from gits_logging import init_gits_logger
from gits_hello import gits_hello_world
from gits_cmd_history import gits_cmd_history_func
from gits_add import gits_add_func
from gits_commit import gits_commit_func
from gits_set import gits_set_func
from gits_setupstream import upstream
from gits_create_branch import create_branch
from gits_super_reset import super_reset
from gits_push import gits_push_func
from gits_init import gits_init_func
from gits_all_branch import gits_all_branch_func
from gits_remote_branch import gits_remote_branch_func
from gits_checkout import checkout
from gits_rebase import gits_rebase
from gits_reset import gits_reset
from gits_unstage import unstage
from gits_profile import gits_set_profile
from gits_pr_update import gits_pr_update_func
from gits_status import gits_status
from gits_diff import gits_diff
from gits_sync import gits_sync
from gits_visualizer import gits_visualizer
from gits_nickname import nickname_default, add_nickname, remove_nickname, list_nickname, update_nickname, read_nicknames_settings
from gits_alias import default_alias, add_alias, remove_alias, list_alias, update_alias
from gits_commit_with_pytest import gits_commit_func_with_pytest

from gits_stats import get_stats
from gits_commit_tree import gits_commit_tree
from gits_tag import gits_tag_func
from gits_describe import gits_describe
from gits_squash import my_git_squash


logger_status = init_gits_logger()
if not logger_status:
    print("ERROR: logger not initialised")
    sys.exit(1)

parser = argparse.ArgumentParser()
parser.set_defaults(func=lambda _: parser.print_help())
subparsers = parser.add_subparsers()

gits_hello_subparser = subparsers.add_parser(
    'hello_world', help='Print "hello world" to test gits integration')
gits_hello_subparser.set_defaults(func=gits_hello_world)

gits_cmd_history_func_subparser = subparsers.add_parser('cmd_history')
gits_cmd_history_func_subparser.set_defaults(func=gits_cmd_history_func)

gits_set_subparser = subparsers.add_parser('set', help='Set the parent branch')
gits_set_subparser.add_argument('--parent', help='git parent branch')
gits_set_subparser.set_defaults(func=gits_set_func)

gits_add_subparser = subparsers.add_parser('add', help='Stage files')
gits_add_subparser.add_argument('file_names',
                                metavar='N',
                                type=str,
                                nargs='+',
                                help='all file names')
gits_add_subparser.set_defaults(func=gits_add_func)


gits_commit_subparser = subparsers.add_parser('commit', help='Commit files')
gits_commit_subparser.add_argument('-m',
                                   required=True,
                                   help='git commit message')
gits_commit_subparser.add_argument('--amend',
                                   action='store_true',
                                   help='amend commit message')
gits_commit_subparser.set_defaults(func=gits_commit_func)

gits_squash_subparser = subparsers.add_parser('squash')
gits_squash_subparser.add_argument('-n',
                                   required=True,
                                   help='number of commits to squash')
gits_squash_subparser.add_argument('-m',
                                   required=True,
                                   help='git squash commit message')

gits_squash_subparser.set_defaults(func=my_git_squash)

gits_create_subparser = subparsers.add_parser(
    'create', help='Check out a new branch from local master')
gits_create_subparser.add_argument('-b', help="branch name to create")
gits_create_subparser.set_defaults(func=create_branch)


gits_upstream_subparser = subparsers.add_parser(
    'upstream', help='Change the upstream branch')
gits_upstream_subparser.add_argument('--remote',
                                     help='the remote branch name')
gits_upstream_subparser.add_argument('--local',
                                     help="local branch name")
gits_upstream_subparser.add_argument('--upstream',
                                     help="the upstream branch name")
gits_upstream_subparser.set_defaults(func=upstream)

gits_profile_subparser = subparsers.add_parser(
    'profile', help='Change git profile')
gits_profile_subparser.set_defaults(func=gits_set_profile)
gits_profile_subparser.add_argument('--email',
                                    required=True,
                                    help='email to be used')
gits_profile_subparser.add_argument('--name',
                                    required=True,
                                    help='name to be used')

gits_pr_subparser = subparsers.add_parser(
    'sync', help='Sync local master with remote master')
gits_pr_subparser.set_defaults(func=gits_pr_update_func)
gits_pr_subparser.add_argument('--upstream', nargs='?')

gits_super_reset_subparser = subparsers.add_parser(
    'super-reset', help='Remove the current repository and clone it again')
gits_super_reset_subparser.add_argument(
    '--name', help="Name of the repository to super reset")
gits_super_reset_subparser.set_defaults(func=super_reset)

gits_rb_subparser = subparsers.add_parser(
    'rebase', help='Automatically rebase off of master')
gits_rb_subparser.set_defaults(func=gits_rebase)

gits_reset_subparser = subparsers.add_parser(
    'reset', help='Hard reset on current branch')
gits_reset_subparser.set_defaults(func=gits_reset)
gits_reset_subparser.add_argument(
    '--branch', required=True, help='branch to be used')

gits_push_subparser = subparsers.add_parser(
    'push', help='Push all local changes up to origin')
gits_push_subparser.set_defaults(func=gits_push_func)

gits_add_subparser = subparsers.add_parser('checkout', help='Switch branches')
gits_add_subparser.add_argument('branch_name')
gits_add_subparser.set_defaults(func=checkout)

gits_add_subparser = subparsers.add_parser(
    'unstage', help='Move files from staging area to working directory')
gits_add_subparser.add_argument('file_names',
                                metavar='N',
                                type=str,
                                nargs='+',
                                help='all file names')
gits_add_subparser.set_defaults(func=unstage)

gits_status_subparser = subparsers.add_parser(
    'status', help='Display the state of the working directory')
gits_status_subparser.set_defaults(func=gits_status)

gits_diff_subparser = subparsers.add_parser(
    'diff', help='Shows difference commits, branches, files and more')
gits_diff_subparser.set_defaults(func=gits_diff)

gits_sync_subparser = subparsers.add_parser('sync')
gits_sync_subparser.set_defaults(func=gits_sync)

gits_visualizer_subparser = subparsers.add_parser('visualize')
gits_visualizer_subparser.set_defaults(func=gits_visualizer)

gits_init_subparser = subparsers.add_parser(
    'init', help='Initialize local git repository')
gits_init_subparser.add_argument("--bare", action="store_true",
                                 help="Omit the working directory and initialize an empty git repository")
gits_init_subparser.add_argument(
    "--url", help="url for cloning an already existing repo")
gits_init_subparser.set_defaults(func=gits_init_func)

gits_all_branch_subparser = subparsers.add_parser(
    'all-branch', help='List all local and remote branches')
gits_all_branch_subparser.set_defaults(func=gits_all_branch_func)

gits_remote_branch_subparser = subparsers.add_parser(
    'remote-branch', help='List all remote branches')
gits_remote_branch_subparser.set_defaults(func=gits_remote_branch_func)


gits_commit_test_subparser = subparsers.add_parser(
    'commit_with_test', help='Run tests to ensure success and then commits')
gits_commit_test_subparser.add_argument('-m',
                                        required=True,
                                        help='git commit message')
gits_commit_test_subparser.add_argument('--amend',
                                        action='store_true',
                                        help='amend commit message')
gits_commit_test_subparser.set_defaults(func=gits_commit_func_with_pytest)

gits_stats_subparser = subparsers.add_parser(
    'stats', help='View user statistics')
gits_stats_subparser.set_defaults(func=get_stats)

gits_status_subparser = subparsers.add_parser(
    'commit_tree', help='Print visual representation of commit history')
gits_status_subparser.set_defaults(func=gits_commit_tree)

gits_tag_subparser = subparsers.add_parser(
    'tag', help='Create, list or checkout tags')
gits_tag_subparser.add_argument("tag_name", action="store_true",
                                help="1. Create a new tag 2.List all stored tags 3.View the state of the repo at a tag using checkout")
gits_tag_subparser.set_defaults(func=gits_tag_func)
gits_status_subparser = subparsers.add_parser('describe')
gits_status_subparser.set_defaults(func=gits_describe)


# Nicknames for gits commands, overall nickname subparser
nickname_parser = subparsers.add_parser(
    'nickname', help='Create, remove, update, list nicknames for gits commands')
nickname_parser.set_defaults(func=nickname_default)
nickname_subparsers = nickname_parser.add_subparsers()

# Nickname subparser for add
add_nickname_parser = nickname_subparsers.add_parser(
    'add', help='Add a nickname')
add_nickname_parser.add_argument('-c', required=True, help='Gits Command')
add_nickname_parser.add_argument('-n', required=True, help='Nickname')
add_nickname_parser.set_defaults(func=add_nickname)

remove_nickname_parser = nickname_subparsers.add_parser(
    'remove', help='Remove a nickname')
remove_nickname_parser.add_argument('nickname', help='Nickname to be deleted')
remove_nickname_parser.set_defaults(func=remove_nickname)

update_nickname_parser = nickname_subparsers.add_parser(
    'update', help='Update a nickname')
update_nickname_parser.add_argument(
    '-o', '--old', required=True, help='Old Nickname')
update_nickname_parser.add_argument(
    '-n', '--new', required=True, help='New Nickname')
update_nickname_parser.set_defaults(func=update_nickname)

list_nickname_parser = nickname_subparsers.add_parser(
    'list', help='List a nickname')
list_nickname_parser.add_argument(
    'nicknames', help='Nicknames to be listed', nargs='*')
list_nickname_parser.set_defaults(func=list_nickname)


# Quickly change git command alias's
alias_parser = subparsers.add_parser(
    'alias', help='Create, remove, update, list git alias properties')
alias_parser.set_defaults(func=default_alias)
alias_subparsers = alias_parser.add_subparsers()

add_alias_parser = alias_subparsers.add_parser('add', help='Add a git alias')
add_alias_parser.add_argument('-c', required=True, help='Git Command')
add_alias_parser.add_argument('-a', required=True, help='Alias')
add_alias_parser.set_defaults(func=add_alias)

remove_alias_parser = alias_subparsers.add_parser(
    'remove', help='Remove a git alias')
remove_alias_parser.add_argument('alias', help='Alias to be deleted')
remove_alias_parser.set_defaults(func=remove_alias)

update_alias_parser = alias_subparsers.add_parser(
    'update', help='Update a git alias')
update_alias_parser.add_argument(
    '-o', '--old', required=True, help='Old Alias')
update_alias_parser.add_argument(
    '-n', '--new', required=True, help='New Alias')
update_alias_parser.set_defaults(func=update_alias)

list_alias_parser = alias_subparsers.add_parser(
    'list', help='List git aliases')
list_alias_parser.add_argument(
    'aliases', help='Aliases to be listed', nargs='*')
list_alias_parser.set_defaults(func=list_alias)

valid_commands = [obj for obj in parser._actions[1].choices]
nicknames = read_nicknames_settings()
arguments = sys.argv[1:]

if len(arguments) > 0:
    if arguments[0] in valid_commands:
        pass
    else:
        if arguments[0] in nicknames:
            arguments[0] = nicknames[arguments[0]]

args = parser.parse_args(args=arguments)
args.func(args)
print()
