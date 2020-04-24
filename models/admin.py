from db import db


class AdminModel(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40))
    password = db.Column(db.String(40))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {'username': self.username, 'password': self.password}

    def create(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return self.json()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(username=name).first()
