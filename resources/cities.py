from flask_restful import Resource, Api, reqparse
from models.cities import CitiesModel
import requests

API_KEY = 'SAyx0slRJe'
GUIPUZKOA_ID = 1010
COUNTRY_ID = 63
LANG = "es"


class CityList(Resource):

    def get(self):
        url = 'http://papi.minube.com/cities'
        params = dict(api_key=API_KEY, lang=LANG, zone_id=GUIPUZKOA_ID)
        res = requests.get(url, params=params)

        if res.status_code == 200:
            return res.json(), 200
        else:
            return {"message": res.json()}, res.status_code


class City(Resource):

    def get(self, city_id=None, city_name=None):
        url = 'http://papi.minube.com/cities'
        params = dict(api_key=API_KEY, lang=LANG, zone_id=GUIPUZKOA_ID, city_id=city_id, filter=city_name)
        res = requests.get(url, params=params)

        print(res.json()[0])

        if res.status_code == 200:
            return res.json(), 200
        else:
            return {"message": res.json()}, res.status_code