from datetime import datetime
import requests
from pytz import timezone
import pytz
from dateutil import parser

currentYear = datetime.now().year
currentMonth = str(datetime.now().month).zfill(2)
date_format='%m/%d/%Y'


endpoint = "https://api.chess.com/pub/player/"
username = input("Enter your username: ")
response = requests.get(endpoint + username + "/games/" + str(currentYear) + "/" + str(currentMonth))

dates = {}


for i in response.json().get("games"):
    game = i.get("pgn")
    if game is not None:

        #date stuff
        date = game.splitlines()[2][7:17]
        time = game.splitlines()[12][10:18]
        date = date.replace('.', '/')
        date_time_str = date + " " + time + " UTC"
        utc_timestamp = parser.parse(date_time_str)
        pacific = utc_timestamp.astimezone(timezone('US/Pacific'))
        date_played = pacific.strftime(date_format)
        if not date_played in dates:
            dates[date_played] = {'W': 0, 'L': 0, 'D': 0, 'times-white': 0, 'times-black': 0}
        
        #daily record
        


print(dates)