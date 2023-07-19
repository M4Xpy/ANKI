import os
import random
import time

from gtts import gTTS

new_srt = "C:\\Users\\Я\\Desktop\\harry_potter_subtitles_2.txt"
folder = "C:\\ANKIsentences\\harry-potter-and-the-sorcerers-stone"


def write_audio(file, folder):
    with open(file, encoding='utf-8') as srt:
        text = srt.read()
    subtitles = text.split('\n\n')
    for subtitle in subtitles:
        subtitle = subtitle.splitlines()
        mp3name = subtitle[1][:8].replace(':', '_') + '.mp3'
        ru_sentence = subtitle[4] if len(subtitle) > 4 else ""
        if subtitle[1][:12] > f"{'00:02:38.226'[:9]}000":
            if ru_sentence:
                print(ru_sentence, subtitle[1][:12])
                audio: gTTS = gTTS(text=ru_sentence, lang='ru', slow=False)  # Generate audio file
                audio_file_path: str = os.path.join(folder, mp3name)  # Save audio file to directory
                audio.save(audio_file_path)
                time.sleep(random.randint(111, 2111))


if __name__ == '__main__':
    write_audio(new_srt, folder)

    pass
