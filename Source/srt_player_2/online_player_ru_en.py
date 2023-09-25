import os
import threading
import time
import tkinter as tk

import keyboard
import mouse
import pygame
import pyperclip
from googletrans import Translator
from gtts import gTTS

from Source.letter_visual_length import visual_len

now_speed = 2
file = f"C:\\Users\\Я\\Desktop\\films\\hercules\\hercules.txt"
text_update = 200 * " "
en_sentence = text_update
ru_sentence = text_update
updated_text = f"{text_update}\n{text_update}"
mp3_ru_audio = False
pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)

def online_player():
    global en_sentence, ru_sentence, updated_text, mp3_ru_audio
    """ """

    prev_subtitle = ""
    # keyboard.send('ctrl + a')
    # time.sleep(0.3)
    # keyboard.send('space')
    # time.sleep(0.3)
    move = 1
    play_track = False


    while 1:
        move *= -1
        mouse.move(move, move, absolute=False, duration=0.0001)
        keyboard.send('ctrl + c')
        subtitle = " ".join(pyperclip.paste().splitlines()[2:])

        if prev_subtitle != subtitle:
            prev_subtitle = subtitle

            if subtitle:
                keyboard.send('space')
                _222 = 0
                translated = Translator().translate(subtitle, 'ru', 'en').text
                max_len = max(visual_len(subtitle), visual_len(translated))
                indent = round((8907 - max_len) / 117) * " "
                updated_text = f'{indent}{subtitle}{indent}         \n{indent}{translated}           {indent}'
                audio_file = gTTS(text=subtitle, lang='en')
                audio_file.save("C:\\ANKIsentences\\temporary.mp3")
                audio = "C:\\ANKIsentences\\temporary.mp3"
                pygame.mixer.init()
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.load(audio, "mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    if not _222:
                        ru_audio_file = gTTS(text=translated, lang='ru')
                        ru_audio_file.save("C:\\ANKIsentences\\ru_temporary.mp3")
                        ru_audio = "C:\\ANKIsentences\\ru_temporary.mp3"
                        _222 = 1

                pygame.mixer.music.load(ru_audio, "mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    continue

                keyboard.send('space')
                pygame.mixer.quit()
                os.remove("C:\\ANKIsentences\\temporary.mp3")
                os.remove("C:\\ANKIsentences\\ru_temporary.mp3")

            else:
                updated_text = f"{text_update}\n{text_update}"
                time.sleep(0.1)
        else:
            time.sleep(0.1)

def method_name(subtitle):
    global updated_text, mp3_ru_audio
    translated = Translator().translate(subtitle, 'ru', 'en').text
    max_len = max(visual_len(subtitle), visual_len(translated))
    indent = round((8907 - max_len) / 117) * " "
    updated_text = f'{indent}{translated}{indent}  \n{indent}{subtitle}  {indent}'
    audio_file = gTTS(text=translated, lang='ru')
    audio_file.save("C:\\ANKIsentences\\temporary.mp3")
    audio = "C:\\ANKIsentences\\temporary.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(audio, "mp3")
    pygame.mixer.music.set_volume(0.2)
    mp3_file = True


def show_subtitle_text(position='+0+0'):

    font = 20
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(position)
    root.overrideredirect(True)  # Remove the window frame
    font = ('Arial', font)
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
    threading.Thread(target=online_player).start()
    show_subtitle_text('+0+680')

    pass
