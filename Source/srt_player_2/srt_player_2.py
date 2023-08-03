import os
import threading
import time
import tkinter as tk
import weakref

import keyboard
import pygame
from mutagen.mp3 import MP3

from Source.letter_visual_length import visual_len

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
        begin, end = subtitle[1].split(' --> ')
        sentence = subtitle[2]
        ru_sentence = subtitle[3]
        mp3_duration = get_mp3_duration(f"{folder}\\{mp3name}")
        begin = (int(begin[:2]) * 3600 + (int(begin[3:5]) * 60) + float(begin[6:12])) + time_correct
        title_duration = ((int(end[:2])) * 3600 + (int(end[3:5]) * 60) + float(end[6:12])) + time_correct - begin + mp3_duration
        if not time_correct:
            time_correct += 3.0      # 1.0 titles before 3.0 titles after
# if total_time += then    time_correct += 2.3  # time.sleep(0.2)
# if total_time -= then    time_correct += 3.0   # time.sleep(0.2)
        dat = [mp3name, sentence, ru_sentence, begin, title_duration, mp3_duration]
        data.append(dat)
    [print(dat, end='\n') for dat in data[:5]]
    for index, dat in enumerate(data[:-1]):

        next_title_only = data[index + 1][3] - data[index][3]
        data[index].append(next_title_only)
        data[index].append(next_title_only+dat[5])
    [print(dat, end='\n') for dat in data[:5]]

    total_time = time.time()

    keyboard.press('space')
    time.sleep(0.2)
    _2, title_duration  = "l", 0
    mp3_duration = 0
    mp3name = 0
    next_title_mp3 = 0
    total_lag = 0
    for now in data:

        old_title_duration = title_duration
        mp3name, sentence, ru_sentence, begin, title_duration, mp3_duration, next_title_only, next_title_mp3 = now

        audio = f"{folder}\\{mp3name}"

        # _1 = time.time()
        # if _2 == "l":
        #     _2, _3 = _1, 0
        # else:
        #     _2, _3 = _1, _1 - _2 #- old_title_duration
        #
        #
        # time_before = time.time()

        if mp3name >= '00_00_29.mp3':
            while total_time > time.time():
                pass
            time_before = time.time()
            total_time += next_title_mp3



            if os.path.exists(audio):

                threading.Thread(target=pause_delay_play, args=(mp3_duration,)
                                 ).start()

                pygame.mixer.init()
                pygame.mixer.music.load(audio, "mp3")
                pygame.mixer.music.play()
                show_subtitle_text(sentence, ru_sentence, int(title_duration * 1000), '+0+680')

                pygame.mixer.quit()


            else:
                show_subtitle_text(sentence, ru_sentence, int(title_duration * 1000), '+0+680')



            real_execut_time = time.time() - time_before
            if real_execut_time > next_title_mp3:
                total_lag += real_execut_time - next_title_mp3
            else:
                diff = next_title_mp3 - real_execut_time
                if total_lag > diff:
                    total_lag -= diff
                    total_time += diff
                else:
                    total_time += total_lag
                    total_lag = 0


            print(real_execut_time, next_title_mp3, total_lag, mp3name, sep="   ")




            # x = time.time() - time_before - title_duration
            # print(x)
            # total_time += x


def pause_delay_play(delay):
    keyboard.press('space')
    time.sleep(delay)
    keyboard.press('space')




def show_subtitle_text(text1, text2="", delay=0, position='+0+0', font=25) :

    max_len = max(visual_len(text1), visual_len(text2))
    indent = round((8907 - max_len) / 118) * " "
    font = (round((8907 / max_len) * 25), 25)[9262 > max_len]
    text = f'{indent}{text1}{333 * " "}\n{indent}{text2}{333 * " "}'
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(position)   # f'+{root.winfo_screenwidth() // 2}+100' == '+683+100'
    root.overrideredirect(True)  # Remove the window frame
    font = ('Arial', font)
    label = tk.Label(root, text=text, font=font, fg='white', bg='black')  # Set text color to white and background to black
    label.pack()
    root.after(delay, root.destroy)  # Schedule the window to close after 5 seconds (5000 milliseconds)
    root.mainloop()











if __name__ == '__main__':



    play_audio_show_titles(new_srt, folder)
