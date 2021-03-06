from flask import request
from flask_restful import Resource, reqparse
import json
from trainer import failed_deque, trainer_settings, settings_parser
from trainer.api_folder.api_utils import upload_images, get_random_list, add_to_deque
from trainer.marshmallow_schemas import TaskSchema


class TaskCreation(Resource):
    task_schema_list = TaskSchema(many=True)

    def get(self) -> list:
        list_lim = 0 if 'len_of_list' not in trainer_settings else int(trainer_settings['len_of_list'])
        return self.task_schema_list.dump(get_random_list(int(list_lim))).data

    def post(self) -> tuple:
        return upload_images(request.files), 200


class FailedDeque(Resource):
    task_schema = TaskSchema()

    def get(self) -> dict or None:
        if len(failed_deque) > 0:
            return self.task_schema.dump(failed_deque.popleft()).data
        else:
            return None

    def post(self) -> tuple:
        print(request.data)
        return add_to_deque(json.loads(request.data)), 200


class TrainerSettings(Resource):
    def get(self) -> tuple:
        return trainer_settings, 200

    def post(self) -> dict:
        args = settings_parser.parse_args()
        for k, v in args.items():
            trainer_settings[k] = v
        return trainer_settings
