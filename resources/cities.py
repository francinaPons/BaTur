from flask_restful import Resource, Api, reqparse
from models.cities import CitiesModel


class City(Resource):
    def get(self, name):
        try:
            account = CitiesModel.find_by_name(name).json()
        except Exception as e:
            return {'message': "City not found"}, 400
        return {'account': account}, 200
