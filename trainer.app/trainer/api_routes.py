from trainer import api
from trainer.api_folder.admin_api import TaskCreation, FailedDeque, TrainerSettings

api.add_resource(TaskCreation, '/tasks')
api.add_resource(FailedDeque, '/failed')
api.add_resource(TrainerSettings, '/settings')
