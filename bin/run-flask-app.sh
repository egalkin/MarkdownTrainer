#!/bin/bash
set -x

virtualenv -p python3 ./trainer.app/.venv
source ./trainer.app/.venv/bin/activate

pip3 install -r ./trainer.app/requirements.txt
#!/bin/bash

cd trainer.app

source .venv/bin/activate
source ../.env.local
pip3 install -r requirements.txt

export FLASK_APP=runserver.py
flask run --port=5000

