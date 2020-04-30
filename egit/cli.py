import argparse
from .utils import good, bad
import os
import sys


def git_status():
    good('>>> Git Status')
    os.system('git status')


def git_add():
    good('>>> Git Add -A')
    os.system('git add -A')

def git_commit(msg):
    good('>>> Git Push')
    os.system('git commit -m {}'.format(msg))

def git_push():
    good('>>> Git Push')
    os.system('git push')


def main():
    # create argument parser object
    custom_usage = '\n' + \
        '  egit  \t\t: Git status\n' + \
        '  egit comment\t\t: Git add, commit (with "comment") and push\n' + \
        '  egit -a\t\t: Git Add -A\n' + \
        ''

    parser = argparse.ArgumentParser(
        description="Easy Git", usage=custom_usage)

    # parser.add_argument("-a", type=str, metavar="", default=None, help="Git Add")

    parser.add_argument('-a', action='store_true', help="Git Add -A")

    parser.add_argument('comment', nargs='?', default=None)
    # parse the arguments from standard input
    args = parser.parse_args()

    print(args.__dict__)

    if args.comment is not None:
        bad('>>> Git Push "{}"'.format(args.comment))
        git_add()
        git_commit(args.comment)
        git_push()

    # if args.a:
    #     git_add()
    #     git_status()

    # else:
    #     git_status()


if __name__ == "__main__":
    main()
