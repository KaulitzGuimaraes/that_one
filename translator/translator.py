import logging
from pprint import pprint

from googletrans import Translator

class LyricsTranslator():
    def __init__(self):
        self.translator = Translator()

    def translate_lyric(self, lyric: str):
        translation = self.translator.translate(lyric)
        # print(f'{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})')
        return translation.text