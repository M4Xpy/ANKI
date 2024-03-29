import json
import os
import threading
import time
import tkinter as tk
import keyboard
import pygame
from gtts import gTTS

top_words, top_en, top_ru = "", "", ""
up_words, up_en, up_ru = "", "", ""
words, en, ru = "", "", ""
down_words, down_en, down_ru = "", "", ""
buttom_words, buttom_en, buttom_ru = "", "", ""

def font_size(text):
    len_line = len(text)
    if len_line < 82:
        return 22, 81 * " ", 81, (81 - len_line) * " "
    elif len_line < 87:
        return 20, 86 * " ", 86, ""
    elif len_line < 93:
        return 19, 92 * " ", 92, ""
    elif len_line < 99:
        return 18, 98 * " ", 98, ""
    elif len_line < 107:
        return 16, 106 * " ", 106, ""
    elif len_line < 115:
        return 15, 114 * " ", 114, ""
    elif len_line < 126:
        return 14, 125 * " ", 125, ""
    elif len_line < 138:
        return 13, 137 * " ", 137, ""
    else:
        return 11, 150 * " ", 150, ""


def audio_book_player_record():
    global top_words, top_en, top_ru, up_words, up_en, up_ru, words, en, ru, down_words, down_en, down_ru, buttom_words, buttom_en, buttom_ru

    with open('../../Source/audiobook/ready_three_line_list.json', 'r', encoding="utf-8") as file:
        three_line_list = json.load(file)
    next_video_time = time.time() + 550
    keyboard.send("f10")
    keyboard.send("space")

    for index, line in enumerate(three_line_list[:]):
        top_words, top_en, top_ru = up_words, up_en, up_ru
        up_words, up_en, up_ru = words, en, ru
        words, en, ru = down_words, down_en, down_ru
        down_words, down_en, down_ru = buttom_words, buttom_en, buttom_ru
        buttom_words, buttom_en, buttom_ru = line

        if not en.strip():
            continue

        pygame.mixer.init()
        cleaned_text = "".join(sign for sign in en.lower() if sign not in '`()"*_[]')
        en_audio_file = gTTS(text=cleaned_text, lang='en', slow=True)
        en_audio_file.save("C:\\ANKIsentences\\temporary_en_audio_file.mp3")
        en_audio = "C:\\ANKIsentences\\temporary_en_audio_file.mp3"
        pygame.mixer.music.load(en_audio, "mp3")

        time.sleep(0.5)
        keyboard.send("space")
        time.sleep(0.04)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass

        if time.time() > next_video_time:
            keyboard.send("f10")
            print(index, index+1)
            x = 1 / 0
            time.sleep(1)
            keyboard.send("f10")
        keyboard.send("space")
        pygame.mixer.quit()
    keyboard.send("f10")
    x = 1 / 0


def audio_book_player_online():
    global top_words, top_en, top_ru, up_words, up_en, up_ru, words, en, ru, down_words, down_en, down_ru, buttom_words, buttom_en, buttom_ru

    with open('../../Source/audiobook/ready_three_line_list.json', 'r', encoding="utf-8") as file:
        three_line_list = json.load(file)
    start = 1
    order = 1
    pygame.mixer.init()
    for index, line in enumerate(three_line_list[10:20]):
        top_words, top_en, top_ru = up_words, up_en, up_ru
        up_words, up_en, up_ru = words, en, ru
        words, en, ru = down_words, down_en, down_ru
        down_words, down_en, down_ru = buttom_words, buttom_en, buttom_ru
        buttom_words, buttom_en, buttom_ru = line

        if not en.strip():
            continue
        if start:
            start = 0
            en_start_audio = save_and_load_audio(en, "en_start_audio")
            pygame.mixer.music.load(en_start_audio, "mp3")
        elif order:
            pygame.mixer.music.load(en_audio_1, "mp3")
        elif not order:
            pygame.mixer.music.load(en_audio_0, "mp3")
        pygame.mixer.music.play()
        next_play = 0
        while pygame.mixer.music.get_busy():
            if not next_play:
                if order:
                    order = 0
                    en_audio_0 = save_and_load_audio(down_en, "en_audio_0")
                else:
                    order = 1
                    en_audio_1 = save_and_load_audio(down_en, "en_audio_1")
                next_play = 1
    x = 1 / 0


def save_and_load_audio(text, file_name):
    cleaned_text = "".join(sign for sign in text if sign not in '`()"*_[]')
    en_audio_file = gTTS(text=cleaned_text.lower(), lang='en', slow=True)
    file_path = os.path.join("C:\\ANKIsentences", file_name)
    en_audio_file.save(file_path)
    return file_path


def show_banner(pre='', text='', aft='', disposition='+0+0', colour='white', background='black', font='Courier New'):
    global old_line
    old_line = update(text)
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(disposition)
    root.overrideredirect(True)  # Remove the window frame
    initial_font_size, _, len_line, spaces = font_size(old_line) # Initial font size calculation
    to_show = f"{old_line}{spaces}"
    label = tk.Label(root, text=f"{pre}{to_show}{aft}", font=(font, initial_font_size), fg=colour, bg=background)
    label.pack()

    def update_text():
        # Update font size dynamically
        global old_line
        new_line = update(text)
        if old_line != new_line:
            old_line = new_line
            current_font_size, _, len_line, spaces = font_size(old_line)
            to_show = f"{old_line}{spaces}"
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
    for data in (
            ("", "top_words", "", "+0+0", "yellow"),
            ("", "top_en", "", "+0+37", "grey"),
            ("", "top_ru", "\n", "+0+66", "yellow"),
            ("", "up_words", "", "+0+136", "yellow"),
            ("", "up_en", "", "+0+174", "grey"),
            ("", "up_ru", "\n", "+0+212", "yellow"),
            ("", "words", "", "+0+282", "yellow"),
            ("", "en", "", "+0+320", "white"),
            ("", "ru", "\n ", "+0+358", "yellow"),
            ("", "down_words", "", "+0+428", "yellow"),
            ("", "down_en", "", "+0+466", "grey"),
            ("", "down_ru", "\n", "+0+504", "yellow"),
            ("", "buttom_words", "", "+0+569", "yellow"),
            ("", "buttom_en", "", "+0+607", "grey"),
            ("", "buttom_ru", "", "+0+645", "yellow")
            ):
        threading.Thread(target=show_banner, args=data).start()
        time.sleep(0.5)





if __name__ == '__main__':
    show_screen()
    audio_book_player_record()
