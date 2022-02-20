from flask_restful import Resource, Api, reqparse

from models.batur import BaturModel


class Batur(Resource):
    def get(self, user_id):
        try:
            baturs = BaturModel.find_by_user_id(self, user_id)
        except Exception as e:
            print(e)
            return {'message': "Preguntas no encontradas"}, 400
        return {'baturs': baturs}, 200

    def post(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define al input parameters need and its type
        parser.add_argument('id', type=int, required=True, help="Se requiere especificar el id del usuario")
        parser.add_argument('user_id', type=int, required=True, help="Se requiere especificar el id del usuario")
        parser.add_argument('charge', type=int, required=True, help="Se requiere especificar si se cargan gastos")
        parser.add_argument('location', type=str, required=True, help="Se requiere especificar la localización")
        parser.add_argument('description', type=str, required=True, help="Se requiere especificar una descripción")
        parser.add_argument('availability', type=str, required=True, help="Se requiere especificar la disponibilidad")
        parser.add_argument('subcategory', type=str, required=True, help="Se requiere especificar la subcategoría")


        data = parser.parse_args()

        if data['user_id'] == '' or "":
            return {'message': "Se requiere especificar el id del usuario"}, 400
        if data['charge'] == '' or "":
            return {'message': "Se requiere especificar si se cargan gastos"}, 400
        if data['location'] == '' or "":
            return {'message': "Se requiere especificar la localización"}, 400
        if data['description'] == '' or "":
            return {'message': "Se requiere especificar una descripció"}, 400
        if data['availability'] == '' or "":
            return {'message': "Se requiere especificar la disponibilidad"}, 400
        if data['subcategory'] == '' or "":
            return {'message': "Se requiere especificar la subcategoría"}, 400

        batur = BaturModel.save_to_db(self)
        return {'batur': batur.json()}, 200



