import argparse
from .utils import good, bad
import os
import sys


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


def main():
    # create argument parser object
    custom_usage = '\n' + \
        '  egit  \t\t: Git status\n' + \
        '  egit comment\t\t: Git add, commit (with "comment") and push\n' + \
        '  egit -a\t\t: Git Add -A\n' + \
        '  egit -c comment\t: Git Commit -m comment\n' + \
        '  egit -p\t\t: Git Push\n'

    parser = argparse.ArgumentParser(
        description="Easy Git", usage=custom_usage)

    # parser.add_argument("-a", type=str, metavar="", default=None, help="Git Add")

    parser.add_argument('-a', action='store_true', help="Git Add -A")
    parser.add_argument('-c', action='store_true',
                        help="Git Commit -m comment")
    parser.add_argument('-p', action='store_true', help="Git Push")

    parser.add_argument('comment', nargs='?', default=None)
    # parse the arguments from standard input
    args = parser.parse_args()

    # print(args.__dict__)

    # git add, commit, push
    if args.comment is not None and args.a is False and args.c is False and args.p is False:
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
        bad('>>> Git Push')
        git_push()
        git_status()

    else:
        git_status()


if __name__ == "__main__":
    main()
