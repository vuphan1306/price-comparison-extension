from flask import request
from flask_restful import Resource, marshal_with

from core.schema import UserSchema, AuthSchema
from core.utils import save_new_user, get_all_users, get_a_user, Auth

user_schema = UserSchema()
users_schema = UserSchema(many=True)
auth_schema = AuthSchema()


class UserList(Resource):
    @marshal_with(users_schema, envelope='data')
    def get(self):
        """
        List all registered users
        ---
        tags:
            - users
        responses:
            200:
                description: A list of users
                schema:
                    $ref: '#/definitions/User'
        """
        return get_all_users()

    def post(self):
        """
        Creates a new User
        ---
        tags:
            - users
        parameters:
            - in: body
              name: body
              schema:
                $ref: '#/definitions/User'
        responses:
            201:
                description: The user has been created
                schema:
                    $ref: '#/definitions/User'
        """
        data = request.json
        return save_new_user(data=data)


class User(Resource):
    @marshal_with(user_schema)
    def get(self, public_id):
        """
        Get a user given its identifier
        ---
        tags:
            - users
        responses:
            200:
                description: User detail
                schema:
                    $ref: '#/definitions/User'
        """
        user = get_a_user(public_id)
        if not user:
            return "User not found.", 404
        else:
            return user


class UserLogin(Resource):
    """
    User Login Resource
    """
    def post(self):
        """
        Login
        ---
        tags:
            - authentication
        parameters:
            - in: body
              name: body
              schema:
                $ref: '#/definitions/Auth'
        responses:
            201:
                description: Login user by username and password
                schema:
                    $ref: '#/definitions/Auth'
        """
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)


class LogoutAPI(Resource):
    """
    Logout Resource
    """
    def post(self):
        """
        Logout
        ---
        tags:
            - authentication
        parameters:
            - in: body
              name: body
              schema:
                $ref: '#/definitions/Auth'
        responses:
            201:
                description: Logout
                schema:
                    $ref: '#/definitions/Auth'
        """
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)
