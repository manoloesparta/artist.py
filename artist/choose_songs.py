from random import randint

def choose_songs(song_id, num):
    chosen_songs = []
    for i in range(num):
        n = randint(0, len(song_id) - 1)
        current_song = song_id[n]
        while current_song in chosen_songs:
            n = randint(0, len(song_id) - 1)
            current_song = song_id[n]
        chosen_songs.append(current_song)

    return chosen_songs