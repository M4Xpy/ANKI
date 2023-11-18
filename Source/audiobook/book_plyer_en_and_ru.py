import json
import os
import threading
import time
import tkinter as tk
import keyboard
import pygame
from gtts import gTTS

from tests.exceptions.top_words import top_300, top_2000, top_5000

top_words, top_en, top_ru = "", "", ""
up_words, up_en, up_ru = "", "", ""
words, en, ru = "", "", ""
down_words, down_en, down_ru = "", "", ""
buttom_words, buttom_en, buttom_ru = "", "", ""
# buttom_words = " РЯДЫ  СВЕРХУ - СЛОВА-ПОДСКАЗКИ  СООТВЕТСТВУЮЩИХ  АНГЛИЙСКИХ  СЛОВ , РАСПОЛОЖЕННЫХ  СНИЗУ "
# buttom_en = " БЕЛЫМ  ШРИФТОМ  ОЗВУЧИВАЕМЫЙ  В  ДАННЫЙ  МОМЕНТ  АНГЛИЙСКИЙ  ТЕКСТ "
# buttom_ru = " НИЖНИЕ  РЯДЫ - ТЕКСТ-ПЕРЕВОД  НА  РУССКОМ "
stop_mark = 0
book_dense = '../../Source/audiobook/ready_three_line_list.json'
book = '../../Source/audiobook/three_line_list.json'

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


def audio_book_player_record(book):
    global top_words, top_en, top_ru, up_words, up_en, up_ru, words, en, ru, down_words, down_en, down_ru, buttom_words, buttom_en, buttom_ru

    with open(book, 'r', encoding="utf-8") as file:
        three_line_list = json.load(file)
    next_video_time = time.time() + 600
    keyboard.send("f10")
    keyboard.send("space")
    ru_audio = "C:\\ANKIsentences\\temporary_ru_audio_file.mp3"
    en_audio = "C:\\ANKIsentences\\temporary_en_audio_file.mp3"
    old_cleaned_en = "dyuyyrh7yhr"
    chunk_start = 344
    for index, line in enumerate(three_line_list[chunk_start:chunk_start+8 ], chunk_start):
        top_en, top_ru = en, ru
        words, en, ru = buttom_words, buttom_en, buttom_ru
        buttom_words, buttom_en, buttom_ru = line

        if not en.strip() or not ru.strip() or index < chunk_start:
            continue
        # print(index, en)
        # continue

        pygame.mixer.init()
        cleaned_en = "".join(sign.lower() for sign in en if sign not in '\n\'-,:`?().;!"*_[]').split()
        double = old_cleaned_en == cleaned_en
        omit_ru = len(cleaned_en) < 4 and all(word in f"{top_300} {top_2000} {top_5000} alices" for word in cleaned_en)

        if not double:
            old_cleaned_en = cleaned_en
            make_and_save_audio(en, "en")
            if not omit_ru:
                make_and_save_audio(ru, "ru")
                pygame.mixer.music.load(ru_audio, "mp3")






        time.sleep(0.5)
        keyboard.send("space")
        time.sleep(0.04)
        if not double and not omit_ru:
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pass


        pygame.mixer.music.load(en_audio, "mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass

        if time.time() > next_video_time:
            time.sleep(1)
            keyboard.send("f10")
            time.sleep(1)
            next_video_time = time.time() + 600
            keyboard.send("f10")
        keyboard.send("space")
        pygame.mixer.quit()
        print(index)
        while stop_mark:
            pass
    keyboard.send("f10")
    x = 1 / 0


def make_and_save_audio(text, language):
    try:
        cleaned_text = "".join(sign for sign in text.lower() if sign not in '`()"*_[]«»')
        gTTS(text=cleaned_text, lang=language).save(f"C:\\ANKIsentences\\temporary_{language}_audio_file.mp3")
    except:
        time.sleep(1)
        make_and_save_audio(text, language)



def audio_book_player_online(book):
    global top_words, top_en, top_ru, up_words, up_en, up_ru, words, en, ru, down_words, down_en, down_ru, buttom_words, buttom_en, buttom_ru

    with open(book, 'r', encoding="utf-8") as file:
        three_line_list = json.load(file)
    start = 1
    order = 1
    pygame.mixer.init()
    for index, line in enumerate(three_line_list[10:20]):
        top_words, top_en, top_ru = up_words, up_en, up_ru
        up_words, up_en, up_ru = words, en, ru
        words, en, ru = down_words, down_en, down_ru
        down_words, down_en, down_ru = line

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
        global old_line
        # wheter_stop_mark = stop_mark / stop_mark
        new_line = update(text)
        if old_line != new_line:
            old_line = new_line
            current_font_size, _, len_line, spaces = font_size(old_line)
            to_show = f"{old_line}{spaces}"
            label.config(text=f"{pre}{to_show}{aft}", font=(font, current_font_size))
        root.after(10, update_text)

    update_text()
    root.mainloop()


def marker_line(marker, size=1, disposition='+0+0', colour='white', background='black', font='Courier New'):
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(disposition)
    root.overrideredirect(True)  # Remove the window frame
    label = tk.Label(root, text=marker * 1360, font=(font, size), fg=colour, bg=background)
    label.pack()
    # root.after(10, update_text)
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

def show_screen1():
    for data in (
            ("", "top_en", "", "+0+13", "grey"),
            ("", "top_ru", "\n", "+0+51", "yellow"),
            ("", "up_words", "", "+0+121", "yellow"),
            ("", "up_en", "", "+0+159", "grey"),
            ("", "up_ru", "\n", "+0+197", "yellow"),
            ("", "words", "", "+0+276", "yellow"),
            ("", "en", "", "+0+314", "white"),
            ("", "ru", "", "+0+352", "yellow"),
            ("\n", "down_words", "", "+0+399", "yellow"),
            ("", "down_en", "", "+0+466", "grey"),
            ("", "down_ru", "\n", "+0+504", "yellow"),
            ("", "buttom_words", "", "+0+569", "yellow"),
            ("", "buttom_en", "", "+0+607", "grey"),
            ("", "buttom_ru", "", "+0+645", "yellow")
            ):
        threading.Thread(target=show_banner, args=data).start()
        time.sleep(0.5)
    threading.Thread(target=marker_line, args=('+0+267', 'white', 'grey')).start()
    time.sleep(0.5)
    threading.Thread(target=marker_line, args=('+0+390', 'white', 'grey')).start()


def show_screen():
    threading.Thread(target=marker_line, args=(' ', 1, '+0+343', 'black', 'grey')).start()
    for data in (
            ("", "top_en", "", "+0+13", "grey"),
            ("", "top_ru", "\n", "+0+51", "yellow"),
            # ("", "up_words", "", "+0+121", "yellow"),
            # ("", "up_en", "", "+0+159", "grey"),
            # ("", "up_ru", "\n", "+0+197", "yellow"),
            ("", "words", "", "+0+267", "grey"),
            ("", "en", "", "+0+305", "white"),
            ("", "ru", "", "+0+352", "grey"),
            # ("\n", "down_words", "", "+0+390", "yellow"),
            # ("", "down_en", "", "+0+457", "grey"),
            # ("", "down_ru", "", "+0+495", "yellow"),
            ("", "buttom_words", "", "+0+560", "yellow"),
            ("", "buttom_en", "", "+0+598", "grey"),
            ("", "buttom_ru", "", "+0+636", "yellow")
            ):
        time.sleep(0.2)
        threading.Thread(target=show_banner, args=data).start()


def check_stop_mark():
    global stop_mark
    keyboard.wait("shift")
    stop_mark = 1

if __name__ == '__main__':
    threading.Thread(target=check_stop_mark).start()

    show_screen()
    audio_book_player_record(book)
