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
from Source.srt_player_2.compose_record_beta import make
from Source.srt_player_2.en_two_line import no_repit
from tests.exceptions.top_words import top_300, top_2000, top_5000

# bandi_data = [0, 0, 0.25, 'f10', 0, 0, 0.25, 'y', 550] # mode, next_time
duration = 50
delay = 0.5
play_pause, play_pause_next_time, play_pause_delay, play_pause_key = [1, 0, delay, 'space']
bandi_mode, bandi_next_time, bandi_delay, bandi_on_of_key, next_avi = [0, 0, delay, 'f10', duration + time.time()]
bandi_pause_mode, bandi_pause_next_time, bandi_pause_delay, bandi_pause_key = [0, 0, delay, 'y']
subtitles_pack = None
text_update = 80 * " "
updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"
error = 0

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
            subtitle = en_ru_corrector(subtitle_lines, "en")
            if subtitle:
                for part in re.split(r'[?!.;:]', subtitle):
                    part = part.strip()
                    if part:
                        en_path, ru_path, to_show_en_subtitle, to_show_ru_subtitle = process_subtitle(part)

                        updated_text = f"{to_show_en_subtitle}\n{to_show_ru_subtitle}\n{text_update}\n{text_update}"
                        pygame.mixer.init()
                        # pygame.mixer.music.set_volume(0.5)

                        make(bandi_pause="off")

                        if ru_path:
                            pygame.mixer.music.load(ru_path, "mp3")
                            pygame.mixer.music.play()
                            while pygame.mixer.music.get_busy():
                                pass
                        pygame.mixer.music.load(en_path, "mp3")
                        pygame.mixer.music.play()
                        while pygame.mixer.music.get_busy():
                            pass
                        pygame.mixer.quit()
                        make(bandi_pause="on")
                        updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"


            #     empty = 0
            # else:
            #     empty += 1
            #     if empty % 50:
            #         empty = 0


def process_subtitle(subtitle):
    global error
    try:
        to_show_en_subtitle, en_to_ru_play_subtitle, _ = no_repit(subtitle)
        to_show_ru_subtitle = Translator().translate(
                to_show_en_subtitle.lower().replace(".", ","), 'ru', 'en'
                ).text
        if en_to_ru_play_subtitle:
            to_play_ru_subtitle = Translator().translate(
                    en_to_ru_play_subtitle.lower().replace(".", ","), 'ru', 'en'
                    ).text
        else:
            to_play_ru_subtitle = ""
        if to_play_ru_subtitle:
            ru_audio_file = gTTS(text=to_play_ru_subtitle, lang='ru')
            ru_audio_file.save(f"temporary_ru_audio_file.mp3")
            ru_path = f"temporary_ru_audio_file.mp3"
        else:
            ru_path = ""
        en_audio_file = gTTS(text=to_show_en_subtitle.lower(), lang='en')
        en_audio_file.save(f"temporary_en_audio_file.mp3")
        en_path = f"temporary_en_audio_file.mp3"

        error = 0

        make(player_pause="off")
        return en_path, ru_path, to_show_en_subtitle, to_show_ru_subtitle

    except:
        print(f"problem with {subtitle}")
        time.sleep(error)
        make(player_pause="on")
        error += 1
        return process_subtitle(subtitle)


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



