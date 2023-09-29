import threading
import time
import tkinter as tk
import os
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
film = "hercules"
en_speed = ("norm", "slow")[0]
ru_speed = ("norm", "slow")[0]

def parralel_player():
    global updated_text, mp3_ru_audio, mp3_en_audio

    file = f"C:\\Users\\Я\\Desktop\\films\\{film}\\{film}.txt"
    folder = f"C:\\ANKIsentences\\films\\{film}"
    with open(file, encoding='utf-8') as srt:
        text = srt.read()
    subtitles_hub = text.split('\n\n')

    en_mp3_name = ""
    ru_mp3_name = ""
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

        subtitle_lines = pyperclip.paste().splitlines()
        len_subtitle_lines = len(subtitle_lines)
        index = {
                0: 99,
                1: 99,
                2: 99,
                3: 2,
                4: 2,
                5: 99,
                6: 99,
                7: 99,
                8: 7,
                9: 7
                }[len_subtitle_lines if len_subtitle_lines < 10 else 0]
        subtitle = " ".join(subtitle_lines[index:])



        if prev_subtitle != subtitle:
            prev_subtitle = subtitle
            print(subtitle, subtitle_lines)

            if play_track :
                play_track = False
                keyboard.send('space')

                if ru_mp3_name:


                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        continue
                    ru_mp3_name = ""

                if en_mp3_name:

                    pygame.mixer.init()
                    pygame.mixer.music.load(en_audio, "mp3")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        continue
                    en_mp3_name = ""




                if subtitle:

                    now_data = subtitles_hub.pop(0)
                    data_lines = now_data.splitlines()
                    updated_text = f"{data_lines[3]}\n{data_lines[4]}\n{text_update}\n{text_update}"


                    if len(data_lines[1]) > 2:
                        play_track = True

                        time_data = data_lines[0].strip().replace(':', '_')
                        print(time_data)
                        zeros = {
                                4: "00_0",
                                5: "00_",
                                7: "0"
                                }[len(time_data)]
                        en_mp3_name = zeros + time_data + f'_en_{en_speed}.mp3'
                        ru_mp3_name = zeros + time_data + f'_ru_{ru_speed}.mp3'

                        ru_audio = f"{folder}\\{ru_mp3_name}"
                        en_audio = f"{folder}\\{en_mp3_name}"

                        pygame.mixer.init()
                        pygame.mixer.music.load(ru_audio, "mp3")
                        pygame.mixer.music.set_volume(0.5)



                else:
                    updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"

                keyboard.send('space')



            elif subtitle:
                now_data = subtitles_hub.pop(0)
                data_lines = now_data.splitlines()
                updated_text = f"{data_lines[3]}\n{data_lines[4]}\n{text_update}\n{text_update}"

                if len(data_lines[1]) > 2:
                    play_track = True

                    time_data = data_lines[0].strip().replace(':', '_')
                    print(time_data)
                    zeros = {
                            4: "00_0",
                            5: "00_",
                            7: "0"
                            }[len(time_data)]
                    en_mp3_name = zeros + time_data + f'_en_{en_speed}.mp3'
                    ru_mp3_name = zeros + time_data + f'_ru_{ru_speed}.mp3'

                    ru_audio = f"{folder}\\{ru_mp3_name}"
                    en_audio = f"{folder}\\{en_mp3_name}"

                    pygame.mixer.init()
                    pygame.mixer.music.load(ru_audio, "mp3")
                    pygame.mixer.music.set_volume(0.5)
                time.sleep(0.1)
            else:
                updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"
                time.sleep(0.1)


        else:
            time.sleep(0.1)





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





if __name__ == '__main__':
    threading.Thread(target=parralel_player).start()
    # threading.Thread(target=top_black_frame).start()
    show_subtitle_text()

    pass
#   23 \ 47 \ 70 \ 94  / 117.5 / 112.5 / 141 / 188
#    50 \ 75 \ 100 \ 125  / 150   /  175 / 200
#   \24  \ 48 \ 72 \ 96 /  120 /   135  / 154

# 75   93.75  # 1.125
# 100  1.25   # 1.5
# 77   96.25  # 1.15