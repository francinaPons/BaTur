import json
from db import db
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


class BaturModel(db.Model):
    __tablename__ = 'baturs'

    id = db.Column(db.Integer,primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    charge = db.Column(db.Integer(), nullable=False)
    location = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    availability = db.Column(db.String(), nullable=False)
    subcategory = db.Column(db.String(), nullable=False)

    def __init__(self, id, user_id, charge, location, description, availability, subcategory):
        self.id = id
        self.user_id = user_id
        self.charge = charge
        self.location = location
        self.description = description
        self.availability = availability
        self.subcategory = subcategory

    def json(self):
        return json.loads(json.dumps(self, default=lambda o: {
            'id': self.id,
            'user_id': self.user_id,
            'charge': self.charge,
            'location': self.location,
            'description': self.description,
            'availability': self.availability,
            'subcateogry' : self.subcategory
        }))
        # return json.loads(json.dumps(self, default=lambda o: {'id': self.id}))

    def save_to_db(self):
        try:# saving data
            db.session.add(self)
            db.session.commit()
            return {"message": "Ok"}, 200
        except:
            raise Exception("There was a problem  saving on database")

    def find_by_user_id(self, user_id):
        res = [i.json() for i in BaturModel.query.filter_by(user_id=user_id).all()]
        return res





