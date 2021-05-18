from flask_marshmallow import Schema
from marshmallow import fields


class ProductSchema(Schema):
    class Meta:
        fields = ["title", "price", "image", "source"]

    title = fields.String()
    price = fields.String()
    image = fields.String()
    source = fields.String()
