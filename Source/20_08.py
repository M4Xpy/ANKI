import os
import time

import mouse
import pyautogui
import pytesseract
from PIL import Image

from Source.tools import press_keys

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
region = 360, 0, 650, 100  # region=(top_left_X_horizont_coordinate=165, top_left_Y_coordinate=585, width=1050, height=160)
time_only = 190, 675, 350, 50

_125_100_down = 60, 665, 950, 110

my_srt = "C:\\Users\\Я\\Desktop\\films\\hatico\\haticoAug20.txt"


def make_folder(subfolder, sub_count=1, minutes=0):
    if minutes:
        sub_count = 1500 * minutes

    sub_count += 1
    count = 1
    while sub_count > count:
        try:
            os.mkdir(os.path.join(os.getcwd(), f"C:\\ANKIsentences\\foto\\{subfolder}\\{count:>09}"))
        except FileExistsError:
            print(f"Folder '{count}' already exists.")
        except Exception as e:
            print(f"An error occurred: {e}")
        count += 1


def text_from_screenshot():
    """ """
    number = 1
    order = 25
    now_text = ""
    cycle = 0
    subtitles = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], ]
    while True:  # subtitles[-1][3] < 39781:  # 5400000:
        if order == 25:
            time, text = text_data_from_screenshot("hatico2", number)
            if text != now_text:
                # print(number, "_25_55555_", (file_in_folder, text))
                number -= 24
                order = 5
            else:
                # print(number, "_25_25_", (file_in_folder, text))
                number += 25
        if order == 5:
            cycle += 1
            time, text = text_data_from_screenshot("hatico2", number)
            if text != now_text or cycle > 4:
                # print(number, "555555_111111111111", (file_in_folder, text))
                number -= 4
                order = 1
                cycle = 0
            else:
                # print(number, "555555", (file_in_folder, text))
                number += 5
        if order == 1:
            time, text = text_data_from_screenshot("hatico2", number)
            if text != now_text:
                if text:
                    if time == 0:
                        subtitles[-1][
                            1] = time
                    subtitles.append(
                            [time,
                             "00:00:00.000", text, int(file_in_folder[:9])]
                            )

                    print(subtitles)
                    print()

                    order = 25
                    number += 25
                    with open(my_srt, "a", encoding="utf-8") as srt:
                        srt.write(
                                f"{subtitles[-2][3]}\n{subtitles[-2][0]} --> {subtitles[-2][1]}\n{subtitles[-2][2]}\n\n"
                                )
                    del subtitles[0]
                else:
                    subtitles[-1][
                        1] = add_to_timing(file_in_folder)
                    print(subtitles)
                    print()
                    order = 25
                    number += 25
                now_text = text


            else:
                # print(number, 111111111, (file_in_folder, text))
                number += 1

    with open(my_srt, "a", encoding="utf-8") as srt:
        srt.write(f"{subtitles[-1][3]}\n{subtitles[-1][0]} --> {subtitles[-1][1]}\n{subtitles[-1][2]}\n\n")


def add_to_timing(timing_start, add=0):
    """
    >>> add_to_timing('0:35')
    (35.0, '00:00:35.000')
    """
    timing_start = timing_start.split(":")
    timing_start = {
            0: (0, 0, 0),
            1: (0, 0, timing_start),
            2: (0, timing_start[-2], timing_start[-1]),
            3: timing_start
            }[len(timing_start)]
    possible_start_to = int(timing_start[-3]) * 3600 + (int(timing_start[-2]) * 60) + float(timing_start[-1]) + float(
            add
            )
    hour, possible_start_to = divmod(possible_start_to, 3600)
    min, possible_start_to = divmod(possible_start_to, 60)
    sec, msec = divmod(possible_start_to, 1)
    msec = str(msec)[2:5]
    start_timing = f"{int(hour):02}:{int(min):02}:{int(sec):02}.{msec:<03}"
    return possible_start_to, start_timing


def text_data_from_screenshot(folder, number):
    return screenshot_text_sorter(
            pytesseract.image_to_string(
                    Image.open(
                            f"C:\\ANKIsentences\\foto\\{folder}\\{number:>09}.png"
                            )
                    )
            )


def screenshot_text_sorter(text):
    """
    text = "So even if Columbus got lost and\n\n0:35 / 1:33:14 wasn't the first to discover America,\n"
    >>> screenshot_text_sorter(text)
    """
    subtitle = ""
    time = 0
    for line in text.replace("|", "I").splitlines():
        if "1:33:14" in line:
            for sub_line in line.split(" / 1:33:14"):
                if all(char in ":01234567890 " for char in sub_line):
                    time = add_to_timing(sub_line.strip())[0]
                else:
                    subtitle = f"{subtitle.strip()} {sub_line.strip()}"
        else:
            subtitle = f"{subtitle.strip()} {line.strip()}"
    return time, subtitle


#     if "|" in input_string:
#         parts = input_string.split("|", 1)
#         if parts[1].strip()[0].islower():
#             return "I " + parts[1].strip('°\n™-=*~@#$%^&*()_+[]{}|/\>< ')
#         return input_string.strip('°\n™-=*~@#$%^&*()_+[]{}|/\>< ').replace("|", "I")
#     return input_string.strip('°\n™-=*~@#$%^&*()_+[]{}|/\>< ')


def screenshot(folder, reg=region):
    time.sleep(0)
    press_keys('space')
    press_keys(0.3, 'space', 0.3, 'left', 0.3, 'space')
    my_time = time.time()
    end_time = my_time + 21600
    next_time = time.time()
    number = 0
    while 1:
        # while time.time() < next_time:
        #     pass
        # next_time += 0.1
        number += 1

        pyautogui.screenshot(region=reg).convert("L").point(lambda colour: 0 if colour < 200 else 255).save(
                f"C:\\ANKIsentences\\foto\\{folder}\\{number:>09}\\{round((time.time() - my_time) * 250):>09}.png"
                )


def timer():
    my_time = time.time()

    while True:
        time.sleep(0.1)
        print(f"{round((time.time() - my_time) * 1000):>09}")


def preprocess_and_ocr():
    # Load the black and white image
    image = Image.open(f"C:\\ANKIsentences\\foto\\hatico\\000002273\\000038535.png")  # Convert to grayscale

    # Convert gray areas to white and black areas to black
    binary_image = Image.open(f"C:\\ANKIsentences\\foto\\hatico\\000002273\\000038535.png").point(
            lambda p: 0 if p < 222 else 255
            )

    # Perform OCR on the binary image
    text = pytesseract.image_to_string(binary_image).replace("\n", ""), pytesseract.image_to_string(image).replace(
            "\n", ""
            )

    return text


def screenshot333(folder, reg=region):
    time.sleep(20)
    press_keys('space')
    number = 0
    move = 1
    while True:
        number += 1
        pyautogui.screenshot(region=reg).convert("L").point(lambda colour: 0 if colour < 200 else 255).save(
                f"C:\\ANKIsentences\\foto\\{folder}\\{number:>09}.png"
                )
        move *= -1
        mouse.move(move, move, absolute=False, duration=0.0000001)


# def rename_with_ms():



def render():
    """
    >>> render()
    """
    # print(preprocess_and_ocr())
    # text_from_screenshot()
    # screenshot('test', _125_100_down)
    # make_folder("test", minutes=2)
    # print(ffffffffff("test", 1))

    # screenshot333('hatico2', _125_100_down)

    print((text_data_from_screenshot("hatico2", 1),))

# 133,  117, 100,  83  , 67 , 50, 33, 17
# 999, 959, 961           925
# 21  19
