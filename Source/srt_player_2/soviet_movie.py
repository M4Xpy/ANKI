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

from Source.srt_player_2.en_two_line import no_repit
from tests.exceptions.top_words import top_300, top_2000, top_5000

# bandi_data = [0, 0, 0.25, 'f10', 0, 0, 0.25, 'y', 550] # mode, next_time
duration = 999999
delay = 0.25
play_pause, play_pause_next_time, play_pause_delay, play_pause_key = [1, 0, delay, 'space']
bandi_mode, bandi_next_time, bandi_delay, bandi_on_of_key, next_avi = [0, 0, delay, 'f10', duration + time.time()]
bandi_pause_mode, bandi_pause_next_time, bandi_pause_delay, bandi_pause_key = [0, 0, delay, 'y']
subtitles_pack = []
text_update = 80 * " "
updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"
go = -1



def make(player_pause="", bandi_record="", bandi_pause=""):
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




def en_ru_corrector(text, lang="en"):
    # """
    # >>> en_ru_corrector("l'm gоnnа rummаgе in thе stоrаgе сlоsеt")
    # """
    russian_to_english = {
            'А': 'A', 'В': 'B', 'С': 'C', 'Е': 'E', 'Н': 'H',
            'К': 'K', 'М': 'M', 'О': 'O', 'Р': 'P', 'Т': 'T',
            'Х': 'X', 'а': 'a', 'с': 'c', 'е': 'e', 'о': 'o',
            'р': 'p', 'х': 'x', 'у': 'y', 'к': 'k'
            }  # russian : english

    for russian, english in russian_to_english.items():
        if lang == "en":
            text = text.replace(russian, english)
        elif lang == "ru":
            text = text.replace(english, russian)
    return text.strip()


def check_new_subtitle():
    global subtitles_pack, updated_text, go
    prev_subtitle = ""
    move = 1
    cycle = 0
    odd = 1
    while True:
        time.sleep(0.1)
        # if go > -1:
        #     go = 0
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
            go = 1
            prev_subtitle = subtitle_lines
            subtitle = en_ru_corrector(subtitle_lines, "en")
            if subtitle:
                odd = (1, 0)[odd]





                to_show_en_subtitle, en_to_ru_play_subtitle, _ = no_repit(subtitle)

                to_show_ru_subtitle = Translator().translate(
                    to_show_en_subtitle.lower().replace(".", ","), 'ru', 'en'
                    ).text



                en_audio_file = gTTS(text=to_show_en_subtitle.lower(), lang='en')
                en_audio_file.save(f"temporary_en{odd}_audio_file.mp3")
                en_path = f"temporary_en{odd}_audio_file.mp3"

                print(len(subtitles_pack))
                while len(subtitles_pack):
                    make(player_pause="on")
                subtitles_pack.append(en_path)
                updated_text = f"{to_show_en_subtitle}\n{to_show_ru_subtitle}\n{text_update}\n{text_update}"
                go = 0

        #     else:
        #         go = 0
        # else:
        #     go = 0





def online_player():
    global subtitles_pack, updated_text, go

    pyperclip.copy("")
    keyboard.send('ctrl + a')
    time.sleep(delay)
    make(player_pause="off", bandi_record="on")

    while True:
        while len(subtitles_pack) < 1 or not go:
            pass

        en_path = subtitles_pack[0]
        print(en_path)
        pygame.mixer.init()
        # pygame.mixer.music.set_volume(0.5)


        pygame.mixer.music.load(en_path, "mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
        pygame.mixer.quit()
        make(player_pause="off")
        updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"

        del subtitles_pack[0]






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
    threading.Thread(target=check_new_subtitle).start()
    online_player()


