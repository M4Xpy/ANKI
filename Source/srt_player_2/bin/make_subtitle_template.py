import time

import keyboard
import mouse
import pyperclip
import threading
import time
import tkinter as tk

import keyboard
import mouse
import pygame
import pyperclip
from googletrans import Translator
from gtts import gTTS

from Source.srt_player_2.online_player_en_ru import no_repit

movie = 'hercules'
my_srt = f"C:\\Users\\Я\\Desktop\\films\\{movie}\\{movie}.txt"
new_srt = ""
pause = False
not_finish = False

def check_for_new_srt():
    """ """
    global pause, subtitle_time, new_srt
    old_srt = ""
    move = 1
    old_time = "0"

    time.sleep(9)
    keyboard.send("ctrl + a")
    time.sleep(0.25)
    keyboard.send("space")
    time.sleep(0.25)

    while True:
        move *= -1
        mouse.move(move, move, absolute=False, duration=0.0000001)
        keyboard.send("ctrl + c")

        text_lines = pyperclip.paste().splitlines()

        new_srt = " ".join(text_lines[2:])
        try:
            subtitle_time = text_lines[1].split('/')[0]
        except IndexError:
            subtitle_time = '7777'

        if old_srt != new_srt and old_time != subtitle_time:
            old_srt = new_srt
            old_time = subtitle_time
            if new_srt:
                while not_finish:
                    if not pause:
                        keyboard.send("space")
                        pause = True
                    time.sleep(0.15)

                if pause:
                    keyboard.send("space")
                    time.sleep(0.1)
                    pause = False

                threading.Thread(target=make_srt).start()
        time.sleep(0.15)





def make_srt():
    """ """
    global not_finish
    not_finish = True
    orig_srt = new_srt
    no_repit_srt = no_repit(orig_srt)
    orig_ru_srt = Translator().translate(orig_srt, 'ru', 'en').text
    if orig_srt != no_repit_srt:
        no_repit_ru_srt = Translator().translate(no_repit_srt, 'ru', 'en').text
    else:
        no_repit_ru_srt = orig_ru_srt



    result = f"{subtitle_time}\n{no_repit_srt}\n{no_repit_ru_srt}\n{no_repit_srt}\n{no_repit_ru_srt}\n{orig_srt}\n{orig_ru_srt}\n\n"
    # play_en
    # play_ru
    # show_en
    # show_ru
    # orig_en
    # orig_ru
    with open(my_srt, "a", encoding="utf-8") as srt:
        srt.write(result)

    not_finish = False




if __name__ == '__main__':
    # threading.Thread(target=check_for_new_srt).start()
    check_for_new_srt()
    pass