from flask_restful import Resource
import requests


class Weather(Resource):
    def get(self, date1, date2):

        day1 = date1[:2]
        month1 = date1[2:4]
        year1 = date1[4:]

        day2 = date2[:2]
        month2 = date2[2:4]
        year2 = date2[4:]

        final_date = year2 + month2 + day2

        url = 'https://api.sandbox.euskadi.eus/euskalmet/weather/regions/basque_country/forecast/at/' + year1 + '/'\
              + month1 + '/' + day1 + '/for/'+final_date
        print(url)

        params = dict(aud="met01.apikey", iss="hackathon", exp="1600000000", version="1.0.0",
                      iat="1600000000", email="racsofernan@gmail.com")

        res = requests.get(url, params=params)

        if res.status_code == 200:
            print()
            return {"message": res.json()['forecastTextByLang']['SPANISH']}, 200
        else:
            return {"message": res.json()}, res.status_code