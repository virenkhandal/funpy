from datetime import datetime
import requests
from pytz import timezone
import pytz
import dateutil
from dateutil import parser

currentYear = datetime.now().year
currentMonth = str(datetime.now().month).zfill(2)
date_format='%m/%d/%Y'


endpoint = "https://api.chess.com/pub/player/"
username = input("Enter your username: ")
response = requests.get(endpoint + username + "/games/" + str(currentYear) + "/" + str(currentMonth))

dates = {}
win = ['win']
loss = ['checkmated', 'timeout', 'resigned', 'threecheck']
draw = ['stalemate', 'timevsinsufficient', 'insufficient', 'repetition', 'agreed']

for i in response.json().get("games"):
    game = i.get("pgn")
    if game is not None:

        #date stuff
        date = game.splitlines()[2][7:17]
        time = game.splitlines()[12][10:18]
        date = date.replace('.', '/')

        try:
            # normal games
            date_time_str = date + " " + time + " UTC"
            utc_timestamp = parser.parse(date_time_str)
        except dateutil.parser._parser.ParserError:
            try:
                # weird 'setup' game
                new_time = game.splitlines()[14][10:18]
                date_time_str = date + " " + new_time + " UTC"
                utc_timestamp = parser.parse(date_time_str)
            except dateutil.parser._parser.ParserError:
                try:
                    # tournament game
                    new_time = game.splitlines()[13][10:18]
                    date_time_str = date + " " + new_time + " UTC"
                    utc_timestamp = parser.parse(date_time_str)
                except dateutil.parser._parser.ParserError:
                    # chess960 game
                    new_time = game.splitlines()[15][10:18]
                    date_time_str = date + " " + new_time + " UTC"
                    utc_timestamp = parser.parse(date_time_str)

        pacific = utc_timestamp.astimezone(timezone('US/Pacific'))
        date_played = pacific.strftime(date_format)
        if not date_played in dates:
            dates[date_played] = {'W': 0, 'L': 0, 'D': 0, 'total': 0,'times-white': 0, 'times-black': 0}

        #daily record
        white = i.get('white')
        black = i.get('black')
        dates.get(date_played)['total'] += 1
        # print("white: " + white.get('result'))
        # print("black: " + black.get('result'))

        if white.get('username') == username :
            dates.get(date_played)['times-white'] += 1
            if white.get('result') in win:
                dates.get(date_played)['W'] += 1
            elif white.get('result') in loss:
                dates.get(date_played)['L'] += 1
            elif white.get('result') in draw:
                dates.get(date_played)['D'] += 1
        else:
            dates.get(date_played)['times-black'] += 1
            if black.get('result') in win:
                dates.get(date_played)['W'] += 1
            elif black.get('result') in loss:
                dates.get(date_played)['L'] += 1
            elif black.get('result') in draw:
                dates.get(date_played)['D'] += 1
            
        # print("White: " + i.get('white').get('result'))
        # print("Black: " + i.get('black').get('result'))

def print_nice(dates):
    for date_played, arr in dates.items():
        print("Stats for {0}:".format(date_played))
        print("Total games played: {}".format(arr['total']))
        print("Wins: {}".format(arr['W']))
        print("Losses: {}".format(arr['L']))
        print("Draws: {}".format(arr['D']))
        print("======")

print()
title = requests.get(endpoint + username).json().get("title")
if not title:
    title = "player"
print("Wins/Losses/Draws for {} {}".format(title, username))
rating_response = requests.get(endpoint + username + "/stats").json()
bullet_rating = rating_response.get("chess_bullet")
if bullet_rating:
    bullet_rating = bullet_rating.get("last").get("rating")
    print("Bullet rating (1 min): {}".format(bullet_rating))
blitz_rating = rating_response.get("chess_blitz")
if blitz_rating:
    blitz_rating = blitz_rating.get("last").get("rating")
    print("Blitz rating (3-5 min): {}".format(blitz_rating))
rapid_rating = rating_response.get("chess_rapid")
if rapid_rating:
    rapid_rating = rapid_rating.get("last").get("rating")
    print("Rapid rating (10 min+): {}".format(rapid_rating))

print()
print_nice(dates)
