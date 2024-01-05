from pymeteosource.types import sections, langs, units, tiers
from pymeteosource.api import Meteosource
from datetime import datetime, timedelta
from decouple import config
import requests
import json


ACCOUNT_TIER = tiers.FLEXI
meteosource = Meteosource(config("METEO_TOKEN"), ACCOUNT_TIER)


latitude = 19.401671
longitude = -99.200548

response = requests.get("https://www.meteosource.com/api/v1/free/point?lat=" + str(latitude) + "&lon=" + str(longitude) + "&timezone=UTC&language=en&units=metric&key=" + config("METEO_TOKEN")).json() 

by_hours = response["hourly"]["data"]

temperatures_list = [hour["temperature"] for hour in by_hours]
print(temperatures_list[:8])
print(len(temperatures_list))