# egit

Python module for handling git easy.

**Only Python 3**

**Module can be accessed using both `eg` and `egit` commands**

``` bash
$ eg -h
usage: 
  egit                  : Git status
  egit comment          : Git add, commit (with "comment") and push
  egit -a               : Git Add -A
  egit -c comment       : Git Commit -m comment
  egit -p               : Git Push
  egit -u               : Git Pull

Easy Git | 2020 Sameera Sandaruwan

positional arguments:
  comment

optional arguments:
  -h, --help  show this help message and exit
  -a          Git Add -A
  -c          Git Commit -m comment
  -p          Git Push
  -u          Git Pull
```

## Install

1. Clone this repo. ( `git clone https://github.com/basameera/egit.git` )
1. `cd egit` 
1. `pip install .` 

**Git fetch**

``` 
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
```

1
