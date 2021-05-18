from flask import Blueprint
from flask_restful import Api

from search.apis import Search
from core.constants import API_V1

search_urls = Blueprint('search_apis', __name__, url_prefix=API_V1)
api = Api(search_urls)

api.add_resource(Search, '/search/')
