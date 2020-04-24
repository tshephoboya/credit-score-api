from db import db
from random import randrange


class ClientModel(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    credit_score = db.Column(db.Integer)

    def __init__(self, name, credit_score):
        self.name = name
        self.credit_score = credit_score

    def json(self):
        return {'name': self.name, 'credit_score': self.credit_score}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def __repr__(self):
        return self.json()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def create_client(cls, name):
        credit_score = randrange(1,999)
        new_client = cls(name, credit_score)
        new_client.save_to_db()

    @classmethod
    def view_all(cls):
        return cls.query.all()

    def delete_by_name(self):
        db.session.delete(self)
        db.session.commit()
