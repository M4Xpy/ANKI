import os
from difflib import SequenceMatcher

import cv2
import keyboard as keyboard
import np as np
import playsound
import pyautogui
import pytesseract
from googletrans import Translator
from gtts import gTTS

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def extract_clear_text_with_thresholding():
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    screenshot = pyautogui.screenshot()

    # Get the dimensions of the screen
    width, height = screenshot.size

    return pytesseract.image_to_string(
            cv2.threshold(
                cv2.cvtColor(
                    cv2.cvtColor(np.array(screenshot.crop((0, 0, width, int(height * 0.95)))), cv2.COLOR_RGB2BGR),
                    cv2.COLOR_BGR2GRAY
                    ), 0, 255, cv2.THRESH_BINARY_INV
                )[1]
            ).replace('|', 'I').replace('...', '.').replace('..', '.').replace('\n', ' ')


# def extract_clear_text_with_thresholding():
#     pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#     return pytesseract.image_to_string(
#             cv2.threshold(
#                     cv2.cvtColor(cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2GRAY),
#                     0, 255,
#                     cv2.THRESH_BINARY_INV
#                     )[1]
#             ).replace('|', 'I').replace('...', '.').replace('..', '.')    #.replace('\n', ' ')


new = '111111111111111111111'
old = '9999999999999999999999'


def play_audio_from_text(text=''):
    audio: gTTS = gTTS(text=text, lang='ru', slow=False)  # Generate audio file
    audio_file_path = 'C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\mp3s_for_tests\\temporary.mp3'
    audio.save(audio_file_path)

    # Play the audio file
    playsound.playsound(audio_file_path)
    keyboard.press('space')
    # Delete the temporary file
    os.remove(audio_file_path)


def make_screenshot():
    # Capture the entire screen
    screenshot = pyautogui.screenshot()

    # Get the dimensions of the screen
    width, height = screenshot.size

    # Calculate the coordinates for the bottom half
    top = height // 2
    bottom = height - 30

    # Calculate the cropping dimensions
    left = int(width * 0.11)  # 15% of the width
    right = int(width * 0.89)  # 85% of the width

    # Crop the screenshot to the bottom half with reduced width
    cropped_screenshot = screenshot.crop((left, top, right, bottom))

    # Save the cropped screenshot
    cropped_screenshot.save(r'C:\Users\Я\Desktop\PythonProjectsFrom22_04_2023\ANKI\Source\img.png')


# def text_from_image():
#     # Путь для подключения tesseract
#     pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#     # Подключение фото
#     img = cv2.imread('img.png')
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # Будет выведен весь текст с картинки
#     config = r'--oem 3 --psm 6'
#     text = pytesseract.image_to_string(img, config=config, lang='eng')
#
#     replaced_text: str = re.sub(r'[^a-zA-Z0-9!?.,\'":-]', ' ', text)
#     print((replaced_text,) , end=' ')
#
#     os.remove(r'C:\Users\Я\Desktop\PythonProjectsFrom22_04_2023\ANKI\Source\img.png')
#     tranlsated = Translator().translate(replaced_text, 'ru', 'en').text
#     print( (tranlsated,))
#     return tranlsated


def text_from_image():
    global old, new
    # Путь для подключения tesseract
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    # Подключение фото
    # img = cv2.imread('img.png')
    # img = cv2.cvtColor('img.png', cv2.COLOR_BGR2GRAY)

    text = extract_clear_text_with_thresholding()
    if text and similar(old, text) < 0.8 and similar(new, text) < 0.8:
        keyboard.press('space')

        tranlsated = Translator().translate(text, 'ru', 'en').text

        play_audio_from_text(tranlsated)
        print(old)
        print(new)
        print(text)

        old, new = new, text
        print('********************************')


if __name__ == '__main__':
    while True:
        # keyboard.press('space')
        # x = extract_clear_text_with_thresholding()
        # keyboard.press('space')
        # print(x)


        text_from_image()
