import argparse
from .utils import good, bad
import os
import subprocess


def sp_result(cmd):
    cmd_list = cmd.split(' ')
    res = subprocess.run(cmd_list, stdout=subprocess.PIPE)
    return res.stdout.decode('utf-8').replace('\n', '')


def git_fetch():
    # fetch is slow. so do it less
    os.system('git fetch -q')


def git_status():
    good('>> Git Status')
    os.system('git status')


def git_add():
    good('>> Git Add -A')
    os.system('git add -A')


def git_commit(msg):
    good('>> Git Commit')
    os.system('git commit -m "{}"'.format(msg))


def git_push():
    good('>> Git Push')
    os.system('git push')


def git_pull():
    good('>> Git Pull')
    os.system('git pull')


def git_switch_branch(msg):
    good('>> Git Change branch')
    os.system('git checkout "{}"'.format(msg))


def main():
    # create argument parser object
    custom_usage = '\n' + \
        '  egit  \t\t: Git status\n' + \
        '  egit comment\t\t: Git add, commit (with "comment") and push\n' + \
        '  egit -a\t\t: Git Add -A\n' + \
        '  egit -c comment\t: Git Commit -m comment\n' + \
        '  egit -p\t\t: Git Push\n' + \
        '  egit -u\t\t: Git Pull\n' + \
        '  egit -b <branch name>\t: Change branch\n'

    parser = argparse.ArgumentParser(
        description="Easy Git | 2020 Sameera Sandaruwan", usage=custom_usage)

    parser.add_argument('-a', action='store_true', help="Git Add -A")
    parser.add_argument('-c', action='store_true',
                        help="Git Commit -m comment")
    parser.add_argument('-p', action='store_true', help="Git Push")
    parser.add_argument('-u', action='store_true', help="Git Pull")
    parser.add_argument('-b', type=str, metavar="",
                        default=None, help="Change branch")

    parser.add_argument('comment', nargs='?', default=None)
    # parse the arguments from standard input
    args = parser.parse_args()

    # git fetch
    git_fetch()

    UPSTREAM = r'@{u}'
    LOCAL = sp_result('git rev-parse @')
    REMOTE = sp_result('git rev-parse {}'.format(UPSTREAM))
    BASE = sp_result('git merge-base @ {}'.format((UPSTREAM)))

    # Up-to-date
    if LOCAL == REMOTE:

        # git add, commit, push
        if args.comment is not None and args.a is False and args.c is False and args.p is False and args.u is False:
            bad('>>> Git All "{}"'.format(args.comment))
            git_add()
            git_commit(args.comment)
            git_push()
            git_status()

        # git add
        elif args.a:
            bad('>>> Git Add -A')
            git_add()
            git_status()

        # git commit
        elif args.comment is not None and args.c:
            bad('>>> Git Commit -m "{}"'.format(args.comment))
            git_commit(args.comment)
            # git_status()

        # git push
        elif args.p:
            git_push()
            git_status()

        # git pull
        elif args.u:
            git_pull()
            # git_status()

        # git checkout <branch>
        elif args.b is not None:
            git_switch_branch(args.b)

        else:
            git_status()

    elif LOCAL == BASE:
        bad("*** Need to pull ***")

        # git pull
        if args.u:
            git_pull()


if __name__ == "__main__":
    main()
