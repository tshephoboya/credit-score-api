from flask_restful import Resource, reqparse
from models.admin import AdminModel

class Admin(Resource):
    def post(self, name):
        if AdminModel.find_by_name(name):
            return {'message': f'User with name <{name}> already exists'}
        parser = reqparse.RequestParser()
        parser.add_argument('password', type=str, required=True, help='Password is required')
        data = parser.parse_args()
        new_admin = AdminModel(name, data['password'])
        new_admin.create()
        return new_admin.json()

    def get(self, name):
        admin = AdminModel.find_by_name(name)
        if admin:
            return admin.json()


    @staticmethod
    def return_message(message):
        return {'message': message}