import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from common.constants import REDIRECT_URL
class SpotifyManager():
    def __init__(self, spotify):
        self.sp = spotify
        self.sp_user = self.sp.current_user()

    def get_track(self, track_name: str, artist: str):
        track = self.sp.search(q=f'artist: {artist} track: {track_name}', type='track', limit=1)
        return [x for x in track['tracks']['items'] if x['type'] == 'track']

    def get_artist(self, artist_name: str):
        return self.sp.search(f'artist: {artist_name}', type='artist', limit=1)

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

    def create_playlist(self, playlist_name: str, desc: str, track_ids: list):
        playlist = self.sp.user_playlist_create(user=self.sp_user['id'],
                                           name=playlist_name,
                                           description=desc)
        self.sp.playlist_add_items(playlist_id=playlist["id"], items=track_ids)
        return playlist
