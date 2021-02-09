from datetime import datetime
import requests

currentMonth = datetime.now().month
currentYear = datetime.now().year
currentMonth = str(currentMonth).zfill(2)

endpoint = "https://api.chess.com/pub/player/"

username = input("Enter your username: ")

payload = {"username": "viren2004"}

games = requests.get(endpoint + username + "/games/" + str(currentYear) + "/" + str(currentMonth))

fp = open("last30.txt", "wb")
fp.write(games.content)
# iterate over content (game)
print("Done writing to file")
# print(games.headers)