import json
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from db import db, secret_key
from flask_httpauth import HTTPBasicAuth
from flask import g, current_app

auth = HTTPBasicAuth()


class WeatherModel(db.Model):
    __tablename__ = 'weather'

    username = db.Column(db.String(30), primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    # 0 not admin/ 1 is admin
    is_admin = db.Column(db.Integer, nullable=False)

    def __init__(self, username, is_admin=0):
        self.username = username
        self.is_admin = is_admin

    def json(self):
        return json.loads(json.dumps(self, default=lambda o: {'username': self.username, 'is_admin': self.is_admin}))