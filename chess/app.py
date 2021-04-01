from flask import Flask, render_template, request
import chess
import lichess
import matplotlib
matplotlib.use('Agg')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')
        
@app.route('/chess', methods=['GET','POST'])
def chessdotcom():
    if request.method == "POST":
        player = request.form['player']
        if chess.test_username(player):
            win_stats = chess.ret_nice(chess.get_win_stats(player))
            ratings = chess.get_ratings(player)
            title = chess.get_title(player)
            bullet_chart = chess.chartify(chess.get_ratings_chart(player, 'bullet'), 'bullet')
            blitz_chart = chess.chartify(chess.get_ratings_chart(player, 'blitz'), 'blitz')
            rapid_chart = chess.chartify(chess.get_ratings_chart(player, 'rapid'), 'rapid')
            charts = [bullet_chart, blitz_chart, rapid_chart]
            return render_template('result.html', player=player, title=title, ratings_arr=ratings, winstats=win_stats, charts=charts)
        else:
            return render_template('error.html')

@app.route('/lichess', methods=['GET','POST'])
def lichessdotorg():
    if request.method == "POST":
        player = request.form['player']
        if lichess.test_username(player):
            data = lichess.get_request_data(player)
            win_stats = lichess.ret_nice(lichess.get_win_stats(data, player))
            ratings = lichess.get_ratings(player)
            title = lichess.get_title(player)
            bullet_chart = lichess.chartify(lichess.get_ratings_chart(data, 'bullet', player), 'bullet')
            blitz_chart = lichess.chartify(lichess.get_ratings_chart(data, 'blitz', player), 'blitz')
            rapid_chart = lichess.chartify(lichess.get_ratings_chart(data, 'rapid', player), 'rapid')
            charts = [bullet_chart, blitz_chart, rapid_chart]
            return render_template('result.html', player=player, title=title, ratings_arr=ratings, winstats=win_stats, charts=charts)
        else:
            return render_template('error.html')

if __name__ == '__main__':
    import os  
    port = int(os.environ.get('PORT', 33507)) 
    app.run(host='0.0.0.0', port=port, debug=True)
