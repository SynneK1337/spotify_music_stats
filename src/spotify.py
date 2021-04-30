import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotify_config import *

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
))