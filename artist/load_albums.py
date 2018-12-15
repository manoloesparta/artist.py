from json import load
from re import sub
from artist.banned_words import banned_words

def load_albums(Spotify, band):
    artists_file = load(open('./artists.json'))
    artist = artists_file['artists'][band]

    albums = Spotify.artist_albums(artist)
    albums_collected_names = []
    albums_collected_id = []

    for i in range(len(albums['items'])):
        current = albums['items'][i]
        current_name = sub(r' ?\([^)]+\)', '', current['name'])

        type_of_album = current['album_type'] == 'album'
        already_registered = not current_name in albums_collected_names

        if (type_of_album and already_registered) and banned_words(current['name']):
            albums_collected_names.append(albums['items'][i]['name'])
            albums_collected_id.append(albums['items'][i]['id'])

    return [albums_collected_id, artist]