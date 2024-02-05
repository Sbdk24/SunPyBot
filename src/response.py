from calculations import CalcWeather


def generate_response(latitude: float, longitude: float, return_type: str) -> str:
    # By this object we'll pass the response that user is expecting
    # Whether current or average news about weather
    tracker = CalcWeather(latitude, longitude)
    if return_type == "sticker":
        return tracker.calc_instant_sticker()
    "If user writes 'weather', generate that reponse, in other case, return daily news instead"
    return tracker.calc_current_reponse() if return_type == "weather" else tracker.calc_hourly_reponse()

""" 
This class tracks both command type user is currently using And checks if location was already passed, just for not being
annoying asking for user's location everytime it's used.
"""

class UserResponses:
    def __init__(self, command_type: str, location_obtained: (bool)):
        self._command_type, self._location_obtained = command_type, location_obtained
    
    @property
    def command_type(self):
        return self._command_type
    
    @command_type.setter
    def command_type(self, command_type: str):
         # Check first if is str type, then if it's an accepted command type
        self._command_type = "None" if not isinstance(command_type, str) or command_type not in accepted_types() else command_type
        
        
    @property
    def location_obtained(self):
        return self._location_obtained
    
    @location_obtained.setter
    def location_obtained(self, location_obtained: bool):
        # Same thing, check if it's boolean type
        self._location_obtained = False if not isinstance(location_obtained, bool) else location_obtained


def accepted_types():
    return ["weather", "forecast", "sticker"]

