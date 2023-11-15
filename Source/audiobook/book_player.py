import json
import threading
import time
import tkinter as tk

from googletrans import Translator


from Source.audiobook.process import audio_book_player


def font_size(text):
    len_line = len(text)
    if len_line < 82:
        return 22, 81 * " "
    elif len_line < 87:
        return 20, 86 * " "
    elif len_line < 93:
        return 19, 92 * " "
    elif len_line < 99:
        return 18, 98 * " "
    elif len_line < 107:
        return 16, 106 * " "
    elif len_line < 115:
        return 15, 114 * " "
    elif len_line < 126:
        return 14, 125 * " "
    elif len_line < 138:
        return 13, 137 * " "
    else:
        return 11, 150 * " "


def show_zero(disposition="+0+306", colour='white', background="black"):
    global lines_zero, old_line
    old_line = lines_zero
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(disposition)
    root.overrideredirect(True)  # Remove the window frame
    initial_font_size, len_line = font_size(lines_zero) # Initial font size calculation
    label = tk.Label(root, text=f"{len_line}\n{lines_zero}\n{len_line}", font=('Courier New', initial_font_size), fg=colour, bg=background)
    label.pack()

    def update_text():
        # Update font size dynamically
        global old_line
        if old_line != lines_zero:
            old_line = lines_zero
            current_font_size, len_line = font_size(old_line)
            to_show = f"{len_line}\n{old_line}\n{len_line}"
            label.config(text=to_show, font=('Courier New', current_font_size))
        root.after(10, update_text)

    update_text()
    root.mainloop()


def show_zero_words(disposition="+0+236", colour='yellow', background="black"):
    global lines_zero_words, old_lines_zero_words
    old_lines_zero_words = lines_zero_words
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(disposition)
    root.overrideredirect(True)  # Remove the window frame
    initial_font_size, len_line = font_size(lines_zero_words) # Initial font size calculation
    label = tk.Label(root, text=f"{len_line}\n{lines_zero_words}", font=('Courier New', initial_font_size), fg=colour, bg=background)
    label.pack()

    def update_text():
        # Update font size dynamically
        global old_lines_zero_words
        if old_lines_zero_words != lines_zero_words:
            old_lines_zero_words = lines_zero_words
            current_font_size, len_line = font_size(old_lines_zero_words)
            to_show = f"{len_line}\n{old_lines_zero_words}"
            label.config(text=to_show, font=('Courier New', current_font_size))
        root.after(10, update_text)

    update_text()
    root.mainloop()


def show_zero_ru(disposition="+0+408", colour='yellow', background="black"):
    global lines_zero_ru, old_lines_zero_ru
    old_lines_zero_ru = lines_zero_ru
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(disposition)
    root.overrideredirect(True)  # Remove the window frame
    initial_font_size, len_line = font_size(lines_zero_ru) # Initial font size calculation
    label = tk.Label(root, text=f"{lines_zero_ru}\n{len_line}", font=('Courier New', initial_font_size), fg=colour, bg=background)
    label.pack()

    def update_text():
        # Update font size dynamically
        global old_lines_zero_ru
        if old_lines_zero_ru != lines_zero_ru:
            old_lines_zero_ru = lines_zero_ru
            current_font_size, len_line = font_size(old_lines_zero_ru)
            to_show = f"{old_lines_zero_ru}\n{len_line}"
            label.config(text=to_show, font=('Courier New', current_font_size))
        root.after(10, update_text)

    update_text()
    root.mainloop()

def audio_book_player():
    global lines_zero_words, lines_zero, lines_zero_ru
    with open('../../Source/audiobook/ready_three_line_list.json', 'r', encoding="utf-8") as file:
        three_line_list = json.load(file)
        for (words, en, ru) in three_line_list:
            lines_zero_words, lines_zero, lines_zero_ru = (words, en, ru)
            time.sleep(2)



if __name__ == '__main__':
    lines_zero_words = "ZERO WORDS"
    threading.Thread(target=show_zero_words).start()
    lines_zero = "MAIN TEXT"
    threading.Thread(target=show_zero).start()
    lines_zero_ru = "ZERO RU"
    threading.Thread(target=show_zero_ru).start()
    audio_book_player()
