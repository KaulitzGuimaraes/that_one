from googletrans import Translator, constants
translator = Translator()
for phrase in '''
You make me 스르르 천천히 잠들어
You make me ay, ay, ay
다정히 불어오는 바람처럼'''.split('\n'):
    translation = translator.translate(phrase)
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")