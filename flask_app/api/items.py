from flask_restful import Resource, abort, reqparse, fields, marshal

from models.items import db, Item


item_api_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'price': fields.String,
}

parser = reqparse.RequestParser()
parser.add_argument(
    'name', type=unicode, required=True, location='form', help='Name required')
parser.add_argument('description', required=True, type=unicode, location='form')
parser.add_argument(
    'price', type=int, required=True, location='form', help='Price required')


class ItemsAPI(Resource):
    """Items API"""

    def get(self, id=None):
        if id:
            item = Item.query.get_or_404(id, description="ITEM NOT AVAILABLE")
            return marshal(item, item_api_fields, envelope='item_data')

        items = Item.query.all()
        return marshal(items, item_api_fields, envelope="all_items")

    def post(self):
        post_data = parser.parse_args()
        try:
            name = post_data.get('name')
            description = post_data.get('description')
            price = post_data.get('price')
            if not (name or price or description):
                abort(412, description='NAME/PRICE/Description DATA MISSIG')

            item = Item()
            item.name = name
            item.description = description
            item.price = price
            db.session.add(item)
            db.session.commit()

        except Exception as e:
            return str(e)

        return marshal(item, item_api_fields, envelope='item_data'), 201

    def delete(self, id):
        item = Item.query.get_or_404(id, description='ITEM NOT Availbele')
        db.session.delete(item)
        item.remove_thumbnail
        db.session.commit()

        return {'status': 'deleted'}, 201
