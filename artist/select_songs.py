from tqdm import tqdm

def select_songs(Spotify, albums_collected_id):
    song_id = []
    for i in tqdm(range(len(albums_collected_id))):
        set_list = Spotify.album_tracks(albums_collected_id[i])
        for song in set_list['items']:
            song_id.append(song['id'])
    num = len(song_id)//2
    if num > 100: num = 100

    return [song_id, num]
