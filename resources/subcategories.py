from flask_restful import Resource
import requests

API_KEY = 'SAyx0slRJe'
LANG = "es"

class SubcategoryList(Resource):

    def get(self):
        url = 'http://papi.minube.com/subcategories'

        params = dict(api_key=API_KEY, lang=LANG)
        res = requests.get(url, params=params)

        if res.status_code == 200:
            return res.json(), 200
        else:
            return {"message": res.json()}, res.status_code
