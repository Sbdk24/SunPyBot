import random

def daily_message(temperature: float) -> str:
    rounded_temp = int(temperature)

    temperature_ranges = {
        (30, float('inf')): f"El calor va a ser insoportable, pero osea feoo feo. Tenemos {rounded_temp} grados por las next hours, que buen día para no ser humano 😊",
        (26, 30): f"Apenas pueda le digo al sol que ya le pare un poquito, vamos a manejar {rounded_temp} grados por las próximas horas",
        (20, 26): f"El clima está re bueno man, osea con {rounded_temp} grados por la siguientes horas estamos naaaais",
        (15, 20): f"El día no va a estar tan feo, creo que mi amigo el sol si se va a poner a jalar :))\nTenemos unos sólidos {rounded_temp} grados por las siguientes horas",
        (9, 15): [
            f"No esperemos mucho calor por las siguientes horas, pero oye...\nSon {rounded_temp} grados. Podría ser peor 🤷‍♂️",
            f"Contamos con unas superincreíbles 8 horas de alrededor de {rounded_temp} grados, vamos pa una cafetería pal frio, invita a un amigo o algo :))",
            f"No hay buenas noticias :/. Mi amigo el sol no va a salir aunque tenemos unos {rounded_temp} que psss... Tampoco es tan tan frio"
        ],
        (5, 9): f"No hay muchas esperanzas en que la temperatura suba :( tendremos unos {rounded_temp} grados en las siguientes horas.\nYa lo sé saber que no hay sol es re triste 😔",
        (0, 5): f"Con {rounded_temp} grados de temperatura, ❄️ vete buscando un lugar calientico para pasar el rato porque va a seguir muuuy frio ❄️",
        (-float('inf'), 0): f"El termómetro marca unos {rounded_temp} grados por las proximas 8 horas.\nPor favor, tenme consideración y no me hagas trabajar mucho hoy, claramente a un sol no le gustan los días frios 🤧"
    }


    for range_, message in temperature_ranges.items():
        if range_[0] <= temperature < range_[1]:
            if isinstance(message, list):
                return random.choice(message)
            return message
