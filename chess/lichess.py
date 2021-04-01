from datetime import datetime
import matplotlib.pyplot as plt, mpld3
import ndjson
import requests

endpoint = "https://lichess.org/api/"

def test_username(username):
    response = requests.get(endpoint + "user/" + username)
    if response.status_code != 200:
        return False
    else:
        return True

def get_request_data(username):
    currentYear = str(datetime.now().year)
    currentMonth = str(datetime.now().month).zfill(2)
    currentMonthTime = int(datetime.strptime("01 " + currentMonth + " " + currentYear + " 00:00", "%d %m %Y %H:%M").timestamp())
    headers = {'accept': 'application/x-ndjson'}
    params = {'since' : str(currentMonthTime*1000)}
    response = requests.get(endpoint + "games/user/" + username, headers=headers, params=params)
    data = response.json(cls=ndjson.Decoder)
    return data

def get_win_stats(data, username):
    dates = {}
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
        ret.append(
            ("Stats for {0}:".format(date_played),
            "Total games played: {}".format(arr['total']),
            "Wins: {}".format(arr['W']),
            "Losses: {}".format(arr['L']),
            "Draws: {}".format(arr['D']))
        )
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

def get_ratings_chart(data, time_ctrl, username):
    dates = {}
    date_fmt = "%m/%d"
    for game in data:
        if game['speed'] == time_ctrl:
            date = datetime.fromtimestamp(game.get('createdAt')//1000)
            date_played = date.strftime(date_fmt)
            white = game.get('players').get('white')
            black = game.get('players').get('black')
            if white.get('user').get('name') == username:
                dates[date_played] = white.get('rating')
            else:
                dates[date_played] = black.get('rating')
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
    print(chartify(get_ratings_chart(get_request_data('rebeccaharris'), 'blitz', 'rebeccaharris')))
