#!/bin/bash
set -x

virtualenv -p python3 ./trainer.app/.venv
source ./trainer.app/.venv/bin/activate

pip3 install -r ./trainer.app/requirements.txt


