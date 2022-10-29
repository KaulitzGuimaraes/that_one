import json
import pickle

from n_pl.emotions_identifier import EmotionsIdentifier
from spotify_api.spotifymanager import SpotifyManager
from pre_processing.bow import BOW
from training.classifier import Classifier
from genius.genius import GeniusLyricsFinder
from translator.translator import LyricsTranslator

sp = pickle.load(open('./sp.bin', mode='rb'))

bow = BOW.get_bow()


class Count():
    count = 0


def create_playlist_by_track(artist: str, track_name: str) -> dict:
    track = sp.get_track(track_name=track_name, artist=artist)
    print(track[0].keys())
    print(track[0]['name'])
    print(track[0]['uri'])
    print(track[0]['artists'][0]['name'])
    Classifier.open_classifier()
    cls: Classifier = Classifier.classifierManager

    prediction = cls.predict(
        bow.fit_to_bow([
            LyricsTranslator().translate_lyric(
                GeniusLyricsFinder().get_song_lyric(
                    track[0]['artists'][0]['name'],
                    track[0]['name']
                )
            )]
        )
    )
    emotion = EmotionsIdentifier.get_map()[prediction][0]
    playlist_tracks = [track[0]['uri']]
    for item in json.loads(open('./predictions.json').read()):
        if item['emotion'] == emotion:
            playlist_tracks.append(item['uri'])

    playlist = sp.create_playlist(f'{emotion.title()} #{Count.count}',
                                  'Created by an artificial intelligence.',
                                  playlist_tracks)
    Count.count += 1
    return playlist
