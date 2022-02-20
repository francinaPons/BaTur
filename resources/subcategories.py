# from flask_restful import Resource, Api, reqparse
# # from models.POIS import POISModel
# import requests
#
# API_KEY = 'SAyx0slRJe'
# GUIPUZKOA_ID = 1010
# COUNTRY_ID = 63
# LANG = "es"
#
#
# class POISSubcategoryList(Resource):
#
#     def get(self, subcategory_id):
#         url = 'http://papi.minube.com/pois'
#
#         params = dict(api_key=API_KEY, lang=LANG, zone_id=GUIPUZKOA_ID, country_id=COUNTRY_ID,
#                       subcategory_id=subcategory_id)
#         res = requests.get(url, params=params)
#
#         if res.status_code == 200:
#             return res.json(), 200
#         else:
#             return {"message": res.json()}, res.status_code
#
#
# class POISList(Resource):
#
#     def get(self):
#         url = 'http://papi.minube.com/pois'
#
#         params = dict(api_key=API_KEY, lang=LANG, zone_id=GUIPUZKOA_ID, country_id=COUNTRY_ID)
#         res = requests.get(url, params=params)
#         print(res)
#         if res.status_code == 200:
#
#             return res.json(), 200
#         else:
#
#             return {"message": res.json()}, res.status_code