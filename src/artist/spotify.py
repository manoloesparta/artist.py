from os import environ as ev, remove
from spotipy import util, Spotify


class SpotifyUser:
    def __init__(self, username, client_id, client_secret, redirect_uri):
        self.username = username
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = 'playlist-modify-private playlist-modify-public'

        self.set_enviroment()

    def set_enviroment(self):
        ev['SPOTIPY_CLIENT_ID'] = self.client_id
        ev['SPOTIPY_CLIENT_SECRET'] = self.client_secret
        ev['SPOTIPY_REDIRECT_URI'] = self.redirect_uri

    def auth(self):
        try:
            token = util.prompt_for_user_token(self.username, self.scope)
        except:
            remove(f'.cache-{self.username}')
            token = util.prompt_for_user_token(self.username, self.scope)

        self.user = Spotify(auth=token)
        return self.user
