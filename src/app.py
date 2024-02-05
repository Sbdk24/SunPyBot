import telebot
from decouple import config
from response import generate_response, UserResponses
from sun_weather import CalcWeather


# To activate your bot you may get your own token from BotFather telegram API
bot = telebot.TeleBot(config("BOT_TOKEN"), parse_mode=None)
response_tracker = UserResponses("None", False)
user_location = CalcWeather(latitude=0.0, longitude=0.0)


"""Here sunpy'll start running when user activates chat"""
@bot.message_handler(commands=["start"])
def send_welcome(message):
    # Obtain chat id using message hidden attributes 
    chat_id = message.chat.id

    # Chat messages displayed at the beggining of the conversation
    bot.send_message(chat_id, "Helou, soy SunPy 🌞")

    bot.send_message(chat_id, "Sé todo lo que necesitas sobre el clima," +
                      "cuando hay sol, cuando no me da mucha pereza 😴")
    
    bot.send_message(chat_id, "Escribe /clima en el chat para ver qué tal" +
                     " está el clima ahorita")
    
    bot.send_message(chat_id, "Escribe /pronostico si quieres saber el " +
                    "pronóstico de las siguientes 8 horas")


"""Weather update and notification"""
@bot.message_handler(commands=["clima"])
def instant_weather(message):
    # Passing by reference type of response for user and use it in obtain location function
    response_tracker.command_type = "clima"
    
    if not response_tracker.location_obtained:
        message_sent = bot.send_message(message.chat.id, ask_location_msg())
        

        # Go now to obtain location to start weather calculation
        bot.register_next_step_handler(message_sent, obtain_location)

    else:
        answer = generate_response(user_location.latitude, user_location.longitude,
                                    response_tracker.command_type)
        # After response is obtained, send it as answer via telegrarm chat
        bot.send_message(message.chat.id, answer)
        # Print internally success of program
        print("succeed")


"""Weather Forecast update and notification"""
@bot.message_handler(commands=["pronostico"])
def instant_weather(message):
    # Passing by reference type of response for user and use it in obtain location function
    response_tracker.command_type = "pronostico"
    if not response_tracker.location_obtained:
        message_sent = bot.send_message(message.chat.id, ask_location_msg())
        

        # Go now to obtain location to start weather calculation
        bot.register_next_step_handler(message_sent, obtain_location)
    else:
        answer = generate_response(user_location.latitude, user_location.longitude, 
                                   response_tracker.command_type)
        # After response is obtained, send it as answer via telegrarm chat
        bot.send_message(message.chat.id, answer)
        # Print internally success of program
        print("succeed")


def obtain_location(message):
    try: # Trying to get user's location
        instant_location = message.location

        # If successful, print location on terminal window
        print(instant_location.latitude, "=", type(instant_location.latitude),
               instant_location.longitude, "=", type(instant_location.longitude))

        # If not, tell user to share the value we're expecting to get
        if not isinstance(instant_location, telebot.types.Location):
            message_sent = bot.send_message(message.chat.id, "Esto no es lo que necesito" + 
                                            "la verdad :/, intenta enviarme tu ubi de nuevo")
            
            # Track that location wasn't succesfully obtained
            response_tracker.location_obtained = False

            bot.register_next_step_handler(message_sent, obtain_location)
            return
        
    # If unexpected error ocurrs, just try again using same function
    except Exception:
        bot.reply_to(message, "Te soy sincero, no sé qué es esto :/, vuelve a intentar " +
                    "mandandome tú ubicación plis")
        # Track that location wasn't succesfully obtained
        response_tracker.location_obtained = False

        bot.register_next_step_handler(message_sent, obtain_location)
        return
    
    # When everything goes well, use lat & long from its location
    else:
        # Now we can be sure his location is now saved
        response_tracker.location_obtained = True
        user_location.latitude, user_location.longitude = instant_location.latitude, instant_location.longitude,

        answer = generate_response(instant_location.latitude, instant_location.longitude,
                                     response_tracker.command_type)
        # After response is obtained, send it as answer via telegrarm chat
        bot.send_message(message.chat.id, answer)
        # Print internally success of program
        print("succeed")


def ask_location_msg():
    return "Por favor, compárteme la " + "ubicación usando el botonsito de Telegram :) " + "(también puede ser en tiempo real si así lo deseas)"


"""When user prompt smth unexpected, just copy and paste"""
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()


