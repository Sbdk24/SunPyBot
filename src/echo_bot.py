import telebot
from decouple import config
from response import generate_response

# To use this code you may get your own token from BotFather telegram API
bot = telebot.TeleBot(config("BOT_TOKEN"), parse_mode=None)

class ObtainFlag:
    def __init__(self, flag: str):
        self._flag = flag
    
    @property
    def flag(self):
        return self._flag
    
    @flag.setter
    def flag(self, flag: str):
        self._flag = flag

state_flag = ObtainFlag("None")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    # Obtain chat id using message hidden attributes 
    chat_id = message.chat.id

    bot.send_message(chat_id, "Helous, soy SunPy 🌞")
    bot.send_message(chat_id, "Sé todo lo que necesitas sobre el clima, pero cuando no hay sol ni me preguntes, me da pereza trabajar")
    bot.send_message(chat_id, "Solo escribe /clima en el chat para ver qué tal está el clima ahorita")
    bot.send_message(chat_id, "Escribe /pronostico si quieres saber el pronóstico de las siguientes horas")
    


@bot.message_handler(commands=["clima"])
def instant_weather(message):
    message_sent = bot.send_message(message.chat.id, "Por favor, compárteme la ubicación que deseas revisar usando el botón de ubicación de Telegram :) (también puede ser tú ubi en tiempo real si lo deseas)")
    state_flag.flag = "clima"
    # Go now to obtain location to start weather calculation
    bot.register_next_step_handler(message_sent, obtain_location)


@bot.message_handler(commands=["pronostico"])
def instant_weather(message):
    message_sent = bot.send_message(message.chat.id, "Por favor, compárteme la ubicación que deseas revisar usando el botón de ubicación de Telegram :) (también puede ser tú ubi en tiempo real si lo deseas)")
    state_flag.flag = "pronostico"
    # Go now to obtain location to start weather calculation
    bot.register_next_step_handler(message_sent, obtain_location)


def obtain_location(message):
    try:
        instant_location = message.location
        print(instant_location.latitude, "=", type(instant_location.latitude), instant_location.longitude, "=", type(instant_location.longitude))
        # Tell user to share the value we're expecting it to give
        if not isinstance(instant_location, telebot.types.Location):
            message_sent = bot.send_message(message.chat.id, "Esto no es lo que necesito la verdad :/, intenta enviarme tu ubi de nuevo")
            bot.register_next_step_handler(message_sent, obtain_location)
            return
        
    except Exception:
        bot.reply_to(message, "Te soy sincero, no sé qué es esto :/, vuelve a intentar mandarme tú ubicación por fas")
        bot.register_next_step_handler(message_sent, obtain_location)
    
    else:
        answer = generate_response(instant_location.latitude, instant_location.longitude, state_flag.flag)
        bot.send_message(message.chat.id, answer)
        print("succeed")
    

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)



bot.infinity_polling()