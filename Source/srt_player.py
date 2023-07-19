import os
import threading
import time

import keyboard
import pygame
from mutagen.mp3 import MP3

from Source.online_title_translator import show_subtitle_text

new_srt = "C:\\Users\\Я\\Desktop\\harry_potter_subtitles_2.txt"
folder = "C:\\ANKIsentences\\harry-potter-and-the-sorcerers-stone"


def get_mp3_duration(mp3_path):
    return MP3(mp3_path).info.length


def play_audio_show_titles(file, folder):
    start, old_delay, finish, remainder, time_after, differ = 0, 0, 0, 0, 0, 0
    with open(file, encoding='utf-8') as srt:
        text = srt.read()
    subtitles = text.split('\n\n')

    data = []
    for subtitle in subtitles:
        subtitle = subtitle.splitlines()
        mp3name = subtitle[1][:8].replace(':', '_') + '.mp3'
        bookmark = int('1' + mp3name[:8].replace('_', ''))
        sentence = subtitle[3]

        ru_sentence = subtitle[4] if len(subtitle) > 4 else ""

        begin = ((int(subtitle[1][:2])) * 3600 + (int(subtitle[1][3:5]) * 60) + float(subtitle[1][6:12]))
        finito = ((int(subtitle[2][:2])) * 3600 + (int(subtitle[2][3:5]) * 60) + float(subtitle[2][6:12])) - begin - 0.1
        dat = [mp3name, sentence, ru_sentence, begin, finito]
        data.append(dat)

    for index, dat in enumerate(data[:-1]):
        data[index].append(data[index + 1][3] - data[index][3] + (51, 0)[data[index][3] < 549]  )
    for dat in data[:11]:
        print(dat)

    total_time = time.time()
    keyboard.press('space')
    for now in data:

        mp3name, sentence, ru_sentence, begin, finito, delay = now
        audio = f"{folder}\\{mp3name}"
        indent = ((100 - len(sentence)) // 2 ) * ' '
        if mp3name > '00_00_00.mp3':
            while total_time > time.time():
                pass
            total_time = total_time + delay

            # xxxx = min(finito, len(sentence) * 0.12) * 2
            # subtitle_thread = threading.Thread(
            #         target=show_subtitle_text, args=(f'{indent}{" ".join(word for word in ru_sentence.split(" ") if word)}{indent}', int(xxxx * 1000), '+0+0')
            #         )
            # subtitle_thread.start()
            #
            # xxxx = min(finito, len(sentence) * 0.12) * 2
            # subtitle_thread = threading.Thread(
            #         target=show_subtitle_text, args=(
            #         f'{indent}{" ".join(word for word in sentence.split(" ") if word)}{indent}', int(xxxx * 1000),
            #         '+0+40')
            #         )
            # subtitle_thread.start()




            xxxx = min(finito, len(sentence) * 0.12) *2
            subtitle_thread = threading.Thread(
                target=show_subtitle_text, args=(f'{indent}{ru_sentence}{indent}', int(xxxx * 1000), '+0+720')
                )
            subtitle_thread.start()
            xxxx = min(finito, len(sentence) * 1.12)*2 if ru_sentence else 1
            subtitle_thread = threading.Thread(
                    target=show_subtitle_text, args=(f'{indent}{sentence}{indent}', int(xxxx * 1000), '+0+680')
                    )
            subtitle_thread.start()

            if os.path.exists(audio):



                keyboard.press('space')
                time_before = time.time()

                pygame.mixer.init()
                pygame.mixer.music.load(audio, "mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    continue
                pygame.mixer.quit()

                total_time += time.time() - time_before
                keyboard.press('space')

            xxxx = min(finito , len(sentence) * 0.12)
            subtitle_thread = threading.Thread(target=show_subtitle_text, args=(f'{indent}{ru_sentence}{indent}', int(xxxx * 1000), '+0+720')  )
            subtitle_thread.start()
            xxxx = min(finito, len(sentence) * 1.12)
            subtitle_thread = threading.Thread(
                    target=show_subtitle_text, args=(f'{indent}{sentence}{indent}', int(xxxx * 1000), '+0+680')
                    )
            subtitle_thread.start()



if __name__ == '__main__':
    play_audio_show_titles(new_srt, folder)
