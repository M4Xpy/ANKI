import re
import threading
import time
import tkinter as tk

import keyboard
import mouse
import pygame
import pyperclip
from googletrans import Translator
from gtts import gTTS

from Source.srt_player_2.compose_record import en_ru_corrector

duration = 999999
delay = 1
play_pause, play_pause_next_time, play_pause_delay, play_pause_key = [1, 0, delay, 'space']
bandi_mode, bandi_next_time, bandi_delay, bandi_on_of_key, next_avi = [0, 0, delay, 'f10', duration + time.time()]
bandi_pause_mode, bandi_pause_next_time, bandi_pause_delay, bandi_pause_key = [0, 0, delay, 'y']
subtitles_pack = None
text_update = 80 * " "
updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"



def make(player_pause: object = "", bandi_record: object = "", bandi_pause: object = "") -> object:
    global next_avi, play_pause_next_time, play_pause, bandi_next_time, bandi_mode, bandi_pause_next_time, bandi_pause_mode
    while time.time() < max(bandi_next_time if player_pause else 0,
                            bandi_next_time if bandi_record else 0,
                            bandi_pause_next_time if bandi_pause else 0):
        pass
    if bandi_pause_mode and play_pause and time.time() > next_avi:
        keyboard.send(bandi_on_of_key)
        time.sleep(delay)
        keyboard.send(bandi_on_of_key)
        next_avi = time.time() + duration
        keyboard.send(bandi_pause_key)
        time.sleep(delay)

    if player_pause:
        act = {"on": 1, "off": 0}[player_pause]
        if play_pause != act:
            print(f"play_pause was{play_pause}, become{act}")
            play_pause = act
            keyboard.send(play_pause_key)
            play_pause_next_time = time.time() + play_pause_delay

    if bandi_record:
        act = {"on": 1, "off": 0}[bandi_record]
        if bandi_mode != act:
            bandi_mode = act
            keyboard.send(bandi_on_of_key)
            bandi_next_time = time.time() + bandi_delay

    if bandi_pause:
        act = {"on": 1, "off": 0}[bandi_pause]
        if bandi_pause_mode != act:
            print(f"bandi_pause_mode was{bandi_pause_mode}, become{act}")
            bandi_pause_mode = act
            keyboard.send(bandi_pause_key)
            bandi_pause_next_time = time.time() + bandi_pause_delay

def check_new_subtitle():
    global subtitles_pack, updated_text
    prev_subtitle = ""
    move = 1
    pyperclip.copy("")
    keyboard.send('ctrl + a')
    time.sleep(1)
    make(player_pause="off", bandi_record="on", bandi_pause="on")
    while True:
        time.sleep(0.1)
        move *= -1
        mouse.move(move, move, absolute=False, duration=0.0001)
        keyboard.send('ctrl + c')
        subtitle_lines = " ".join(
                [
                        line for line in pyperclip.paste().splitlines()
                        if not
                           any(
                                   word in line for word in
                                   ["Качество", "Звук", "Субтитры", "Скорость", "Масштаб", '0:00/ 0:00', "/ 2:", "/ 1:",
                                    "/ 3:"]
                                   ) and line
                        ]
                )
        if "Пропустить" in subtitle_lines:
            continue
        if prev_subtitle != subtitle_lines:
            prev_subtitle = subtitle_lines
            subtitle = en_ru_corrector(subtitle_lines, "en").strip()

            if subtitle:
                updated_text = f"{subtitle}\n{text_update}\n{text_update}\n{text_update}"
                make(bandi_pause="off")
                to_show_ru_subtitle = Translator().translate(
                subtitle.lower().replace(".", ","), 'ru', 'en'
                ).text

                updated_text = f"{subtitle}\n{to_show_ru_subtitle}\n{text_update}\n{text_update}"

            else:
                make(bandi_pause="on")
                updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"
        elif not subtitle_lines:
            make(bandi_pause="on")
            updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"










def show_subtitle_text():
    font = 22
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry('+0+668')
    root.overrideredirect(True)  # Remove the window frame
    font = ('Courier New', font)
    label = tk.Label(
            root, text=updated_text, font=font, fg='white', bg='black'
            )  # Set text color to white and background to black
    label.pack()

    def update_text():
        label.config(text=updated_text)
        root.after(10, update_text)

    update_text()
    root.mainloop()





if __name__ == '__main__':
    threading.Thread(target=show_subtitle_text).start()
    check_new_subtitle()



