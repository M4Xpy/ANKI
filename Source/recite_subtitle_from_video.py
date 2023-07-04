import os
import re
import time

import cv2
import keyboard as keyboard
import playsound
import pyautogui
import pytesseract
from googletrans import Translator
from gtts import gTTS

old = 'starrt'


def play_audio_from_text(text):
    global old
    if text and text != old:
        keyboard.press('space')
        audio: gTTS = gTTS(text=text, lang='ru', slow=False)  # Generate audio file
        audio_file_path = 'C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\mp3s_for_tests\\temporary.mp3'
        audio.save(audio_file_path)

        # Play the audio file
        playsound.playsound(audio_file_path)
        keyboard.press('space')
        # Delete the temporary file
        os.remove(audio_file_path)
        old = text


def make_screenshot():
    # Capture the entire screen
    screenshot = pyautogui.screenshot()

    # Get the dimensions of the screen
    width, height = screenshot.size

    # Calculate the coordinates for the bottom half
    top = height // 2
    bottom = height

    # Calculate the cropping dimensions
    left = int(width * 0.15)  # 15% of the width
    right = int(width * 0.85)  # 85% of the width

    # Crop the screenshot to the bottom half with reduced width
    cropped_screenshot = screenshot.crop((left, top, right, bottom))

    # Save the cropped screenshot
    cropped_screenshot.save(r'C:\Users\Я\Desktop\PythonProjectsFrom22_04_2023\ANKI\Source\img.png')


def text_from_image():
    # Путь для подключения tesseract
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    # Подключение фото
    img = cv2.imread('img.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Будет выведен весь текст с картинки
    config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=config, lang='eng')

    replaced_text: str = re.sub(r'[^a-zA-Z0-9!?.,\'":-]', ' ', text)
    print((replaced_text,) , end=' ')

    os.remove(r'C:\Users\Я\Desktop\PythonProjectsFrom22_04_2023\ANKI\Source\img.png')
    tranlsated = Translator().translate(replaced_text, 'ru', 'en').text
    print( (tranlsated,))
    return tranlsated


if __name__ == '__main__':
    time.sleep(10)
    while True:
        make_screenshot()
        play_audio_from_text(text_from_image())
