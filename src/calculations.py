from messages import special_message_current
from messages import special_message_hourly
from messages import stickers_list
from meteorequest import temperature_request

class CalcWeather:
    # In this class it's only needed lat and lon for calcs
    def __init__(self, latitude: (float, None), longitude: (float, None)): 
        self._latitude, self._longitude = latitude, longitude 

    # First obtain current temperature and then check for its specific message
    def calc_current_reponse(self) -> str:
        temperature = self.current_temperature()
        return special_message_current(temperature) # There I have all possible messages for current weather

    # Now we're checking average temperature and then looking for its specific message
    def calc_hourly_reponse(self) -> str:
        temperature = self.average_temperature()
        return special_message_hourly(temperature)
    
    # I'll use the current funct to check what sticker is appropiate in that situation
    def calc_instant_sticker(self) -> str:
        temperature = self.current_temperature()
        return stickers_list(temperature)

    # Calculate current temperature  
    def current_temperature(self) -> float:
        return temperature_request(self.latitude, self.longitude, return_type="current")
    
    # Calculate average temperature by the next 8 hours
    def average_temperature(self) -> float:
        return temperature_request(self.latitude, self.longitude, return_type="avg")


    """Getters and setters for latitude"""
    @property
    def latitude(self):
        return self._latitude
    
    @latitude.setter
    def latitude(self, latitude):
        self._latitude = latitude
    
    """Getters and setters for longitude"""
    @property
    def longitude(self):
        return self._longitude
    
    @longitude.setter
    def longitude(self, longitude):
        self._longitude = longitude