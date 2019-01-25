def update_playlist(Spotify, username, playlist_goal, chosen_songs, artist):
    Spotify.user_playlist_add_tracks(username, playlist_goal, chosen_songs)
    
    artist_name = Spotify.artist(
        artist)['name'].lower().replace(' ', '') + '.py'

    Spotify.user_playlist_change_details(
        username, playlist_goal, name=artist_name)
