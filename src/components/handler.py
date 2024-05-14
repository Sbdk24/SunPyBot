import telebot
from response import generate_response, UserResponses
from calculations import CalcWeather

def whishpers(bot):
    response_tracker = UserResponses("None", False)
    user_location = CalcWeather(latitude=0.0, longitude=0.0)

    # SunPy will start running when the user activates the chat

    response_tracker = UserResponses("None", False)
    user_location = CalcWeather(latitude=0.0, longitude=0.0)