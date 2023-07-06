import os
import re
from difflib import SequenceMatcher

import cv2
import keyboard as keyboard
import np as np
import playsound
import pyautogui
import pytesseract
from googletrans import Translator
from gtts import gTTS

old = 'aaaa'


def extract_clear_text_with_thresholding():
    global old
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    screenshot = pyautogui.screenshot()
    width, height = screenshot.size
    text = pytesseract.image_to_string(
            cv2.threshold(
                    cv2.cvtColor(
                            cv2.cvtColor(
                                    np.array(screenshot.crop((0, 0, width, int(height * 0.95)))), cv2.COLOR_RGB2BGR
                                    ),
                            cv2.COLOR_BGR2GRAY
                            ), 0, 255, cv2.THRESH_BINARY_INV
                    )[1]
            ).replace('|', 'I').splitlines()
    text = ' '.join(line for line in text if len(re.sub('[^A-z]', '', '_ rT . i -')) > 4)
    if text and SequenceMatcher(None, old, text).ratio() < 0.8:
        gTTS(text=Translator().translate(text, 'ru', 'en').text, lang='ru').save("C:\\ANKIsentences\\temporary.mp3")
        keyboard.press('space')
        playsound.playsound("C:\\ANKIsentences\\temporary.mp3", block=True)
        keyboard.press('space')
        os.remove("C:\\ANKIsentences\\temporary.mp3")
        old = text
        print((text,))


exceptions = ('mm SB HB oo. E\n\n- You got any kids?',)
if __name__ == '__main__':
    while True:
        extract_clear_text_with_thresholding()
