import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

cid = os.getenv('CLIENT_ID')
secret = os.getenv('CLIENT_SECRET')
auth = SpotifyOAuth(cid, secret, scope=['playlist-modify-public',
                                        'playlist-modify-private'], redirect_uri="http://localhost:8080")
sp = spotipy.Spotify(oauth_manager=auth)

# artist = 'spotify:artist:6nfDaffa50mKtEOwR8g4df'
artist = 'bigbang'
sp_user = sp.current_user()
# print(sp_user)
# pprint(results)
user_id = sp_user['uri'].split(":")[2]
# playlist = sp.user_playlist_create(user=sp_user['id'],
#                                    name='Test numero DOIS',
#                                    description='E so um teste e nada mais.')
artist_ = sp.search(q=f'artist={artist}', type='artist', limit=1)
print(artist_['artists']['items'][0]['uri'])
exit()
songs = sp.artist_top_tracks(artist_id=artist, country='BR')
# print(songs)
# playlist_id = playlist["id"]


class Spotify():
    def __int__(self, redirect_uri="http://localhost:8080"):
        cid = os.getenv('CLIENT_ID')
        secret = os.getenv('CLIENT_SECRET')
        auth = SpotifyOAuth(cid, secret, scope=['playlist-modify-public'], redirect_uri=redirect_uri)
        self.sp = spotipy.Spotify(oauth_manager=auth)
        self.sp_user = sp.current_user()

    def get_top_songs_for_artist(self, artist):
        artist_id = artist['artists']['items'][0]['uri'] if 'spotify:artist:' not in artist else artist
        return sp.artist_top_tracks(artist_id=artist_id, country='BR')

    def add_to_playlist(self, playlist_id, track_ids):
        sp.playlist_add_items(playlist_id=playlist_id, items=track_ids)

    def get_songs_list(self, songs):
        track_ids = []
        for t in songs['items']:
            if t['type'] == 'track':
                track_ids.append(t['uri'])
                break
        return track_ids

    def create_playlist(self, playlist_name, desc):
        playlist = sp.user_playlist_create(user=self.sp_user['id'],
                                           name=playlist_name,
                                           description=desc)
        return playlist["id"]
