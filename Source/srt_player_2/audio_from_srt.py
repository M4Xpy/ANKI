import os
import random
import time
import pyperclip
from gtts import gTTS



def write_audio(film):
    file = f"C:\\Users\\Я\\Desktop\\films\\{film}\\{film}Sept21.txt"
    folder = f"C:\\ANKIsentences\\films\\{film}"
    with open(file, encoding='utf-8') as srt:
        text = srt.read()
    subtitles = text.split('\n\n')
    for subtitle in subtitles:
        subtitle = subtitle.replace('_', " ").splitlines()
        print(subtitle)
        print()
        mp3name = subtitle[1][:8].replace(':', '_') + '.mp3'
        ru_sentence = subtitle[4] if len(subtitle) > 4 else ""
        if ru_sentence:
            # timing = pyperclip.paste()
            # if subtitle[1][:12] > f"{f'{timing}'[:9]}000":
            print(ru_sentence, mp3name)
            audio: gTTS = gTTS(text=ru_sentence, lang='ru', slow=False)  # Generate audio file
            audio_file_path: str = os.path.join(folder, mp3name)  # Save audio file to directory
            audio.save(audio_file_path)
            time.sleep(random.randint(1, 2))



if __name__ == '__main__':
    write_audio('hercules')

    pass
