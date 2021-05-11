import spotipy, requests
from spotipy.oauth2 import SpotifyClientCredentials
from private import client_id, secret, oauth

top_artists = []
top_tracks = []

artists_endpoint = 'https://api.spotify.com/v1/me/top/artists'
tracks_endpoint = 'https://api.spotify.com/v1/me/top/tracks'

short_payload = {'time_range': 'short_term', 'limit': 10} 
mid_payload = {'time_range': 'medium_term', 'limit': 10} 
long_payload = {'time_range': 'long_term', 'limit': 10} 

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

artists = requests.get(artists_endpoint, params=payload, auth=BearerAuth(oauth))
tracks = requests.get(tracks_endpoint, params=payload, auth=BearerAuth(oauth))
artist_file = open('top_artists.txt', 'w')
track_file = open('top_tracks.txt', 'w')

print("Here are your top " + str(payload.get('limit')) + " artists for the past 6 months: ")
counter = 1
for i in artists.json().get("items"):
    string = str(counter) + ". " + i.get("name")
    print(string)
    artist_file.write(string + "\n")
    top_artists.append(string)
    counter += 1

print("\n")

counter = 1
print("Here are your top " + str(payload.get('limit')) + " tracks for the past 6 months: ")
for j in tracks.json().get("items"):
    string = str(counter) + ". " + j.get("name")
    print(string)
    track_file.write(string + "\n")
    top_tracks.append(string)
    counter += 1