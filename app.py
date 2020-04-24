from flask import Flask
from flask_restful import Api
from db import db

from resources.client import Client, ClientList
from resources.admin import Admin

app = Flask(__name__)
db_url = 'sqlite:///data.db'

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIDICATIONS'] = False
app.secret_key = '064u'
api = Api(app)


@app.before_first_request
def create_all():
    db.create_all()


api.add_resource(Client, '/client/<string:name>')
api.add_resource(Admin, '/admin/<string:name>')
api.add_resource(ClientList, '/clients')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=4040)
