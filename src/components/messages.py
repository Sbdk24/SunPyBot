import random


# These ranges are fully switchable if you'd like to change them organized by name
temp_ranges =  {"super_hot": (30, float('inf')), 
                "hot": (26, 30), "average": (20, 26),
               "kinda_cold": (13, 20), "is_colder": (9, 13),
               "really_cold": (5, 13), "insufferable": (0, 5), 
               "ice": (-float('inf'), 0)
            }


def special_message_current(temperature: float) -> str:
    rounded_temp = int(temperature)

    # Here I have a simple message to explain all range of temperatures for a specific moment
    messages_by_range = {
        temp_ranges["super_hot"]: f"If we continue at {rounded_temp} degrees, please turn me off.\nI mean, I know I'm SunPy and all, but nobody can handle this.",
        temp_ranges["hot"]: f"A somewhat powerful heat but bearable, we currently have {rounded_temp} degrees :))",
        temp_ranges["average"]: f"Nice weather, {rounded_temp} degrees is the perfect temperature to relax and sunbathe for a while ⛅",
        temp_ranges["kinda_cold"]: f"We currently have {rounded_temp} degrees, it's perfect.\nI hope it doesn't drop any further because otherwise, I'll have to cool down, and that's just too much effort :(",
        temp_ranges["is_colder"]: [
            f"The day looks like we're going to shiver. {rounded_temp} degrees?? Noooo, working in this is such a hassle 😴",
            f"This cold of {rounded_temp} degrees is for a coffee or hot chocolate with the biggest, furriest jacket you have, and it's probably going to get worse :/",
            f"If the {rounded_temp} degrees keep dropping, I'm literally going to start crying and I won't send you anything anymore."
        ],
        temp_ranges["really_cold"]: f"The sun doesn't feel like working\nYou're at {rounded_temp} degrees, so don't go out for anything in the world",
        temp_ranges["insufferable"]: f"With {rounded_temp} degrees, I'm not even going to work, the servers are going to freeze.",
        temp_ranges["ice"]: f"You should move, my friend.\nWhy do you keep living in such a cold place??? You're at {rounded_temp} degrees 🥶🥶"
    }

    return find_your_message(messages_by_range, temperature)


def special_message_hourly(temperature: float) -> str:
    rounded_temp = int(temperature)

    # These ones are thought for average forecast temperatures
    messages_by_range = {
        temp_ranges["super_hot"]: f"The heat is going to be unbearable, like really ugly. We have {rounded_temp} degrees for the next hours, what a great day to not be human 😊",
        temp_ranges["hot"]: f"As soon as I can, I'll tell the sun to calm down a bit, we're going to have {rounded_temp} degrees for the next hours",
        temp_ranges["average"]: f"The weather is really nice, man, with {rounded_temp} degrees for the next hours, we're all good",
        temp_ranges["kinda_cold"]: f"The day won't be so bad, I think my friend the sun will actually do some work :))\nWe have a solid {rounded_temp} degrees for the next hours",
        temp_ranges["is_colder"]: [
            f"Don't expect much heat for the next hours, but hey...\nIt's {rounded_temp} degrees. It could be worse 🤷‍♂️",
            f"We have some super amazing 8 hours with around {rounded_temp} degrees, let's go to a café for the cold, invite a friend or something :))",
            f"There's no good news :/. My friend the sun won't come out even though we have around {rounded_temp} degrees, well... it's not that cold"
        ],
        temp_ranges["really_cold"]: f"There's not much hope for the temperature to rise :( we'll have around {rounded_temp} degrees in the next hours.\nI know, knowing that there's no sun is really sad 😔",
        temp_ranges["insufferable"]: f"With {rounded_temp} degrees, ❄️ find a warm place to hang out because it's going to be very cold ❄️",
        temp_ranges["ice"]: f"The thermometer shows around {rounded_temp} degrees for the next 8 hours.\nPlease, have some consideration and don't make me work too much today, clearly, the sunpy doesn't like cold days 🤧"
    }

    return find_your_message(messages_by_range, temperature)


def stickers_list(temperature: float) -> str:
    stickers_by_range = {
        # Sun heated by the high temperature
        temp_ranges["super_hot"]: "CAACAgIAAxkBAAELUcNlwGMjcndfvqtnXDddkiz54uyHBgAC2AADUomRI2V0cN023Kl6NAQ",  
        # Sun with sunglasses
        temp_ranges["hot"]: "CAACAgIAAxkBAAELUcVlwGNKaiWudoOGaui9CsEMwax6PAAC1wADUomRIxJisMdoFAViNAQ",
        # Penguin with red jacket saying literally "cool"
        temp_ranges["average"]: "CAACAgIAAxkBAAELUc9lwGVb7KqavvhklAlSkJSQVSNykwACxAUAAj-VzAq0p9HqKKcM4jQEs",
        # Cloud fighting with the sun for being in the front
        temp_ranges["kinda_cold"]: "CAACAgIAAxkBAAELUc9lwGVb7KqavvhklAlSkJSQVSNykwACxAUAAj-VzAq0p9HqKKcM4jQE",
        
        temp_ranges["is_colder"]: [
            # A green bird taking a cup of coffe
            "CAACAgIAAxkBAAELUdVlwGWyzHvT6Xgb0rXh8A1ejOXAUQACdwEAAladvQorspFPkDuVODQE",
            # # A blue penguin looking at the window
            "CAACAgIAAxkBAAELUdFlwGVwhLpKIWqSGHi-Ga38fqW4VwACygUAAj-VzAo8YTavwr_JXzQE",
        ],
        # Literally an ice with red jacket which inside of it has shows a like XD
        temp_ranges["really_cold"]: "CAACAgIAAxkBAAELUcllwGOkquhqhD1VEjePti89EiSkfgACfRMAAso2UUl7H7rRo9vhTjQE",
        # Ice being happy and looking at some snowflakes
        temp_ranges["insufferable"]: "CAACAgIAAxkBAAELUdllwGvh7VJFilC76x7HC_WNkp363gACxxEAAhEuUUngkpaNreJG0TQE",
        # Old ice walking int snow
        temp_ranges["ice"]: "CAACAgIAAxkBAAELUcFlwGMAAZ-nFeJFvU2fjDJPiA1KOIIAAmcSAAJ7dfBJNRS6MfjrwQ40BA"
    }

    return find_your_message(stickers_by_range, temperature)



def find_your_message(messages_by_range, temperature):
    # Here we'll look what's temperature range and prompt it respective message or sticker
    for range_, message in messages_by_range.items():
        if range_[0] <= temperature < range_[1]:
            if isinstance(message, list):
                return random.choice(message)
            return message
