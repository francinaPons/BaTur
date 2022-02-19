from flask_restful import Resource, Api, reqparse

from models.activity import ActivityModel


class Activity(Resource):
    def get(self, id):
        try:
            activity = ActivityModel.find_by_id(self, id)
        except Exception as e:
            print(e)
            return {'message': "Activitat no  trobada"}, 400
        return {'activity': activity}, 200


class ActivityList(Resource):

    def get(self):
        try:
            activity_list = ActivityModel.find_all(self)
            print(activity_list)
        except Exception as e:
            print(e)
            return {'message': "La lista de actividades no se ha encontrado"}, 400
        return {'activity_list': activity_list}, 200
