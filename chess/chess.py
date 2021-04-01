from datetime import datetime
import requests
from pytz import timezone
import dateutil
from dateutil import parser
import matplotlib.pyplot as plt, mpld3

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
        ret.append(
            ("Stats for {0}:".format(date_played), 
            "Played: {}".format(arr['total']), 
            "Wins: {}".format(arr['W']), 
            "Losses: {}".format(arr['L']), 
            "Draws: {}".format(arr['D']))
        )
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

def get_ratings_chart(username, time_control):
    dates = {}
    currentYear = datetime.now().year
    currentMonth = str(datetime.now().month).zfill(2)
    date_format='%m/%d/%Y'
    response = requests.get(endpoint + username + "/games/" + str(currentYear) + "/" + str(currentMonth))
    games = response.json().get("games")
    # print(games)
    for i in range(0, len(games)):
        game = games[i].get("pgn")
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
            date_played = pacific.strftime(date_format)[0:5]
            if games[i].get('time_class') == time_control:
                # print(games[i].get('time_class'), '\n')
                if not date_played in dates:
                    dates[date_played] = 0
                    white = games[i].get('white')
                    black = games[i].get('black')

                    if white.get('username') == username:
                        dates[date_played] = white.get('rating')
                        # print(games[i], '\n')
                    else:
                        dates[date_played] = black.get('rating')
                        # print(games[i], '\n')
    rating_response = requests.get(endpoint + username + "/stats").json()
    current_rating = rating_response.get("chess_"+ time_control)
    today = datetime.now().strftime(date_format)[0:5]
    if current_rating:
        dates[today] = current_rating.get("last").get("rating")
    print(time_control, dates, '\n')
    return dates

def chartify(data, time_ctrl):
    x = data.keys()
    y = data.values()
    fig = plt.figure()
    plt.plot(x, y)
    plt.title(time_ctrl)
    plt.xlabel('Date')
    plt.ylabel('Rating')
    chart = mpld3.fig_to_html(fig)
    return chart

if __name__ == "__main__":
    blitz = get_ratings_chart('boejohn', 'blitz')
    print(blitz)
#    chartify(blitz)
