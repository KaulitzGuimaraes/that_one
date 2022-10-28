import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth
class SpotifyManager():
    def __init__(self, redirect_uri='http://localhost:8080'):
        cid = os.getenv('CLIENT_ID')
        secret = os.getenv('CLIENT_SECRET')
        auth = SpotifyOAuth(cid, secret, scope=['playlist-modify-public'], redirect_uri=redirect_uri)
        self.sp = spotipy.Spotify(oauth_manager=auth)
        self.sp_user = self.sp.current_user()

    def get_artist(self, artist_name):
        return self.sp.search(f'artist: {artist_name}',type='artist', limit=1)

    def get_top_songs_for_artist(self, artist):
        artist_id = artist['artists']['items'][0]['uri'] if 'spotify:artist:' not in artist else artist
        return self.sp.artist_top_tracks(artist_id=artist_id, country='BR')

    def get_track_name_for_track_list(self, tracks):
        track_list = []
        for track in tracks['tracks']:
            if track['type'] == 'track':
                track_list.append(
                    {
                        'uri': track['uri'],
                        'name': track['name']
                    }
                )
        return track_list

    def get_songs_list(self, songs):
        track_ids = []
        for t in songs['items']:
            if t['type'] == 'track':
                track_ids.append(t['uri'])
                break
        return track_ids

    def create_playlist(self, playlist_name, desc, track_ids):
        playlist = self.sp.user_playlist_create(user=self.sp_user['id'],
                                           name=playlist_name,
                                           description=desc)
        self.sp.playlist_add_items(playlist_id=playlist["id"], items=track_ids)
        return playlist
