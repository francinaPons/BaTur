import json
from db import db, secret_key
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


class ActivityModel(db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(), nullable=False)
    path = db.Column(db.String(), nullable=False)
    size = db.Column(db.String(), nullable=False)

    # 0 not admin/ 1 is admin

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def json(self):
        return json.loads(json.dumps(self, default=lambda o: {'id': self.id}))

    def find_by_id(self, id):
        return ActivityModel.query.filter_by(id=id).first().json()
        try:
            return self.query.filter_by(self.id == id).first().json()
        except:
            raise Exception("There was a problem finding the activity")

    def find_all(self):
        activities = ActivityModel.query.all()

        return [i.json() for i in activities]
