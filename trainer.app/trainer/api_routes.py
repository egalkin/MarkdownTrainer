from trainer import api
from trainer.api_folder.admin_api import TaskCreation

api.add_resource(TaskCreation, '/tasks')
