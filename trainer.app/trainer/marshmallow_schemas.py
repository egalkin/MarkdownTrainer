from marshmallow import post_load
from trainer import ma
from trainer.models import Task


class TaskSchema(ma.ModelSchema):
    class Meta:
        model = Task

        @post_load
        def create_task(self, data):
            return Task(**data)
