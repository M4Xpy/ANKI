import time
from difflib import SequenceMatcher

import cv2
import keyboard as keyboard
import np as np
import pyautogui
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
region = 333, 0, 700, 140  # region=(top_left_X_horizont_coordinate=165, top_left_Y_coordinate=585, width=1050, height=160)
old_time_only = 120, 716, 200, 25
time_only = 190, 675, 350, 50
my_srt = "C:\\Users\\Я\\Desktop\\films\\hatico\\haticoAug17.txt"
prev_text = ""

def read_from_screen():
    """ """
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    return pytesseract.image_to_string(
            cv2.threshold(
                    cv2.cvtColor(np.array(pyautogui.screenshot(region=region)), cv2.COLOR_RGB2GRAY), 0,
                    255,
                    cv2.THRESH_BINARY
                    )[1]
            )  # region=(top_left_X_horizont_coordinate=165, top_left_Y_coordinate=585, width=1050, height=160)


def screenshot():
    start_time = time.time()
    stop_time = time.time() + 500
    while stop_time > time.time():
        pyautogui.screenshot(region=region).save(
                f"C:\\ANKIsentences\\foto\\{f'{(time.time() - start_time) / 4:.3f}'}.png"
                )
        time.sleep(1)


def transform_string(input_string):
    if "|" in input_string:
        parts = input_string.split("|", 1)

        try:
            if parts[1].strip()[0].islower():
                return "I " + parts[1].strip('°\n™-=*~@#$%^&*()_+[]{}|/\>< ')
        except:
            return input_string.strip('°\n™-=*~@#$%^&*()_+[]{}|/\>< ').replace("|", "I")
    return input_string.strip('°\n™-=*~@#$%^&*()_+[]{}|/\>< ')


def read_from_screen_every_10_ms():
    """ """
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    ms = 0
    will_compare = 0
    prev_time_text = "!!!!!!!!!!!!!!!!!"

    timing_start = "99:00:00.000"
    time.sleep(5)
    keyboard.send('space')
    float_possible_start_from, str_possible_start_from = (0.0, "99:00:00.000")
    begin = True
    prev_subtitle_end = None
    process = 0
    str_subtitle_start, float_subtitle_start, str_subtitle_finish, float_subtitle_finish = \
        "99:00:00.000", 99999999.9, "88:00:00.000", 88888888.8
    next_subtitle = "next_subtitle_next_subtitle_next_subtitle"
    subtitle = "subtitle_subtitle_subtitle"
    float_now_time = 0.0

    str_start_current, float_start_current = "99:00:00.000", 99999999.9
    str_end_prior, float_end_prior = "00:00:00.000", 0.0
    str_end_current, float_end_current = "99:00:00.000", 99999999.9
    str_end_current, float_end_current = None, None
    str_be_end_prior, float_be_end_prior = None, None
    timing_finish = "00:00:00.777"
    str_first_subtitle_1, float_first_subtitle_1 = None, None
    str_last_subtitle_1, float_last_subtitle_1   = None, None

    while True:

        time.sleep(0.25)
        keyboard.send('space')

        text = pytesseract.image_to_string(
                cv2.threshold(
                        cv2.cvtColor(np.array(pyautogui.screenshot(region=region)), cv2.COLOR_RGB2GRAY),
                        0,
                        255,
                        cv2.THRESH_BINARY
                        )[1]
                ).splitlines()

        text = " ".join(transform_string(line) for line in text)

        time_text = pytesseract.image_to_string(
                cv2.cvtColor(np.array(pyautogui.screenshot(region=time_only)), cv2.COLOR_BGR2GRAY)
                ).split("1:33:14")[0].strip('°\n™-=*~@#$%^&*()_+[]{}|/\>< ')

        if prev_time_text != time_text:
            prev_time_text = time_text
            ms = -1
        ms += 1
        str_ms = {
                0: "000", 1: "063", 2: "125", 3: "188", 4: "250", 5: "313", 6: "375", 7: "438", 8: "500",
                9: "563", 10: "625", 11: "688", 12: "750", 13: "813", 14: "875", 15: "938"
                }[ms] if ms < 15 else "999"
        time_text = {
                0: add_to_timing(timing_finish, 0.063)[0],
                1: add_to_timing(timing_finish, 0.063)[0],
                2: add_to_timing(timing_finish, 0.063)[0],
                3: add_to_timing(timing_finish, 0.063)[0],
                4: f"00:0{time_text}.{str_ms}",
                5: f"00:{time_text}.{str_ms}",
                6: f"00:{time_text}.{str_ms}",
                7: f"00:{time_text}.{str_ms}",
                }[len(time_text)]

        timing_finish = time_text
        if another_subtitle_in_(text):
            if not_empty_(text):
                print(f"{time_text = } , {text = } , {str_first_subtitle_1 = } , {str_last_subtitle_1 = } \n\n")
                if float_last_subtitle_1:
                    str_first_subtitle_2, float_str_first_subtitle_2 = add_to_timing(time_text)
                    float_differ = float_str_first_subtitle_2 - float_last_subtitle_1
                    if float_differ < 2:
                        float_differ = float_last_subtitle_1 + float_differ / 2
                        str_last_subtitle_1, float_last_subtitle_1 = add_to_timing(possible_start_to=float_differ)
                        with open(my_srt, "a", encoding="utf-8") as srt:
                            srt.write(f"{str_first_subtitle_1} --> {str_last_subtitle_1}\n{subtitle}\n\n")
                            str_first_subtitle_1, float_first_subtitle_1 = str_last_subtitle_1, float_last_subtitle_1
                    else:
                        str_last_subtitle_1, float_last_subtitle_1 = add_to_timing(str_last_subtitle_1, 1)
                        str_first_subtitle_1, float_first_subtitle_1 = add_to_timing(str_first_subtitle_1, -1)
                        with open(my_srt, "a", encoding="utf-8") as srt:
                            srt.write(f"{str_first_subtitle_1} --> {str_last_subtitle_1}\n{subtitle}\n\n")
                            str_first_subtitle_1, float_first_subtitle_1 = add_to_timing(time_text)


                elif float_first_subtitle_1:
                    str_last_subtitle_1, float_last_subtitle_1 = add_to_timing(time_text)
                    with open(my_srt, "a", encoding="utf-8") as srt:
                        srt.write(f"{str_first_subtitle_1} --> {str_last_subtitle_1}\n{subtitle}\n\n")
                    str_first_subtitle_1, float_str_first_subtitle_1 = str_last_subtitle_1, float_last_subtitle_1

                elif not float_first_subtitle_1:
                    str_first_subtitle_1, float_first_subtitle_1 = add_to_timing(time_text, -1)

                subtitle = text
                str_last_subtitle_1, float_last_subtitle_1 = None, None

            else:
                str_last_subtitle_1, float_last_subtitle_1 = add_to_timing(time_text)
        if time_text[:8] == "01:33:14":
            subtitle_start = (str_subtitle_finish, str_subtitle_start)[
                float_subtitle_start < float_subtitle_finish]
            subtitle_end = (str_subtitle_finish, time_text)[float_now_time > float_subtitle_finish]
            with open(my_srt, "a", encoding="utf-8") as srt:
                srt.write(f"{subtitle_start} --> {subtitle_end}\n{subtitle}\n\n")


        keyboard.send('space')

def another_subtitle_in_(text):
    global prev_text
    compare, prev_text = prev_text, text
    return SequenceMatcher(None, text, compare).ratio() < 0.95



def not_empty_(text):
    return len([char for char in text if char.isalpha()]) > 4


def add_to_timing(timing_start="00:00:00.000", add=0, possible_start_to=None):
    if not possible_start_to:
        possible_start_to = int(timing_start[:2]) * 3600 + (int(timing_start[3:5]) * 60) + float(
                timing_start[6:12]
                ) + float(add)

    hour, possible_start_to = divmod(possible_start_to, 3600)
    min, possible_start_to = divmod(possible_start_to, 60)
    sec, msec = divmod(possible_start_to, 1)
    msec = str(msec)[2:5]
    start_timing = f"{int(hour):02}:{int(min):02}:{int(sec):02}.{msec:<03}"
    return start_timing, possible_start_to


def extract_text_from_image(image_path):
    try:
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Convert to binary image using thresholding
        _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

        extracted_text = pytesseract.image_to_string(binary_image)
        return extracted_text
    except Exception as e:
        return str(e)


read_from_screen_every_10_ms()
