from pymeteosource.types import tiers
from pymeteosource.api import Meteosource
from decouple import config
import requests


# Calling API KEY from .env file (you must create your own one)
ACCOUNT_TIER = tiers.FLEXI
meteosource = Meteosource(config("METEO_TOKEN"), ACCOUNT_TIER)


def temperature_request(latitude: float, longitude: float, return_type: str) -> float:
        response = requests.get("https://www.meteosource.com/api/v1/free/point?lat=" + # Calling meteosoruce API
                            str(latitude) + "&lon=" + str(longitude) + # Passing lat & lon from live location
                            "&timezone=UTC&language=en&units=metric&key=" + # Setting language & units
                            config("METEO_TOKEN")).json() # Here you must add your own meteosruce API KEY 
        
        return current_rqst(response) if return_type == "current" else average_rqst(response)
    

def current_rqst(response):
    return response["current"]["temperature"] # Here I just only need the current temeperature value


def average_rqst(response):
    by_hours = response["hourly"]["data"] # Asking only for hourly weather data

    temperatures_list = [hour["temperature"] for hour in by_hours] # Obtain all temperatures that API currently has
    
    return sum(temperatures_list[:8]) / 8 # Uniquely use the first 8 hours