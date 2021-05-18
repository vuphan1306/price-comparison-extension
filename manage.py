import os
import unittest

from dotenv import load_dotenv
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flasgger import Swagger, APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

from app.settings import create_app, db
from core.urls import core_urls, api
from core.schema import UserSchema, AuthSchema
from search.urls import search_urls
from search.schema import ProductSchema

# Load environment file
load_dotenv('.env')

# Create an APISpec
spec = APISpec(
    title='Price Comparison Extension',
    version='0.0.1',
    openapi_version='2.0',
    plugins=[
        FlaskPlugin(),
        MarshmallowPlugin(),
    ],
)

app = create_app(os.getenv('FLASK_APP_ENV') or 'dev')

# Import module URLs
app.register_blueprint(core_urls)
app.register_blueprint(search_urls)

# # Config swagger
# template = {
#     "swagger": "2.0",
#     "info": {
#         "title": "Flask APP",
#         "description": "Practice using flask for building APIs",
#         "contact": {
#             "responsibleOrganization": "ME",
#             "responsibleDeveloper": "Me",
#             "email": "me@me.com",
#             "url": "www.me.com",
#         },
#         "termsOfService": "http://me.com/terms",
#         "version": "0.0.1"
#     },
#     "basePath": "/api/v1",  # base bash for blueprint registration
#     "schemes": [
#         "http",
#         "https"
#     ],
#     "operationId": "getmyData"
# }

template = spec.to_flasgger(
    app,
    definitions=[UserSchema, AuthSchema, ProductSchema]
)

swagger = Swagger(app, template=template)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


# Generate models bellow for migrations
from core.models import User, BlacklistToken # noqa


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('.', pattern='test_*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
