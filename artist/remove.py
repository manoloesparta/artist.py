
def remove(username, playlist_goal, Spotify):
    results = Spotify.user_playlist_tracks(username, playlist_goal)
    playlist = results['items']

    removed = []
    for track in playlist:
        removed.append(track['track']['id'])

    Spotify.user_playlist_remove_all_occurrences_of_tracks(username, playlist_goal, removed)
