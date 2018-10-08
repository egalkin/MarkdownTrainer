#!/bin/bash
set -x

cd trainer.app

source .venv/bin/activate
source ../.env.local
export FLASK_APP=runserver.py

flask db init
if [ -d /migrations ]; then
  rm -rf /migrations
fi
flask db migrate
flask db upgrade






