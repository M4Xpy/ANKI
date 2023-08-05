import os
import threading
import time
import tkinter as tk

import keyboard
import pygame
from mutagen.mp3 import MP3

from Source.letter_visual_length import visual_len
from Source.tools import press_keys

film = 'hatico'
new_srt = f"C:\\Users\\Я\\Desktop\\films\\{film}\\{film}_en_ru_align_Aug1.txt"
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
        title_duration = ((int(end[:2])) * 3600 + (int(end[3:5]) * 60) + float(
                end[6:12]
                )) + time_correct - begin + mp3_duration
        if not time_correct:
            time_correct += 1.8  # 1.0 titles before 3.0 titles after  # 3.048 +-
        dat = [mp3name, sentence, ru_sentence, begin, title_duration, mp3_duration]
        data.append(dat)
    [print(dat, end='\n') for dat in data[:5]]
    for index, dat in enumerate(data[:-1]):
        next_title_only = data[index + 1][3] - data[index][3]
        data[index].append(next_title_only)
        data[index].append(next_title_only + dat[5])

    _2 = "l"
    pause = False
    p_t = 0
    total_time = time.time()
    total_lag = 0
    time_before = total_time
    prev_title_mp3 = 0
    def check_pause():
        nonlocal pause, total_time, p_t

        def get_pause():
            nonlocal pause, total_time, p_t
            if pause:
                p_t = time.time()
            if not pause:
                total_time += time.time() - p_t
            pause = not pause

        keyboard.add_hotkey('space', get_pause)
        keyboard.wait()

    threading.Thread(target=check_pause, ).start()




    press_keys('space', 0.2, 'space', 0.2, 'left', 0.2, 'space')


    for now in data:
        mp3name, sentence, ru_sentence, begin, title_duration, mp3_duration, next_title_only, next_title_mp3 = now
        audio = f"{folder}\\{mp3name}"
        if mp3name >= '00_00_00.mp3':
            # print(prev_title_mp3, total_lag, mp3name, sep="   ")
            real_execut_time, total_lag, total_time = time_shift(prev_title_mp3, time_before, total_lag, total_time)



            while total_time > time.time():
                while pause:
                    pass
            prev_title_mp3 = next_title_mp3
            time_before = time.time()
            total_time += next_title_mp3 - 0.15

            mp3_and_subtitles(audio, mp3_duration, ru_sentence, sentence, title_duration)




def mp3_and_subtitles(audio, mp3_duration, ru_sentence, sentence, title_duration):
    if os.path.exists(audio):

        threading.Thread(
                target=pause_delay_play, args=(mp3_duration,)
                ).start()

        pygame.mixer.init()
        pygame.mixer.music.load(audio, "mp3")
        pygame.mixer.music.play()

        show_subtitle_text(sentence, ru_sentence, int(title_duration * 1000), '+0+680')

        pygame.mixer.quit()
    else:
        show_subtitle_text(sentence, ru_sentence, int(title_duration * 1000), '+0+680')


def time_shift(next_title_mp3, time_before, total_lag, total_time):
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
    return real_execut_time, total_lag, total_time


def pause_delay_play(delay):
    keyboard.press('space')
    time.sleep(delay)
    keyboard.press('space')




def show_subtitle_text(text1, text2="", delay=0, position='+0+0', font=25):

    max_len = max(visual_len(text1), visual_len(text2))
    indent = round((8907 - max_len) / 118) * " "
    font = (round((8907 / max_len) * 25), 25)[9262 > max_len]
    text = f'{indent}{text1}{333 * " "}\n{indent}{text2}{333 * " "}'
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(position)  # f'+{root.winfo_screenwidth() // 2}+100' == '+683+100'
    root.overrideredirect(True)  # Remove the window frame
    font = ('Arial', font)
    label = tk.Label(
        root, text=text, font=font, fg='white', bg='black'
        )  # Set text color to white and background to black
    label.pack()
    root.after(delay, root.destroy)  # Schedule the window to close after 5 seconds (5000 milliseconds)
    root.mainloop()


if __name__ == '__main__':

    play_audio_show_titles(new_srt, folder)
