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
# from pydub import AudioSegment


# def play_audio_with_speed(audio_path):
#     audio = AudioSegment.from_file(audio_path)
#     new_audio = audio.speedup(playback_speed=2)
#     modified_audio_path = "C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\mp3s_for_tests\\modified_audio.mp3"
#     new_audio.export(modified_audio_path, format="mp3")
#
#     playsound.playsound(modified_audio_path)
#
#     # Delete the modified audio file
#     os.remove(modified_audio_path)


new = '111111111111111111111'
old = '9999999999999999999999'


def extract_clear_text_with_thresholding():
    global old, new
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
            ).replace('|', 'I').splitlines() # strip(' .,_-|§—')
    text = ' '.join(line for line in text if len(line) > 4)
    if text and SequenceMatcher(None, old, text).ratio() < 0.8:  # and SequenceMatcher(None, new, text).ratio() < 0.8
        audio_file_path = 'C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\mp3s_for_tests\\temporary.mp3'
        translated = gTTS(text=Translator().translate(text, 'ru', 'en').text, lang='ru')
        keyboard.press('space')
        translated.save(audio_file_path)
        playsound.playsound(audio_file_path)
        os.remove(audio_file_path)
        old = text  # old, new = new, text
        print((text,))
        keyboard.press('space')

exceptions = ('mm SB HB oo. E\n\n- You got any kids?',)
if __name__ == '__main__':
    while True:
        extract_clear_text_with_thresholding()
