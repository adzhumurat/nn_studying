#!/bin/bash -e

case "$1" in
  pipenv)
    pipenv install -r requirements.txt --deploy
    ;;
  jupyter)
    pipenv run jupyter notebook --ip 0.0.0.0 --port 8888 --no-browser --allow-root
    ;;
  *)
    exec "$@"
esac