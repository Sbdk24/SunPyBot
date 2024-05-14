import telebot
from components.response import generate_response, UserResponses
from components.calculations import CalcWeather
from decouple import config
from components.handler import whispers

# To activate your bot you may get your own token from BotFather telegramp API
bot = telebot.TeleBot(config("BOT_TOKEN"), parse_mode=None)

whispers(bot)

response_tracker = UserResponses("None", False)
user_location = CalcWeather(latitude=0.0, longitude=0.0)


# SunPy will start running when the user activates the chat

@bot.message_handler(commands=["start"])
def send_welcome(message):
    # Obtain chat id using message hidden attributes
    chat_id = message.chat.id

    # Chat messages displayed at the beginning of the conversation
    bot.send_message(chat_id, "Hey, I am SunPy 🌞")

    bot.send_message(chat_id, "If you're new, check out my functionalities below at the menu.")


# Weather update and notification


@bot.message_handler(commands=["weather"])
def instant_weather(message):
    # Passing by reference type of response for the user and use it in obtain location function
    response_tracker.command_type = "weather"

    if response_tracker.location_obtained:
        location_already_obtained(message)
        return

    message_sent = location_message(message)
    # Go now to obtain location to start weather calculation
    bot.register_next_step_handler(message_sent, obtain_location)


"""Weather Forecast update and notification"""


@bot.message_handler(commands=["forecast"])
def daily_weather(message):
    # Passing by reference type of response for the user and use it in obtain location function
    response_tracker.command_type = "forecast"

    if response_tracker.location_obtained:
        location_already_obtained(message)
        return

    message_sent = location_message(message)
    # Go now to obtain location to start weather calculation
    bot.register_next_step_handler(message_sent, obtain_location)


@bot.message_handler(commands=["sticker"])
def sticker_like(message):
    # Passing by reference type of response for the user and use it in obtain location function
    response_tracker.command_type = "sticker"
    if response_tracker.location_obtained:
        location_already_obtained(message)
        return

    message_sent = location_message(message)
    # Go now to obtain location to start weather calculation
    bot.register_next_step_handler(message_sent, obtain_location)


def location_already_obtained(message):
    answer = generate_response(user_location.latitude, user_location.longitude,
                               response_tracker.command_type)

    # When user is asking fore sticker, we need a different command
    if response_tracker.command_type == "sticker":
        bot.send_sticker(message.chat.id, answer)
        return

     # After response is obtained, send it as an answer via telegram chat
    bot.send_message(message.chat.id, answer)
    # Print internally success of program
    print("succeed")


@bot.message_handler(commands=["location"])
def change_location(message):
    response_tracker.command_type = "location"
    message_sent = location_message(message)
    # Go now to obtain location to start weather calculation
    bot.register_next_step_handler(message_sent, obtain_location)


def location_message(message):
    message_sent = bot.send_message(message.chat.id, "Please, share your " +
                                    "location using the Telegram button :) " +
                                    "(it can also be in real time if you wish)")
    return message_sent


def obtain_location(message):
    try:  # Trying to get the user's location
        instant_location = message.location

        # If successful, print location on the terminal window
        print(instant_location.latitude, "=", type(instant_location.latitude),
              instant_location.longitude, "=", type(instant_location.longitude))

        # If not, tell the user to share the value we're expecting to get
        if not isinstance(instant_location, telebot.types.Location):
            message_sent = bot.send_message(message.chat.id, "This is not what I need" +
                                            " :/, try sending me your location again")

            # Track that the location wasn't successfully obtained
            response_tracker.location_obtained = False

            bot.register_next_step_handler(message_sent, obtain_location)
            return

    # If an unexpected error occurs, just try again using the same function
    except Exception:
        bot.reply_to(message, "To be honest, I don't know what this is :/, try again by " +
                     "sending me your location please")
        # Track that the location wasn't successfully obtained
        response_tracker.location_obtained = False

        bot.register_next_step_handler(message_sent, obtain_location)
        return

    # When everything goes well, use lat & long from its location
    else:
        # Now we can be sure his location is now saved
        response_tracker.location_obtained = True
        user_location.latitude, user_location.longitude = instant_location.latitude, instant_location.longitude
        if response_tracker.command_type == "location":
            return

        answer = generate_response(user_location.latitude, user_location.longitude,
                                   response_tracker.command_type)

        # When user is asking fore sticker, we need a different command
        if response_tracker.command_type == "sticker":
            bot.send_sticker(message.chat.id, answer)
            return

        # After response is obtained, send it as an answer via telegram chat
        bot.send_message(message.chat.id, answer)
        # Print internally success of program
        print("succeed")


"""When the user prompts something unexpected, just copy and paste"""


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
