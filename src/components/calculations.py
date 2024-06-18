from components.messages import special_message_current
from components.messages import special_message_hourly
from components.messages import stickers_list
from api_rqst.meteorequest import temperature_request

class Weather:
    """
        Tracks all data about location brought by user from telegram send location.

        Args:
            latitude (float): Geolocation latitude.
            longitude (float): Geolocation longitude.
            command_type (str): Command selected by user from the Telegram menu bar.
            location_obtained (bool): Indicates if user has already add location before.
    """ 
    # In this class it's only needed lat and lon for calcs
    def __init__(self, latitude: float, longitude: float, command_type: str, location_obtained: bool) -> None: 
        """
            Instance Weather class.

        Args:
            latitude (float): Geolocation latitude.
            longitude (float): Geolocation longitude.
            command_type (str): Command selected by user from the Telegram menu bar.
            location_obtained (bool): Indicates if user has already add location before.
    """ 
        self.latitude, self.longitude = latitude, longitude 
        self.command_type, self.location_obtained = command_type, location_obtained

    # First obtain current temperature and then check for its specific message
    def calc_current_reponse(self) -> str:
        temperature = self.current_temperature()
        return special_message_current(temperature) # There I have all possible messages for current weather

    # Now we're checking average temperature and then looking for its specific message
    def calc_hourly_reponse(self) -> str:
        temperature = self.average_temperature()
        return special_message_hourly(temperature)
    
    # I'll use the current funct to check what sticker is appropiate in that situation
    def calc_instant_sticker(self) -> str:
        temperature = self.current_temperature()
        return stickers_list(temperature)

    # Calculate current temperature  
    def current_temperature(self) -> float:
        return temperature_request(self.latitude, self.longitude, return_type="current")
    
    # Calculate average temperature by the next 8 hours
    def average_temperature(self) -> float:
        return temperature_request(self.latitude, self.longitude, return_type="avg")
    
    @property
    def command_type(self):
        """
            Getter for command selected by user
        """
        return self._command_type
    
    @command_type.setter
    def command_type(self, command_type: str):
         # Check first if is str type, then if it's an accepted command type
        self._command_type = "None" if not isinstance(command_type, str) or command_type not in self.accepted_types() else command_type
        
        
    @property
    def location_obtained(self):
        """
            Getter for location obtained indicator 
        """
        return self._location_obtained
    
    @location_obtained.setter
    def location_obtained(self, location_obtained: bool):
        # Same thing, check if it's boolean type
        self._location_obtained = False if not isinstance(location_obtained, bool) else location_obtained

    @staticmethod
    def accepted_types():
        return ["weather", "forecast", "sticker"]




    def chat(self, client, question: str) -> str: #, context: str
        """
            Initializes a chat session for user interactions tracking.

            Args:
                r (redis.client.Redis): Redis database manipulator object.
                user (str): User's username.
                llm (str): Large Language Model utilized by the agent.
                conversation_id (str): Id generated to connect current session with user's chats.
                interactions_limit (int): Number of interactions allowed to be saved in caché

            Raises:
                ConnectionError: If redis is not installed/connected to the machine or
                when port (usually 6379) is not opened.
        """

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                # Aqui esta todo el contexto y al final está le pregunta actual
                #{"role": "system", "content": "Dada nuestra conversación: \n" + context},
                # Aqui la pregunta que le hago al bot
                {"role": "system", "content": "responde a la siguiente pregunta: " + question + 
                "\nPor favor, sé breve."},
            ]
        )
        bot_message = response.choices[0].message.content

        return bot_message


    """Getters and setters for latitude"""
    @property
    def latitude(self):
        return self._latitude
    
    @latitude.setter
    def latitude(self, latitude):
        self._latitude = latitude
    
    """Getters and setters for longitude"""
    @property
    def longitude(self):
        return self._longitude
    
    @longitude.setter
    def longitude(self, longitude):
        self._longitude = longitude