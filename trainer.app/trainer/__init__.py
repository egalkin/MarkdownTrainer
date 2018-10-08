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

failed_args = ['false_picture_url', 'true_picture_url', 'id']
failed_parser = reqparse.RequestParser()
for arg in failed_args:
    failed_parser.add_argument(arg)

trainer_settings = dict()
settings_args = ['deque_step']
settings_parser = reqparse.RequestParser()
for arg in settings_args:
    settings_args.append(arg)

TASK_IMAGE_FOLDER = app.config['TASK_IMAGE_FOLDER']

from trainer import views, models, api_routes
