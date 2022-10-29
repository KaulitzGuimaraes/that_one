from lyricsgenius import Genius
import os


class GeniusLyricsFinder():
    def __init__(self):
        self.genius = Genius(os.getenv('GENIUS_TOKEN'))

    def get_song_lyric(self, artist: str, title: str) -> str:
        song = self.genius.search_song(artist=artist, title=title)
        return song.to_dict()['lyrics']

if __name__ == '__main__':
    t = GeniusLyricsFinder().get_song_lyric(artist='Tokio Hotel', title='Humanoid')
    print(t)