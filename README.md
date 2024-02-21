# SunPyBot
## Video Demo
[Watch the video demo](https://youtu.be/uQHkmh37ECQ)

## Description
This is a Telegram bot that talks to you about the weather in some creative ways. You'll be able to check the temperature of any location in your own chat. Not only that, you'll also be able to get a forecast for the next 8 hours or check the weather's time with a related sticker.

> Note: Helou :)

First, you'll need to create a `.env` file to store both the pyTelegramBotAPI API key and the Meteosource API key (Don't worry about the cost because they're completely free).

Then, please create your own virtual environment using the following libraries:
- pyTelegramBotAPI
- pymeteosource
- python-dotenv
- python-decouple
- requests

After that, we can move forward with the code.

All commands and messages are stored in `app.py`. There are 5 different command options (explained below), but the ones that use all features are "sticker," "weather," and "forecast."

These commands can be accessed through a side bar menu at the left of your chat bar, which can be activated using the BotFather edit options (check all info about Telegram APIs [here](https://core.telegram.org/)).

### Command Process
1. Check if the user has already provided their location.
   - If yes, proceed to step 3.

2. If not, it'll start asking for a location using the Telegram location button.
   - If the information is correct, continue.
   - If not, go back to step two, reminding the user what we're expecting.

3. Until we obtain the location, we save the operation we'd like to develop, then extract the information from the Meteosource API and do the calculations to obtain the specific message for that temperature.

4. After finishing that process, we'll get a string with either the message we'll pass to the user or the sticker ID we're going to send, which is then sent to the user.

5. That's it! Repeat the process if needed.

### Command Details

- **Start:** Bot introduction.
- **Weather:** Outputs a funny message about the current weather.
- **Forecast:** Outputs a funny message about the average weather for the next 8 hours.
- **Sticker:** Returns an unique sticker ID related to the current weather.
- **Location:** Allows changing the location used in the chat.

This project is a small but interesting opportunity to enhance your skills dealing with backend problems, without worrying about UX design or data management.
