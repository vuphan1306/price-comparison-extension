from flask_marshmallow import Schema
from marshmallow import fields


class UserSchema(Schema):
    class Meta:
        fields = ["email", "username", "password", "public_id"]

    email = fields.String()
    username = fields.String()
    password = fields.String()
    public_id = fields.String()


class AuthSchema(Schema):
    class Meta:
        fields = ["email", "password"]

    email = fields.String()
    password = fields.String()
