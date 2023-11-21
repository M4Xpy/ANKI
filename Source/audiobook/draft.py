import json
import threading
import time
import tkinter as tk
from gtts import gTTS
import pygame
from googletrans import Translator
import os

from Source.audiobook.book_plyer_en_and_ru import marker_line


def font_size(text):
    len_line = len(text)
    if len_line < 82:
        return 22, 81 * " ", 81
    elif len_line < 87:
        return 20, 86 * " ", 86
    elif len_line < 93:
        return 19, 92 * " ", 92
    elif len_line < 99:
        return 18, 98 * " ", 98
    elif len_line < 107:
        return 16, 106 * " ", 106
    elif len_line < 115:
        return 15, 114 * " ", 114
    elif len_line < 126:
        return 14, 125 * " ", 125
    elif len_line < 138:
        return 13, 137 * " ", 137
    else:
        return 11, 150 * " ", 150



def show_banner(pre='', text='', aft='', disposition='+0+0', colour='white', background='black', font='Courier New'):
    global old_line
    old_line = update(text)
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(disposition)
    root.overrideredirect(True)  # Remove the window frame
    initial_font_size, _, len_line = font_size(old_line) # Initial font size calculation
    to_show = old_line.center(len_line)
    label = tk.Label(root, text=f"{pre}{to_show}{aft}", font=(font, initial_font_size), fg=colour, bg=background)
    label.pack()

    def update_text():
        # Update font size dynamically
        global old_line
        new_line = update(text)
        if old_line != new_line:
            old_line = new_line
            current_font_size, _, len_line = font_size(old_line)
            to_show = old_line.center(len_line)
            label.config(text=f"{pre}{to_show}{aft}", font=(font, current_font_size))
        root.after(10, update_text)

    update_text()
    root.mainloop()

def update(line):
    return {"top_words": top_words,
            "top_en": top_en,
            "top_ru": top_ru,
            "up_words": up_words,
            "up_en": up_en,
            "up_ru": up_ru,
            "words": words,
            "en": en,
            "ru": ru,
            "down_words": down_words,
            "down_en"   : down_en,
            "down_ru"   : down_ru,
            "buttom_words": buttom_words,
            "buttom_en": buttom_en,
            "buttom_ru": buttom_ru
            }[line]


def show_screen():
    threading.Thread(target=marker_line, args=(' ', 1, '+0+343', 'black', 'grey')).start()
    for data in (
            ("", "top_en", "", "+0+13", "grey"),
            ("", "top_ru", "\n", "+0+51", "yellow"),
            ("", "up_words", "", "+0+121", "yellow"),
            ("", "up_en", "", "+0+159", "grey"),
            ("", "up_ru", "\n", "+0+197", "yellow"),
            ("", "words", "", "+0+267", "grey"),
            ("", "en", "", "+0+305", "white"),
            ("", "ru", "", "+0+352", "grey"),
            ("\n", "down_words", "", "+0+390", "yellow"),
            ("", "down_en", "", "+0+457", "grey"),
            ("", "down_ru", "", "+0+495", "yellow"),
            ("", "buttom_words", "", "+0+560", "yellow"),
            ("", "buttom_en", "", "+0+598", "grey"),
            ("", "buttom_ru", "", "+0+636", "yellow")
            ):
        time.sleep(0.2)
        threading.Thread(target=show_banner, args=data).start()







if __name__ == '__main__':
    # top_words, top_en, top_ru = "Top_Words", "Top_En", "top_ru"
    # up_words, up_en, up_ru = "up_words", "up_en", "up_ru"
    # words, en, ru = "words", "en", "ru"
    # down_words, down_en, down_ru = "down_words", "down_en", "down_ru"
    # buttom_words, buttom_en, buttom_ru = "buttom_words", "buttom_en", "buttom_ru"
    #
    #
    # show_screen()

    "I don't propose to discuss politics,"
    "I don't propose to discuss politics,"
    "politics politics    politics       "
    "politics     politics      politics "
    "I don't propose to discuss politics,"
    import keyboard
    keyboard.send('f10')
    keyboard.send('y')
    keyboard.send('space')






