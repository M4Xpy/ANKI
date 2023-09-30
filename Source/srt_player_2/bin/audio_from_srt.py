import os
import random
import time
import pyperclip
from gtts import gTTS
import time


def write_audio(film):
    file = f"C:\\Users\\Я\\Desktop\\films\\{film}\\{film}.txt"
    folder = f"C:\\ANKIsentences\\films\\{film}"
    with open(file, encoding='utf-8') as srt:
        text = srt.read()
    subtitles = text.split('\n\n')

    start = time.time()
    for subtitle in subtitles:
        subtitle = subtitle.splitlines()


        if subtitle[0] :
            # print(subtitle)
            time_data = subtitle[0].strip().replace(':', '_')
            zeros = {
                    4: "00_0",
                    5: "00_",
                    7: "0"
                    }[len(time_data)]

            if len(subtitle[1]) > 2:
                en_sentence = subtitle[1]

                en_norm_mp3_name = zeros + time_data + '_en_norm.mp3'
                print(en_norm_mp3_name, en_sentence)
                audio: gTTS = gTTS(text=en_sentence, lang='en', slow=False)  # Generate audio file
                audio_file_path: str = os.path.join(folder, en_norm_mp3_name)  # Save audio file to directory
                audio.save(audio_file_path)

                en_slow_mp3_name = zeros + time_data + '_en_slow.mp3'
                audio: gTTS = gTTS(text=en_sentence, lang='en', slow=True)  # Generate audio file
                audio_file_path: str = os.path.join(folder, en_slow_mp3_name)  # Save audio file to directory
                audio.save(audio_file_path)

            if len(subtitle[2]) > 2:
                ru_sentence = subtitle[2]

                ru_norm_mp3_name = zeros + time_data + '_ru_norm.mp3'
                print(ru_norm_mp3_name, ru_sentence)
                audio: gTTS = gTTS(text=ru_sentence, lang='ru', slow=False)  # Generate audio file
                audio_file_path: str = os.path.join(folder, ru_norm_mp3_name)  # Save audio file to directory
                audio.save(audio_file_path)

                ru_slow_mp3_name = zeros + time_data + '_ru_slow.mp3'
                audio: gTTS = gTTS(text=ru_sentence, lang='ru', slow=True)  # Generate audio file
                audio_file_path: str = os.path.join(folder, ru_slow_mp3_name)  # Save audio file to directory
                audio.save(audio_file_path)
            print()






        time.sleep(random.randint(1, 2) * 0.1)

    print(time.time() - start, len(subtitles))
# 188.17341208457947 1230
# 203.73446130752563 1230





if __name__ == '__main__':
    write_audio('hercules')

    pass
