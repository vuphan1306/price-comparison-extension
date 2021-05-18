from flask import Blueprint
from flask_restful import Api

from core.apis import User, UserList, UserLogin, LogoutAPI
from core.constants import API_V1

core_urls = Blueprint('core_apis', __name__, url_prefix=API_V1)
api = Api(core_urls)

api.add_resource(User, '/users/<public_id>/')
api.add_resource(UserList, '/users/')
api.add_resource(UserLogin, '/authentication/login/')
api.add_resource(LogoutAPI, '/authentication/logout/')
