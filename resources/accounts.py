from flask_restful import Resource, Api, reqparse
from sqlalchemy import types

from models.accounts import AccountsModel
from models.accounts import auth


class AccountId(Resource):
    def get(self, id):
        try:
            account = AccountsModel.find_by_id(id).jsonAllAccount()
        except Exception as e:
            return {'message': "Usuario no econtrado"}, 400
        return {'account': account}, 200

class Accounts(Resource):
    def get(self, username):
        try:
            account = AccountsModel.find_by_username(username).json()
        except Exception as e:
            return {'message': "Usuari no  trobat"}, 400
        return {'account': account}, 200


    def post(self, username):

        if username:
            parser = reqparse.RequestParser()  # create parameters parser from request

            parser.add_argument('name', type=str)
            parser.add_argument('description', type=str)
            parser.add_argument('city', type=str)

            dades = parser.parse_args()
            try:
                if AccountsModel.find_by_username(username):
                    account = AccountsModel.find_by_username(username)
                    account.updateName(dades['name'])
                    account.updateDescription(dades['description'])
                    account.updateCity(dades['city'])
                    account.save_to_db()

            except:
                return {'message': "El usuario no se ha modificado debido a un error"}, 400
            return {'message': "Cambio realizado con éxito"}, 200

        else:
            try:
                parser = reqparse.RequestParser()  # create parameters parser from request

                # define al input parameters need and its type
                parser.add_argument('username', type=str, required=True, help="This field cannot be left blanck")
                parser.add_argument('password', type=str)

                dades = parser.parse_args()
                if AccountsModel.find_by_username(dades['username']):
                    return {'message': "Usari amb ['username': {} ] ja existeix".format(dades['username'])}, 409
                else:
                    new_account = AccountsModel(username=dades['username'])
                    new_account.hash_password(dades['password'])
                    new_account.save_to_db()
                    return {'account': new_account.json()}, 200

            except:
                return {'message': "Ha hagut un problema amb la petició"}, 400

            return {'message': "Petició processada correctament"}, 200

    # @auth.login_required(role='admin')
    # def post(self):
    #     try:
    #         parser = reqparse.RequestParser()  # create parameters parser from request
    #
    #         # define al input parameters need and its type
    #         parser.add_argument('username', type=str, required=True, help="This field cannot be left blanck")
    #         parser.add_argument('password', type=str)
    #
    #
    #
    #         dades = parser.parse_args()
    #         if AccountsModel.find_by_username(dades['username']):
    #             return {'message': "Usari amb ['username': {} ] ja existeix".format(dades['username'])}, 409
    #         else:
    #             new_account = AccountsModel(username=dades['username'])
    #             new_account.hash_password(dades['password'])
    #             new_account.save_to_db()
    #             return {'account': new_account.json()}, 200
    #
    #     except:
    #         return {'message': "Ha hagut un problema amb la petició"}, 400
    #
    #     return {'message': "Petició processada correctament"}, 200

    @auth.login_required(role='admin')
    def delete(self, username):
        try:
            AccountsModel.delete_by_username(username)
        except:
            return {'message': "Usari amb  ['username': {} ] no trobat".format(username)}, 400
        return {'message': "Usari amb ['username': {} ] esborrat correctament".format(username)}, 200

    def put(self, username):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define al input parameters need and its type
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('city', type=str)

        dades = parser.parse_args()
        try:
            if AccountsModel.find_by_username(username):
                account = AccountsModel.find_by_username(username)
                account.updateName(dades['name'])
                account.updateDescription(dades['description'])
                account.updateCity(dades['city'])
                account.save_to_db()

        except:
            return {'message': "El usuario no se ha modificado debido a un error"}, 400
        return {'message': "Cambio realizado con éxito"}, 200


class AccountsList(Resource):
    def get(self):
        acc = AccountsModel.retrieveAllAccounts(self)  # TO TEST

        container_accounts = []
        for a in acc:
            container_accounts.append(a.jsonAllAccount())

        return {'accounts': container_accounts}, 200
