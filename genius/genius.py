from lyricsgenius import Genius
import os
genius = Genius(os.get('GENIUS_TOKEN'))
song = genius.search_song('Silver Cross','Charli XCX')
s = song.to_dict()['lyrics']
print(s)