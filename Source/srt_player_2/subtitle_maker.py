import time

import keyboard
import mouse
import pyperclip

my_srt = "C:\\Users\\Я\\Desktop\\films\\hercules\\herculesSept21.txt"


def add_to_timing(timing_start, add=0):
    # """
    # >>> add_to_timing('0:35')
    # (35.0, '00:00:35.000')
    # """
    timing_start = timing_start.strip().split(":")
    timing_start = {
            0: (0, 0, 0),
            1: (0, 0, timing_start[0]),
            2: (0, timing_start[0], timing_start[-1]),
            3: timing_start
            }[len(timing_start)]
    seconds_amount = int(timing_start[-3]) * 3600 + (int(timing_start[-2]) * 60) + float(timing_start[-1]) + float(
            add
            )
    hour, possible_start_to = divmod(seconds_amount, 3600)
    min, possible_start_to = divmod(possible_start_to, 60)
    sec, msec = divmod(possible_start_to, 1)
    msec = str(msec)[2:5]
    start_timing = f"{int(hour):02}:{int(min):02}:{int(sec):02}.{msec:<03}"
    return seconds_amount, start_timing


def win():
    time.sleep(9)
    move = 1
    prev_time = 0
    prev_msec = time.time()
    now_msec = prev_msec
    subtitles = [['00:00:00.000', '00:00:00.000', 0], ]
    prev_subtitle = ""
    keyboard.send('space')
    time.sleep(0.2)
    keyboard.send('ctrl + a')
    time.sleep(0.2)
    _2 = 0
    while prev_time != '5:30':
        move *= -1
        mouse.move(move, move, absolute=False, duration=0.0000001)
        keyboard.send('ctrl + c')
        text_lines = pyperclip.paste().splitlines()
        subtitle = " ".join(text_lines[2 if len(text_lines) < 6 else 7:])
        try:
            subtitle_time = text_lines[1].split('/')[0]
        except IndexError:
            subtitle_time = '7777'

        if prev_time != subtitle_time:
            now_msec = time.time()
            prev_time = subtitle_time


        if prev_subtitle != subtitle:
            prev_subtitle = subtitle

            msec = (time.time() - now_msec) / 4
            _1, subtitle_time = add_to_timing(subtitle_time, add=msec)

            if not subtitles[-1][1]:
                _2, subtitles[-1][1] = _1, subtitle_time

            if subtitle:
                subtitles.append([subtitle_time, 0, subtitle, _1])
                diff = _1 - _2
                secs, subtitles[-2][1] = add_to_timing(str(_2), min((1, diff)))

                duration = secs - subtitles[-2][-1]
                with open(my_srt, "a", encoding="utf-8") as srt:
                    srt.write(f"{duration}\n{subtitles[-2][0]} --> {subtitles[-2][1]}\n{subtitles[-2][2]}\n\n")
                del subtitles[0]
        time.sleep(0.1)
    subtitles[-1][1] = add_to_timing(subtitles[-1][1], 1)[1]
    with open(my_srt, "a", encoding="utf-8") as srt:
        srt.write(f"{subtitles[-1][0]} --> {subtitles[-1][1]}\n{subtitles[-1][2]}")




# def render():
#     """
#     >>> render()
#     """
#     time.sleep(9)
#     win()

win()
# print(add_to_timing('00:01:06.803'))
