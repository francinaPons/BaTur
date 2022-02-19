import json
from db import db
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


class InitialQuestionsModel(db.Model):
    __tablename__ = 'questions'

    user_id = db.Column(db.Integer,primary_key=True, unique=True, nullable=False)
    host = db.Column(db.Boolean(), nullable=False)
    charge = db.Column(db.Integer(), nullable=False)
    location = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    availability = db.Column(db.Integer(), nullable=False)



    def __init__(self, user_id, host, charge, location, description, availability):
        self.user_id = user_id
        self.host = host
        self.charge = charge
        self.location = location
        self.description = description
        self.availability = availability

    # def json(self):
    #     return json.loads(json.dumps(self, default=lambda o: {'id': self.id}))

    def save_to_db(self):
        try:# saving data
            db.session.add(self)
            db.session.commit()
            return {"message": "Ok"}, 200
        except:
            raise Exception("There was a problem  saving on database")

    def find_by_user_id(self, user_id):
        return InitialQuestionsModel.query.filter_by(user_id=user_id).first().json()

