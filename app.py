from flask import Flask, render_template, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
from resources.accounts import Accounts, AccountsList
from resources.activity import Activity, ActivityList
from resources.cities import CityList
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from checktype import *
from db import db, secret_key



app = Flask(__name__)
app = Flask(__name__,
            static_folder="./frontend/dist/static",
            template_folder="./frontend/dist")

app.config["CONTENT_UPLOADS"] = '/app/media'
app.config["CONTENT_UPLOADS_THUMBNAILS"] = '/app/media/thumbnails'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = secret_key

CORS(app, resources={r'/*': {'origins': '*'}})

api = Api(app)
migrate = Migrate(app, db, directory='./database/migrations')
manager = Manager(app)
manager.add_command('db', MigrateCommand)
db.init_app(app)


cors = CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:3000"}})

@app.route('/')
def home():
  message = {}
  data = {}

  message['message'] = 'Hello World from Flask!'
  data['status'] = 200
  data['data'] = message

  return jsonify(data)




@app.route('/controlPanel')
def main_window():
    return render_template("index.html")


api.add_resource(Accounts, '/account/<string:username>', '/account')
api.add_resource(Activity, '/activity/<int:id>')
api.add_resource(ActivityList, '/activities')
api.add_resource(AccountsList, '/accounts')
api.add_resource(CityList, '/cities/<string:lang>')


if __name__ == '__main__':
  app.run(debug=True)


# if __name__ == '__main__':
#     manager.run()
#     app.run(port=80, debug=True)
