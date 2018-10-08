from flask import request
from flask_restful import Resource

from trainer.api_folder.api_utils import upload_images, get_random_list
from trainer.marshmallow_schemas import TaskSchema


class TaskCreation(Resource):
    task_schema_list = TaskSchema(many=True)

    def get(self):
        list_lim = request.args['lim']
        return self.task_schema_list.dump(get_random_list(int(list_lim))).data

    def post(self):
        return upload_images(request.files), 200

