import threading
import time
import tkinter as tk

import keyboard
import mouse
import pyautogui
import pygame
import pyperclip

from Source.letter_visual_length import visual_len

now_speed = 2
file = f"C:\\Users\\Я\\Desktop\\films\\hercules\\hercules.txt"
text_update = f"{200 * ' '}\n{200 * ' '}"
updated_text = text_update

def online_player():
    global updated_text
    """ """
    with open(file, encoding='utf-8') as srt:
        text = srt.read()
        casts = [cast.splitlines() for cast in text.strip('\ufeff ').split('\n\n')]
        for index, cast in enumerate(casts):
            casts[index][1] = cast[1][:8].replace(':', '_') + '.mp3'
            if len(casts[0]) < 5:
                casts[index].append("")
    print(casts[0])
    _, audio, en_sentence, ru_sentence, mp3 = casts[0]
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.2)
    go_next = True
    prev_subtitle = ""
    # time.sleep(11)
    # keyboard.send('ctrl + a')
    time.sleep(0.2)
    keyboard.send('space')
    move = 1
    prev_time = time.time()

    play_track = False
    # score = 0
    # times = 0
    while 1:
        move *= -1
        mouse.move(move, move, absolute=False, duration=0.0001)
        keyboard.send('ctrl + c')

        text_lines = pyperclip.paste().splitlines()
        subtitle = " ".join(text_lines[2 if len(text_lines) < 6 else 7:])

        if prev_subtitle != subtitle:
            prev_subtitle = subtitle
            if play_track:
                play_track = False
                keyboard.press('space')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    continue
                pygame.mixer.quit()
                keyboard.press('space')

            if subtitle:

                max_len = max(visual_len(en_sentence), visual_len(ru_sentence))
                indent = round((10030 - max_len) / 118) * " "
                updated_text = f'{indent}{en_sentence}{indent}\n{indent}{ru_sentence}{indent}'

                if mp3:
                    audio = f"C:\\ANKIsentences\\films\\hercules\\{audio}"
                    pygame.mixer.init()
                    pygame.mixer.music.load(audio, "mp3")
                    pygame.mixer.music.set_volume(0.2)
                    play_track = True


                del casts[0]
                _, audio, en_sentence, ru_sentence, mp3 = casts[0]
            else:
                updated_text = text_update
                time.sleep(0.07)
        else:
            time.sleep(0.07)
            # keyboard.send('space')
            # show_subtitle_text(subtitle, delay=1111, position='+0+680', play_mode=False)
            # keyboard.send('space')
        # score += 1
        # now_time = time.time()
        # times += now_time - prev_time
        # print(times / score)
        # prev_time = now_time


def video_speed_change_to(speed=1):
    """ size 25 % """
    global now_speed
    if now_speed != speed:
        now_speed = speed
        pyautogui.moveTo(1350, 760)
        mouse.click('left')
        pyautogui.moveTo(1350, 750, 0.1)
        mouse.click('left')
        speed = {0.25: 680, 0.5: 690, 0.75: 700, 1: 710, 1.25: 720, 1.5: 730, 1.75: 740, 2.0: 750}[speed]
        pyautogui.moveTo(1350, speed, 0.1)
        mouse.click('left')
        time.sleep(0.1)
        keyboard.send('ctrl + a')


def show_subtitle_text(position='+0+0'):

    font = 25
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
