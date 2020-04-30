import os
import subprocess


def sp_result(cmd):
    cmd_list = cmd.split(' ')
    res = subprocess.run(cmd_list, stdout=subprocess.PIPE)
    return res.stdout.decode('utf-8').replace('\n', '')


def git_fetch():
    # fetch is slow. so do it less
    os.system('git fetch -q')


if __name__ == "__main__":

    '''
    UPSTREAM=${1:-'@{u}'}
    LOCAL=$(git rev-parse @)
    REMOTE=$(git rev-parse "$UPSTREAM")
    BASE=$(git merge-base @ "$UPSTREAM")

    echo LOCAL : $LOCAL
    echo REMOTE: $REMOTE
    echo BASE : $BASE

    if [ $LOCAL = $REMOTE ]; then
        echo "Up-to-date"
    elif [ $LOCAL = $BASE ]; then
        echo "Need to pull"
    elif [ $REMOTE = $BASE ]; then
        echo "Need to push"
    else
        echo "Diverged"
    fi
    '''

    # git fetch

    git_fetch()

    UPSTREAM = r'@{u}'
    LOCAL = sp_result('git rev-parse @')
    REMOTE = sp_result('git rev-parse {}'.format(UPSTREAM))
    BASE = sp_result('git merge-base @ {}'.format((UPSTREAM)))

    if LOCAL == REMOTE:
        print("Up-to-date")
    elif LOCAL == BASE:
        print("Need to pull")
    elif REMOTE == BASE:
        print("Need to push")
