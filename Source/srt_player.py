import os
import threading
import time

import keyboard
import pygame
from mutagen.mp3 import MP3

from Source.letter_visual_length import visual_len
from Source.online_title_translator import show_subtitle_text

film = 'hatico'
new_srt = f"C:\\Users\\Я\\Desktop\\films\\{film}\\hatico_en_ru_align.txt"
folder = f"C:\\ANKIsentences\\films\\{film}"


def get_mp3_duration(mp3_path):
    try:
        return MP3(mp3_path).info.length
    except:
        return 0


def play_audio_show_titles(file, folder):
    with open(file, encoding='utf-8') as srt:
        text = srt.read()
    subtitles = text.split('\n\n')
    time_correct = 0
    data = []
    for subtitle in subtitles:
        subtitle = subtitle.splitlines()
        mp3name = subtitle[1][:8].replace(':', '_') + '.mp3'
        begin , finito = subtitle[1].split(' --> ')
        sentence = subtitle[2]
        ru_sentence = subtitle[3]
        mp3_duration = get_mp3_duration(f"{folder}\\{mp3name}")
        begin = (int(begin[:2]) * 3600 + (int(begin[3:5]) * 60) + float(begin[6:12]) ) + time_correct
        finito = ((int(finito[:2])) * 3600 + (int(finito[3:5]) * 60) + float(finito[6:12])) + time_correct - begin +  mp3_duration
        if not time_correct:
            time_correct += 2.1  # 1.0 titles before 3.0 titles after

        dat = [mp3name, sentence, ru_sentence, begin, finito, mp3_duration]
        data.append(dat)

    for index, dat in enumerate(data[:-1]):
        delay = data[index + 1][3] - data[index][3]
        data[index].append(delay )
        data[index][4] = min(delay + dat[5] , dat[4] * 1.2) + 0.3


    total_time = time.time()

    keyboard.press('space')

    for now in data:
        mp3name, sentence, ru_sentence, begin, finito, _, delay = now
        audio = f"{folder}\\{mp3name}"
        if mp3name >= '00_00_00.mp3':
            while total_time > time.time():
                pass
            total_time = total_time + delay
            # show_subtitle_text(sentence, ru_sentence, int(finito * 1000), '+0+680')
            # threading.Thread(target=show_subtitle_text, args=(sentence, ru_sentence, int(finito * 1000), '+0+680')
            #                  ).start()

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

if __name__ == '__main__':
    play_audio_show_titles(new_srt, folder)
