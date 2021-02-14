from datetime import datetime
import requests
from pytz import timezone
import dateutil
from dateutil import parser

endpoint = "https://api.chess.com/pub/player/"

win = ['win']
loss = ['checkmated', 'timeout', 'resigned', 'threecheck']
draw = ['stalemate', 'timevsinsufficient', 'insufficient', 'repetition', 'agreed']

def test_username(username):
    response = requests.get(endpoint + username)
    if not response:
        return False
    else:
        return True

def get_win_stats(username):
    dates = {}
    currentYear = datetime.now().year
    currentMonth = str(datetime.now().month).zfill(2)
    date_format='%m/%d/%Y'
    response = requests.get(endpoint + username + "/games/" + str(currentYear) + "/" + str(currentMonth))
    games = response.json().get("games")
    games = games[::-1]
    # print(games)
    # games = games.reverse()
    for i in games:
        game = i.get("pgn")
        if game:
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
    return dates

def ret_nice(dates):
    ret = []
    for date_played, arr in dates.items():
        ret.append("Stats for {0}:".format(date_played))
        ret.append("Total games played: {}".format(arr['total']))
        ret.append("Wins: {}".format(arr['W']))
        ret.append("Losses: {}".format(arr['L']))
        ret.append("Draws: {}".format(arr['D']))
        ret.append("======")
    return ret

def get_title(username):
    title = requests.get(endpoint + username).json().get("title")
    if not title:
        title = "player"
    return title

def get_ratings(username):
    ret = []
    rating_response = requests.get(endpoint + username + "/stats").json()
    bullet_rating = rating_response.get("chess_bullet")
    if bullet_rating:
        bullet_rating = bullet_rating.get("last").get("rating")
        ret.append("Bullet rating (1 min): {}".format(bullet_rating))
    blitz_rating = rating_response.get("chess_blitz")
    if blitz_rating:
        blitz_rating = blitz_rating.get("last").get("rating")
        ret.append("Blitz rating (3-5 min): {}".format(blitz_rating))
    rapid_rating = rating_response.get("chess_rapid")
    if rapid_rating:
        rapid_rating = rapid_rating.get("last").get("rating")
        ret.append("Rapid rating (10 min+): {}".format(rapid_rating))
    return ret


# print("Wins/Losses/Draws for {} {}".format(get_title(username), username))
