from flask_restful import Resource, Api, reqparse
from models.cities import CitiesModel
import requests

API_KEY = 'SAyx0slRJe'

class CityList(Resource):
    def get(self, lang, zone_id=None, country_id=None, latitude=None, longitude=None, filter=None, order_by=None):
        url = 'http://papi.minube.com/cities'
        params = dict(api_key=API_KEY, lang=lang, zone_id=zone_id, country_id=country_id,
                      latitude=latitude, longitude=longitude, filter=filter, order_by=order_by)
        res = requests.get(url, params=params)
        print(res)
        if res.status_code == 200:
            return res.json(), 200
        else:
            return {"message": res.json()}, res.status_code