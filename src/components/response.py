from components.calculations import Weather


def generate_response(latitude: float, longitude: float, return_type: str) -> str:
    # By this object we'll pass the response that user is expecting
    # Whether current or average news about weather
    tracker = Weather(latitude, longitude, command_type=return_type, location_obtained=True)

    if return_type == "sticker":
        return tracker.calc_instant_sticker()
    
    # Checking what return type user is asking and return the specific response for its petition
    return tracker.calc_current_reponse() if return_type == "weather" else tracker.calc_hourly_reponse()

