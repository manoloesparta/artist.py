from os import environ
from artist.auth import auth
from artist.remove import remove
from artist.load_albums import load_albums
from artist.select_songs import select_songs
from artist.choose_songs import choose_songs
from artist.update_playlist import update_playlist
from artist.spotify import SpotifyUser

def main():

    try:
        username = environ['USERNAME']
        playlist_goal = environ['ARTIST_PLAYLIST']
        CLIENT_ID, CLIENT_SECRET = environ['CLIENT_ID'], environ['CLIENT_SECRET']
        REDIRECT_URI = environ['REDIRECT_URI']

    except KeyError as k:
         print(k, 'must be defined in the environment or you need to define the variables with your custom data')
         return 0

    user = SpotifyUser(username, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
    Spotify = user.auth()

    remove(username, playlist_goal, Spotify)
    albums_collected_id, artist = load_albums(Spotify, 'The White Stripes')
    song_id, num = select_songs(Spotify, albums_collected_id)
    chosen_songs = choose_songs(song_id, num)
    
    update_playlist(Spotify, username, playlist_goal,chosen_songs, artist)

if __name__ == '__main__':
    main()
