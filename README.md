# SunPyBot
    ## Video Demo:  <https://youtu.be/uQHkmh37ECQ>
    ## Description:
    This is a telegram bot that talk to you about the weather in some creative ways. You'll be able to look at any location temperature in your own chat, and not only that, you'll be able to make a forecast for the next 8 hours of time or check weather's time with a sticker related.


    > Note: The one I'm submitting it's not the posted one on my github, I had to change it in some way I 
    > could create a test file because bots programming doesn't actually use the syntax we're using in 
    > this course

    First, I have to tell you you'll need to create a .env file to store both pyTelegramBotAPI API key and Meteosource ApiKey (Don't worry about money plan cause they're completely free).

    Then, please create your own virtual environment using the next libraries:
        **pyTelegramBotAPI**
        **pymeteosource**
        **python-dotenv**
        **python-decouple**
        **request**

    After that, we can move forward the code:

    All commands and messages are stores in **app.py** file, we'll have 5 different command options (I'll explain them one by one)

    But in fact, the ones that use all features are "sticker", "weather" and "forecast", you'll see a side bar menu at the left of your chat bar to easily any command you want. This one can be activated using the BotFather edit options (check all info about telegram APIs here: https://core.telegram.org/).

    
    Well, any of those 3 commands will pass through the next secuence:

        1. Check if user has already give us its location
            a. If yes, just go to step 3.

        2. If not, it'll start asking for a location using telegram location button
            a. If information is correct, continue
            b. If not, go back to step two, remining to user what we're expecting

        3. Until we obtain location, we save the operation we'd like to develop,
           then, go to extract the information from meteosource API and next 
           do the calculations to obtain the specific message for that temperature.

        4. After finishing that process, we'll get a string even with the message 
           we'll pass to user or the sticker id we're going to send, so that's what
           it's sent to user

        5. That it! Repeat process if you'd like to.


    So well, i'll explain all commands on detail:
    

    ### Start 
        Bot introduces itself and shows the features it has, not a super intresting thing.

    ### Weather
        Outputs a funny message about the current weather.

        In step 3, it'll go at calculations and obtain the current weather for the specific location
        prompted from a json file obtained by Meteosource API, then it pass that temperature into another
        file called messages where are located all different messages for different temperature ranges. When it finds the range where temperature is located, returns the message related with that specific temeperature as string.
        
    ### Forecast
        Outputs a funny message about the **average** weather.

        In step 3, it'll instead go through average weather function and extracts all information json's file has by hour and then calculate the average temperature for the next eight hours. 
        
        It goes to messages file where are located some other messages for different temperature ranges thought for average temperature hours. When it finds the range where temperature is located, returns the message related with that specific average as string.

    ### Sticker
        Actually works quite similar to weather command since it use the current weather petition from API, but in messages file it return now an unique sticker id related with that temperature, which is sent to a specific method back in app.py to output it in your chat.


    ### Location
        If you'd like to change the location you're using on the chat, just click to this command and it re use the function which is used at step 2 to obtain at the first time your location.


    Obiusly we can go with this further, but in my opinion it's a tiny but intersting project to enhance your skills dealing with back-end problems, not worring about UX desing o data managing.
