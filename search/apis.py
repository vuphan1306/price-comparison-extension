from re import sub

from flask_restful import Resource
from flask import request

from stores.utils.amazon import AmazonProducts


class Search(Resource):
    def get(self, *args, **kwargs):
        """
        Searches online stores using the given term.
        Note: If no term is given, defaults to recent.
        ---
        tags:
            - search
        responses:
            200:
                type: array
                description: Search the place sell with best price by product name
                schema:
                    $ref: '#/definitions/Product'
        """
        search_term = request.args.get('search_term')
        amazon_products = AmazonProducts()
        results = amazon_products.parse(search_term=search_term)
        return results, 200
