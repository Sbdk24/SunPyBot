from sun_weather import CalcWeather

def generate_response(latitude: float, longitude: float, return_type: str) -> str:
    tracker = CalcWeather(latitude, longitude)

    return tracker.calc_current_reponse() if return_type == "clima" else tracker.calc_daily_reponse()

