from os import environ, remove
from spotipy import util, Spotify

def auth(username, playlist_goal):
    username = environ['username']
    scope = 'playlist-modify-private'
    playlist_goal = '4v3NiG1FGPSPzCI1Be0if6'

    try:
        token = util.prompt_for_user_token(username, scope)
    except:
        remove(f'.cache-{username}')
        token = util.prompt_for_user_token(username, scope)

    return Spotify(auth=token)
