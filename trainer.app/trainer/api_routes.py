from trainer import api
from trainer.api_folder.admin_api import Admin

api.add_resource(Admin, '/admin')