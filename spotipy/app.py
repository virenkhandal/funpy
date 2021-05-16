from flask import Flask, render_template, request
from spotify import *
# import matplotlib
# matplotlib.use('Agg')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    artists = spotify.getArtists()
    tracks = spotify.getTracks()
    return render_template('index.html', artists=artists, tracks=tracks)

if __name__ == '__main__':
    import os  
    port = int(os.environ.get('PORT', 33507)) 
    app.run(host='0.0.0.0', port=port, debug=True)
