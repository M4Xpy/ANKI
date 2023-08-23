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
        if parts[1].strip()[0].islower():
            return "I " + parts[1].strip('°\n™-=*~@#$%^&*()_+[]{}|/\>< ')
        return input_string.strip('°\n™-=*~@#$%^&*()_+[]{}|/\>< ').replace("|", "I")
    return input_string.strip('°\n™-=*~@#$%^&*()_+[]{}|/\>< ')


def read_from_screen_every_10_ms():
    """ """
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    ms = 0
    will_compare = 0
    prev_time_text = "!!!!!!!!!!!!!!!!!"
    prev_text = ""
    timing_start, timing_finish, subtitle = "5555", "99:00:00.000", ""
    time.sleep(5)
    keyboard.send('space')
    possible_start_from = (0.0, "99:00:00.000")
    begin = True
    while True:

        time.sleep(0.2)
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
                0: "000", 1: "053", 2: "105", 3: "158", 4: "211", 5: "263", 6: "315", 7: "368", 8: "421",
                9: "474", 10: "526", 11: "579", 12: "632", 13: "684", 14: "737", 15: "790", 16: "842", 17: "895",
                18: "947"
                }[ms] if ms < 19 else "999"
        if len(time_text) < 4:
            time_text = add_to_timing(timing_finish, 0.053)[1]
        if len(time_text) < 5:
            time_text = f"00:0{time_text}.{str_ms}"
        elif len(time_text) < 6:
            time_text = f"00:{time_text}.{str_ms}"
        elif len(time_text) < 8:
            time_text = f"0{time_text}.{str_ms}"

        if SequenceMatcher(None, text, subtitle).ratio() < 0.95:
            if not begin:
                # if len([char for char in text if char.isalpha()]) < 5:
                #     timing_finish = time_text
                with open(my_srt, "a", encoding="utf-8") as srt:
                    possible_start_to, start_timing = add_to_timing(timing_start, -1)
                    will_start = (start_timing, possible_start_from[1])[possible_start_from[0] > possible_start_to]
                    if prev_subtitle_end:
                        will_compare = add_to_timing(time_text)
                        will_end = (prev_subtitle_end[1], will_compare[1])[prev_subtitle_end[0] > will_compare[0]]
                        srt.write(f"{prev_will_start} --> {will_end}\n{prev_subtitle}\n\n")
                    prev_subtitle_end = add_to_timing(time_text, 1)
                    prev_will_start, prev_subtitle = will_start, subtitle

                    begin = True
                    possible_start_from = add_to_timing(time_text)[0], time_text

                    # print("with open")
            if len([char for char in text if char.isalpha()]) > 4:
                timing_start, timing_finish, subtitle = time_text, time_text, text
                begin = False
        else:
            timing_finish = time_text

        #
        #
        # print((time_text, text))
        # print()
        keyboard.send('space')


def add_to_timing(timing_start, add=0):
    possible_start_to = int(timing_start[:2]) * 3600 + (int(timing_start[3:5]) * 60) + float(timing_start[6:12]) + float(add)
    hour, possible_start_to = divmod(possible_start_to, 3600)
    min, possible_start_to = divmod(possible_start_to, 60)
    sec, msec = divmod(possible_start_to, 1)
    msec = str(msec)[2:5]
    start_timing = f"{int(hour):02}:{int(min):02}:{int(sec):02}.{msec:<03}"
    return possible_start_to, start_timing


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

# screenshot()
#
# print(extract_text_from_image(f'C:\\ANKIsentences\\foto\\0.015.png'))
# print(extract_text_from_image(f'C:\\ANKIsentences\\foto\\1.690.png'))
# print(extract_text_from_image(f'C:\\ANKIsentences\\foto\\1.962.png'))
# print(extract_text_from_image(f'C:\\ANKIsentences\\foto\\correct.png'))
# print(extract_text_from_image(f'C:\\ANKIsentences\\foto\\5f50cc8ba1301234189151.png'))
