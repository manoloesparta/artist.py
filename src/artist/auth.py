from os import environ, remove
from spotipy import util, Spotify

def auth(username):
    scope = 'playlist-modify-private'
    try:
        token = util.prompt_for_user_token(username, scope)
    except:
        remove(f'.cache-{username}')
        token = util.prompt_for_user_token(username, scope)

    return Spotify(auth=token)
 