import spotipy, requests
from spotipy.oauth2 import SpotifyClientCredentials
from private import client_id, secret, oauth


post_endpoint = "https://api.spotify.com/v1/me/player/queue"