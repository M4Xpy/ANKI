from difflib import SequenceMatcher
import time
from difflib import SequenceMatcher

from googletrans import Translator
from gtts import gTTS


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time} seconds to execute.")

    return wrapper


old = 'aaaaaa'


def extract_text(input_string):
    print(input_string)
    start_index = -1
    end_index = -1

    # Find the index of the first capital letter
    for i, char in enumerate(input_string):
        if char.isupper():  # and input_string[-~i] in 'qwertyuioplkjhgfdsazxcvbnm ':
            start_index = i
            break

    # Find the index of the last dot, comma, or question mark
    for i, char in reversed(list(enumerate(input_string))):

        if char in (".", ",", "?"):  # and input_string[~-i].islower():
            end_index = i
            break

    # Extract the text based on the start and end indices
    if start_index != -1 and end_index != -1:
        return input_string[start_index:end_index + 1]


async def text_not_old(text):
    return SequenceMatcher(None, old, text).ratio() < 0.5


def translate_and_make_audio(text):
    translated = gTTS(text=Translator().translate(text, 'uk', 'en').text, lang='uk')
    translated.save("C:\\ANKIsentences\\temporary.mp3")


#
# @measure_execution_time
# def extract_clear_text_with_thresholding():
#     global old, new
#     pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe '
#     keyboard.press('space')
#     screenshot = pyautogui.screenshot()
#     width, height = screenshot.size
#     text = extract_text(pytesseract.image_to_string(
#             cv2.threshold(
#                     cv2.cvtColor(
#                             cv2.cvtColor(
#                                     np.array(screenshot.crop((0, 0, width, int(height * 0.95)))), cv2.COLOR_RGB2BGR
#                                     ),
#                             cv2.COLOR_BGR2GRAY
#                             ), 0, 250, cv2.THRESH_BINARY_INV
#                     )[1]
#             ))
#     # time.sleep(0.1)
#     keyboard.press('space')
#     print(text)


import pyautogui
import cv2
import numpy as np
import pytesseract


@measure_execution_time
def extract_text_from_screenshot():
    screenshot = pyautogui.screenshot(region=(165, 580, 1050, 160))
    screenshot.show()
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    text = pytesseract.image_to_string(
            cv2.threshold(
                cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY), 0, 255,
                cv2.THRESH_BINARY
                )[1]
            )

    print(text)


exceptions = ('mm SB HB oo. E\n\n- You got any kids?',)
if __name__ == '__main__':
    while True:
        # if keyboard.is_pressed('space'):
        extract_text_from_screenshot()


