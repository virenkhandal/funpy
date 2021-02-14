from datetime import datetime
import ndjson
import requests

endpoint = "https://lichess.org/api/"

def test_username(username):
    response = requests.get(endpoint + "user/" + username)
    if response.status_code != 200:
        return False
    else:
        return True

def get_win_stats(username):
    dates = {}
    currentYear = str(datetime.now().year)
    currentMonth = str(datetime.now().month).zfill(2)
    currentMonthTime = int(datetime.strptime("01 " + currentMonth + " " + currentYear + " 00:00", "%d %m %Y %H:%M").timestamp())
    headers = {'accept': 'application/x-ndjson'}
    params = {'since' : str(currentMonthTime*1000)}
    response = requests.get(endpoint + "games/user/" + username, headers=headers, params=params)
    data = response.json(cls=ndjson.Decoder)
    date_fmt = "%m/%d/%Y"
    for game in data:
        date = datetime.fromtimestamp(game.get('createdAt')//1000)
        date_played = date.strftime(date_fmt)
        if not date_played in dates:
            dates[date_played] = {'W': 0, 'L': 0, 'D': 0, 'total': 0,'times-white': 0, 'times-black': 0}

        #daily record
        white = game.get('players').get('white')
        dates.get(date_played)['total'] += 1

        if white.get('user').get('name') == username :
            dates.get(date_played)['times-white'] += 1
            if game.get('winner') == 'white':
                dates.get(date_played)['W'] += 1
            elif game.get('winner') == 'black':
                dates.get(date_played)['L'] += 1
            elif game.get('status') == 'draw':
                dates.get(date_played)['D'] += 1
        else:
            dates.get(date_played)['times-black'] += 1
            if game.get('winner') == 'black':
                dates.get(date_played)['W'] += 1
            elif game.get('winner') == 'white':
                dates.get(date_played)['L'] += 1
            elif game.get('status') == 'draw':
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
    title = requests.get(endpoint + "user/" + username).json().get("title")
    if not title:
        title = "player"
    return title

def get_ratings(username):
    ret = []
    rating_response = requests.get(endpoint + "user/" + username).json().get('perfs')
    bullet_rating = rating_response.get("bullet")
    if bullet_rating and bullet_rating.get('games') > 0:
        bullet_rating = bullet_rating.get("rating")
        ret.append("Bullet rating (1 min): {}".format(bullet_rating))
    blitz_rating = rating_response.get("blitz")
    if blitz_rating and blitz_rating.get('games') > 0:
        blitz_rating = blitz_rating.get("rating")
        ret.append("Blitz rating (3-5 min): {}".format(blitz_rating))
    rapid_rating = rating_response.get("rapid")
    if rapid_rating and rapid_rating.get('games') > 0:
        rapid_rating = rapid_rating.get("rating")
        ret.append("Rapid rating (10 min+): {}".format(rapid_rating))
    return ret
