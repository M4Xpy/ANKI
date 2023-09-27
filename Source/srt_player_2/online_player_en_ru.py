import threading
import time
import tkinter as tk

import keyboard
import mouse
import pygame
import pyperclip
from googletrans import Translator
from gtts import gTTS

text_update = 170 * " "
updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"
mp3_ru_audio = False
mp3_en_audio = False


def online_player():
    global updated_text, mp3_ru_audio, mp3_en_audio
    """ """

    prev_subtitle = ""
    keyboard.send('ctrl + a')
    time.sleep(0.3)
    keyboard.send('space')
    time.sleep(0.3)
    move = 1
    play_track = False

    while 1:
        move *= -1
        mouse.move(move, move, absolute=False, duration=0.0001)
        keyboard.send('ctrl + c')
        subtitle = " ".join(pyperclip.paste().splitlines()[2:])

        if prev_subtitle != subtitle:
            prev_subtitle = subtitle

            if play_track:
                keyboard.send('space')
                play_track = False

                while not mp3_ru_audio:
                    pass
                mp3_ru_audio = False
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    continue

                while not mp3_en_audio:
                    pass
                mp3_en_audio = False
                pygame.mixer.music.load(en_audio, "mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    continue

                if subtitle:
                    play_track = True
                    threading.Thread(
                            target=subtitle_processing, args=(subtitle,)
                            ).start()
                else:
                    updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"

                keyboard.send('space')

            elif subtitle:
                play_track = True
                threading.Thread(
                        target=subtitle_processing, args=(subtitle,)
                        ).start()
                time.sleep(0.1)
            else:
                updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"
                time.sleep(0.1)
        else:
            time.sleep(0.1)


def subtitle_processing(subtitle):
    global updated_text, mp3_ru_audio, mp3_en_audio, ru_audio, en_audio
    subtitle = no_repit(subtitle)
    updated_text = f'{subtitle}\n{text_update}\n{text_update}\n{text_update}'
    translated = Translator().translate(subtitle, 'ru', 'en').text
    if len(translated) > 99:
        halve = translated.split()
        point = len(halve) // 2
        first = " ".join(halve[:point])
        second = " ".join(halve[point:])
        updated_text = f'{subtitle}\n{first}\n{second}\n{text_update}'
    else:
        updated_text = f'{subtitle}\n{translated}\n{text_update}\n{text_update}'
    ru_audio_file = gTTS(text=translated, lang='ru')
    ru_audio_file.save("C:\\ANKIsentences\\temporary.mp3")
    ru_audio = "C:\\ANKIsentences\\temporary.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(ru_audio, "mp3")
    pygame.mixer.music.set_volume(0.5)
    mp3_ru_audio = True

    en_audio_file = gTTS(text=subtitle, lang='en')
    en_audio_file.save("C:\\ANKIsentences\\en_temporary.mp3")
    en_audio = "C:\\ANKIsentences\\en_temporary.mp3"
    mp3_en_audio = True


def show_subtitle_text():
    font = 20
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry('+0+668')
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


def top_black_frame():
    top_message = "                                                             "
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry('+0+0')
    root.overrideredirect(True)  # Remove the window frame
    font = ('Arial', 63)
    label = tk.Label(
            root, text=top_message, font=font, fg='white', bg='black'
            )  # Set text color to white and background to black
    label.pack()
    label.config(text=top_message)


def no_repit(text):
    # """
    # >>> no_repit(" - No, no - no, no, no, no. Yes, no . - No way, no way, no way! Now, now? now? What. what.. what... - how , - how ?")
    # ' - No. Yes, No way! Now? What. how ?'
    # """
    compares = [" "]
    part = ""
    for letter in text:
        part = part + letter
        if letter not in "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            now_compare = 1
            for index, compare in enumerate(compares):
                now_compare = part.strip(' -?!,.:').lower()
                if compare.strip(' -?!,.:').lower() == now_compare and now_compare:
                    compares[index] = compares[index][:-1] + letter
                    now_compare = 0
                    break
            if now_compare or part == compares[-1][-1]:
                compares.append(part)
            part = ""
    out_put = "".join(compares) + part
    if text != out_put:
        print(f"{text}\n{out_put}\n")
    return out_put


if __name__ == '__main__':
    threading.Thread(target=online_player).start()
    threading.Thread(target=top_black_frame).start()
    show_subtitle_text()

    pass
