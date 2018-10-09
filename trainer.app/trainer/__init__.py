from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api, reqparse
from flask_sqlalchemy import SQLAlchemy

from trainer.config import Config
from collections import deque

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app, "/api/v1")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
failed_deque = deque()

trainer_settings = dict()
settings_args = ['deque_step', 'num_of_steps', 'len_of_list']
settings_parser = reqparse.RequestParser()
for arg in settings_args:
    settings_parser.add_argument(arg)

TASK_IMAGE_PARENT_FOLDER = app.config['TASK_IMAGE_PARENT_FOLDER']
TASK_RELATIVE_PATH = app.config['TASK_RELATIVE_PATH']

from trainer import views, models, api_routes
