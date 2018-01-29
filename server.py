from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
import boto3
import json
import decimal

app = Flask(__name__)
api = Api(app)


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


dynamodb = boto3.resource('dynamodb', region_name='us-east-2', endpoint_url="http://localhost:8000")

table_restaurant = dynamodb.Table('Restaurant_Meng')
table_menu = dynamodb.Table('Menu_Meng')
table_item = dynamodb.Table('Item_Meng')

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('address')


class Restaurant(Resource):
    def get(self, restaurant_id):
        response = table_restaurant.get_item(
            Key={
                'id': int(restaurant_id),
            }
        )
        item = response['Item']
        return json.dumps(item, cls=DecimalEncoder)

    def delete(self, restaurant_id):
        table_restaurant.delete_item(
            Key={
                'id': int(restaurant_id)
            }
        )
        return '', 204

    def post(self, restaurant_id):
        args = parser.parse_args()
        table_restaurant.put_item(
            Item={
                'id': int(restaurant_id),
                'info': {'name': args['name'], 'address': args['address']},
            }
        )

    def put(self, restaurant_id):
        args = parser.parse_args()
        table_restaurant.update_item(
            Key={
                'id': int(restaurant_id)
            },
            UpdateExpression='SET info = :val1',
            ExpressionAttributeValues={
                ':val1': {'name': args['name'], 'address': args['address']}
            }
        )


api.add_resource(Restaurant, '/restaurant/<restaurant_id>')

if __name__ == '__main__':
    app.run(debug=True)
