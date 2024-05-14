# SunPyBot

## Video Demo: <https://youtu.be/uQHkmh37ECQ>

### Description:
This is a Telegram bot that talks to you about the weather in some creative ways. You'll be able to look at any location's temperature in your own chat. Not only that, you'll be able to make a forecast for the next 8 hours or check the weather's time with a related sticker.

> Note: The one I'm submitting is not the posted one on my GitHub. I had to change it in some way so I could create a test file because bot programming doesn't actually use the syntax we're using in this course.

First, I have to tell you you'll need to create a .env file to store both the pyTelegramBotAPI API key and the Meteosource API key (Don't worry about a money plan because they're completely free).

Then, please create your own virtual environment using the following libraries:
- **pyTelegramBotAPI**
- **pymeteosource**
- **python-dotenv**
- **python-decouple**
- **requests**

After that, we can move forward with the code:

All commands and messages are stored in **app.py** file. We'll have 5 different command options (I'll explain them one by one).

But in fact, the ones that use all features are "sticker", "weather", and "forecast". You'll see a sidebar menu at the left of your chat bar to easily select any command you want. This one can be activated using the BotFather edit options (check all info about Telegram APIs [here](https://core.telegram.org/)).

Well, any of those 3 commands will pass through the following sequence:

1. Check if the user has already given us their location.
    - If yes, just go to step 3.

2. If not, it'll start asking for a location using the Telegram location button.
    - If information is correct, continue.
    - If not, go back to step two, reminding the user what we're expecting.

3. Until we obtain the location, we save the operation we'd like to develop, then proceed to extract the information from the Meteosource API and do the calculations to obtain the specific message for that temperature.

4. After finishing that process, we'll get a string either with the message we'll pass to the user or the sticker ID we're going to send, and that's what is sent to the user.

5. That's it! Repeat the process if you'd like to.

So well, I'll explain all commands in detail:

### Start 
Bot introduces itself and shows the features it has, not a super interesting thing.

### Weather
Outputs a funny message about the current weather.

In step 3, it'll go through calculations and obtain the current weather for the specific location prompted from a JSON file obtained by the Meteosource API. Then, it passes that temperature into another file called messages where all different messages for different temperature ranges are located. When it finds the range where the temperature is located, it returns the message related to that specific temperature as a string.

### Forecast
Outputs a funny message about the **average** weather.

In step 3, it'll instead go through the average weather function and extract all information from the JSON file by hour, then calculate the average temperature for the next eight hours.

It goes to the messages file where some other messages for different temperature ranges are located, thought for average temperature hours. When it finds the range where the temperature is located, it returns the message related to that specific average as a string.

### Sticker
Actually works quite similar to the weather command since it uses the current weather petition from the API, but in the messages file, it returns now a unique sticker ID related to that temperature, which is sent to a specific method back in app.py to output it in your chat.

### Location
If you'd like to change the location you're using on the chat, just click on this command, and it reuses the function which is used at step 2 to obtain your location for the first time.

Obviously, we can go further with this, but in my opinion, it's a tiny but interesting project to enhance your skills dealing with backend problems, not worrying about UX design or data managing.
