<p align="center">
  <a>
    <img width="200px" src="./image.png" alt="Artists.py" />
    <h1 align="center">Artist.py</h1>
  </a>
</p>

<p align="center">
	<a href="https://github.com/manoloesparta/artist.py/releases">
		<img src="https://img.shields.io/badge/Version-1.0.0-blue.svg" alt="Version">
	</a>
  <a>
		<img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="License">
	</a>
  <a>
    <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" alt="Python">
  </a>
</p>

> Another way for discovering new artists

This script generates a new playlist for a selected artist, it applies a lot of filters starting with the word in banned_words.json, it has my default configuration but its made so that everybody can edit it.

**The file artists.json is for personal configuration the default bands are chosed by me but it is intended that you add more artists with the format used in the file, name and Spotify Artist ID**

## Requirements

```
git clone https://github.com/manoloesparta/artist.py
cd artist
pip3 install -r requirements.txt
```
Export some enviroments variables
```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```

## Usage
Edit the following line with the codename you set up in the artists.json
```python
albums_collected_id, artist = load_albums(Spotify, 'ARTIST_NAME')
```
Exceute with
```
python3 main.py
```

## Docker
For bulding your own docker container you need to specify some enviroment variables with:
```bash
docker build -t artist.py \
--build-arg user='username' \
--build-arg playlist='0iYFyrLsby2E0QBBPs2xWi' \
--build-arg id='8589a322e8b142a0bf76ac9da43cfb92' \
--build-arg secret='cd0629c79f544c959ebbbbb23fd0239b' \
--build-arg uri='http://google.com/' .
```
For running the container
```bash
docker run --rm -v $(pwd):/user/src/ -it artist.py bash
```

## License
This project is licensed under the MIT License