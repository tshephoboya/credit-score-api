from flask_restful import Resource, reqparse
from flask import request
from models.client import ClientModel

class Client(Resource):
    def get(self, name):
        client = ClientModel.find_by_name(name)
        return client.json()

    def post(self, name):
        if ClientModel.find_by_name(name):
            return {'message':'user already exists'}
        ClientModel.create_client(name)
        return {'message':f'user with name {name} has been created'}

    def delete(self, name):
        client = ClientModel.find_by_name(name)
        if client:
            client.delete_by_name()
        return {'message': f'Client with name <{name}> has been deleted'}

    def put(self, name):
        client = ClientModel.find_by_name(name)
        parser = reqparse.RequestParser()
        parser.add_argument('credit_score', type=int, help='This is required')
        data = parser.parse_args()
        if client:
            client.credit_score = data['credit_score']
        else:
            client = ClientModel(name, data['credit_score'])

        client.save_to_db()
        return client.json()


class ClientList(Resource):
    def get(self):
        return {'Clients': list(map(lambda x: x.json(), ClientModel.view_all() ) )}