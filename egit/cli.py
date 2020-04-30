import argparse
from .utils import good, bad
import os
import sys


def main():
    # create argument parser object
    custom_usage = '\n' + \
        '\tegit\t: Git status'

    parser = argparse.ArgumentParser(
        description="Easy Git", usage=custom_usage)

    parser.add_argument("-a", type=str, nargs=1,
                        metavar="", default=None, help="Git Add")

    # parse the arguments from standard input
    args = parser.parse_args()

    # print(args.__dict__)

    if args.a is None:
        good('>>> Git Status')
        os.system('git status')

    else:
        print(args.a)


if __name__ == "__main__":
    main()
