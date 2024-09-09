import argparse
from .utils import good, bad
from .vsr import VERSION
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


def git_cache_cred():
    good('>> Git cache credential')
    os.system("git config credential.helper 'cache --timeout=7200'")


def git_pull():
    good('>> Git Pull')
    os.system('git pull')


def git_switch_branch(msg):
    good('>> Git Change branch')
    os.system('git checkout "{}"'.format(msg))

def git_setup_cred(username, email, token):
    bad('\n>> Before')
    os.system('cat .git/config')

    info = 'git config user.name "<username>"\n' + \
    'git config user.email <email address>\n' + \
    'git remote rm origin\n' + \
    'git remote add origin https://<username>:<access_token>@<git remote link>\n' + \
    'git push --set-upstream origin <branch name>'

    # get branch name
    branch_name = sp_result("git rev-parse --abbrev-ref HEAD")
    
    # get remote link
    remote_link = sp_result("git remote get-url origin").split('://')[1]

    print()
    os.system('git config user.name "{}"'.format(username))
    os.system('git config user.email {}'.format(email))
    os.system('git remote rm origin')
    os.system('git remote add origin https://{}:{}@{}'.format(username, token, remote_link))
    os.system('git push --set-upstream origin {}'.format(branch_name))

    good('\n>> After')
    os.system('cat .git/config')

    

def main():
    # create argument parser object
    custom_usage = '\n' + \
        '  egit  \t\t: Git status\n' + \
        '  egit comment\t\t: Git add, commit (with "comment") and push\n' + \
        '  egit -a\t\t: Git Add -A\n' + \
        '  egit -c comment\t: Git Commit -m comment\n' + \
        '  egit -p\t\t: Git Push\n' + \
        '  egit -u\t\t: Git Pull\n' + \
        '  egit -b <branch name>\t: Change branch\n' + \
        '  egit -z <username> <email> <github token>\t: Setup Credentials\n'
    
    custom_usage = None

    parser = argparse.ArgumentParser(
        description="Easy Git - {} | 2024 Sameera Sandaruwan".format(VERSION), usage=custom_usage)

    parser.add_argument('-a', action='store_true', help="Git Add -A")
    parser.add_argument('-c', action='store_true',
                        help="Git Commit -m comment")
    parser.add_argument('-p', action='store_true', help="Git Push")
    parser.add_argument('-u', action='store_true', help="Git Pull")
    parser.add_argument('-b', type=str, metavar="",
                        default=None, help="Change branch")
    parser.add_argument('-s', action='store_true',
                        help="git-credential-cache for 3 hours")
    # https://git-scm.com/docs/git-credential-cache
    parser.add_argument('-z', action='store_true', help="Setup Credentials | eg -z [username] [email] [token]")

    parser.add_argument('comment', nargs='?', default=None, help="comment or username for -z")
    parser.add_argument('email', nargs='?', default=None, help="email for -z")
    parser.add_argument('token', nargs='?', default=None, help="token for -z")
    # parse the arguments from standard input
    args = parser.parse_args()

    # git-credential-cache
    if args.s:
        git_cache_cred()

    # git fetch
    git_fetch()

    UPSTREAM = r'@{u}'
    LOCAL = sp_result('git rev-parse @')
    REMOTE = sp_result('git rev-parse {}'.format(UPSTREAM))
    BASE = sp_result('git merge-base @ {}'.format((UPSTREAM)))

    # Up-to-date
    if LOCAL == REMOTE:

        # git add, commit, push
        if args.comment is not None and args.a is False and args.c is False and args.p is False and args.u is False and args.z is False:
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

        # git setup credentials
        elif args.z:
            # git_push()
            # git_status()
            if args.comment is not None and args.email is not None and args.token is not None:
                z_username = args.comment
                z_email = args.email
                z_token = args.token
                git_setup_cred(z_username, z_email, z_token)
            else:
                bad("> Not enough Arguments. Need <username> <email> <token>")

        else:
            git_status()

    elif LOCAL == BASE:
        bad("*** Need to pull ***")

        # git pull
        if args.u:
            git_pull()

    elif REMOTE == BASE:
        bad("*** Need to push ***")

        # git push
        if args.p:
            git_push()
            git_status()


if __name__ == "__main__":
    main()
