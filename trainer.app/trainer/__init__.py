from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from trainer.config import Config

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app, "/api/v1")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

TASK_IMAGE_FOLDER = app.config['TASK_IMAGE_FOLDER']

from trainer import views, models, api_routes
