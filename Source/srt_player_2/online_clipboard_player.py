import time

import keyboard
import mouse
import pyautogui
import pyperclip

from Source.srt_player_2.srt_player_2 import show_subtitle_text

now_speed = 2


def online_player():
    """ """

    prev_subtitle = ""
    # time.sleep(11)
    # keyboard.send('ctrl + a')
    time.sleep(0.2)
    keyboard.send('space')
    move = 1
    # prev_time = time.time()
    # score = 0
    # times = 0
    while 1:
        move *= -1
        mouse.move(move, move, absolute=False, duration=0.0001)
        keyboard.send('ctrl + c')
        text_lines = pyperclip.paste().splitlines()
        # subtitle = " ".join(text_lines[2 if len(text_lines) < 5 else 6:])
        subtitle = ' '.join(text_lines[2:])
        time.sleep(0.1)
        if prev_subtitle != subtitle and subtitle:
            prev_subtitle = subtitle
            keyboard.send('space')
            show_subtitle_text(subtitle, delay=1111, position='+0+680', play_mode=False)
            keyboard.send('space')
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


online_player()
