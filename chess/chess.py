from datetime import datetime
import requests
from pytz import timezone
import pytz
from dateutil import parser

currentMonth = datetime.now().month
currentYear = datetime.now().year
currentMonth = str(currentMonth).zfill(2)
my_timezone=timezone('US/Pacific')
date_format='%m/%d/%Y %H:%M:%S %Z'


endpoint = "https://api.chess.com/pub/player/"
username = input("Enter your username: ")
payload = {"username": "viren2004"}
games = requests.get(endpoint + username + "/games/" + str(currentYear) + "/" + str(currentMonth))


for i in games.json().get("games"):
    game = i.get("pgn")
    if game is not None:
        date = game.splitlines()[2][7:17]
        time = game.splitlines()[12][10:18]
        date_time_str = date + " " + time + " UTC"
        
        utc_date = parser.parse(date_time_str)

        date = utc_date.astimezone(timezone('US/Pacific'))
        print("Local date & time is: " + date.strftime(date_format))
        
