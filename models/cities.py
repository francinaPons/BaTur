import json

from db import db
class CitiesModel(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def json(self):
        return json.loads(json.dumps(self, default=lambda o: {'id': self.id, 'name': self.name}))

    def find_by_name(name):
        try:
            return CitiesModel.query.filter_by(name=name).first()
        except:
             raise Exception("There was a problem finding the name")
