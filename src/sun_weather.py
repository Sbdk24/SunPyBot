from messages.current_msgs import special_message
from messages.average_msgs import daily_message
from api_rqst import temperature_request



class CalcWeather:
    def __init__(self, latitude: float, longitude: float): 
        self._latitude, self._longitude = latitude, longitude 


    def calc_current_reponse(self) -> str:
        temperature = self.current_temperature()
        return special_message(temperature) # There I have all possible messages for current weather


    def current_temperature(self) -> float:
        return temperature_request(self.latitude, self.longitude, return_type="current")
    

    def calc_daily_reponse(self) -> str:
        temperature = self.average_temperature()
        return daily_message(temperature)


    def average_temperature(self):
        return temperature_request(self.latitude, self.longitude, return_type="avg")


    @property
    def latitude(self):
        return self._latitude
    
    @latitude.setter
    def latitude(self, latitude):
        self._latitude = latitude


    @property
    def longitude(self):
        return self._longitude
    
    @longitude.setter
    def longitude(self, longitude):
        self._longitude = longitude