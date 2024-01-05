import random

def special_message(temperature: float) -> str:
    rounded_temp = int(temperature)

    temperature_ranges = {
        (30, float('inf')): f"Si seguimos a {rounded_temp} grados, por favor apágame.\nOsea yo sé que soy SunPy y todo pero esto no lo aguanta nadie",
        (26, 30): f"Un calorsito algo potente pero soporable, {rounded_temp} grados tenemos en este momento :))",
        (20, 26): f"Clima agradable, {rounded_temp} grados es la temperatura perfecta para relajarte y tomar el sol un rato ⛅",
        (13, 20): f"Tenemos en este momento {rounded_temp} grados, está perfectoooo.\nEspero no baje más porque sino me wua enfriar y que pereza :(",
        (9, 13): [
            f"El día tiene cara de que vamos a tiritar. {rounded_temp} grados?? Noooo , que pereza trabajar así 😴",
            f"Este frio de {rounded_temp} grados está para un café o un chocolate con la chamarra más grande y peluda que tengas, y seguramente se ponga peor :/",
            f"Si los {rounded_temp} grados siguen bajando, literalmente me voy a poner a llorar y no voy a mandarte nada más."
        ],
        (5, 9): f"El sol no se sabe la de chambear\nEstás a {rounded_temp} so no salgas por nada del mundo",
        (0, 5): f"Con {rounded_temp} grados de temperatura ni yo voy a chambear, los servidores se van a helar.",
        (-float('inf'), 0): f"Ya múdate, amigo.\nPor qué sigues viviendo en un lugar tan frio??? estás a {rounded_temp} grados 🥶🥶"
    }

    for range_, message in temperature_ranges.items():
        if range_[0] <= temperature < range_[1]:
            if isinstance(message, list):
                return random.choice(message)
            return message
