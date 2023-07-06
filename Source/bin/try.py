import asyncio as asyncio
import os
from difflib import SequenceMatcher

import cv2
import keyboard as keyboard
import np as np
import pyautogui
import pygame
import pytesseract
from googletrans import Translator
from gtts import gTTS

# from pydub import AudioSegment
# from pydub.playback import play
#
#
# def play_audio_with_adjustments(audio_path, speed_factor, volume_adjustment):
#     # Load the audio file
#     audio = AudioSegment.from_file(audio_path)
#
#     # Adjust the speed
#     modified_audio = audio.speedup(playback_speed=speed_factor)
#
#     # Adjust the volume
#     modified_audio = modified_audio + volume_adjustment
#
#     # Play the modified audio
#     play(modified_audio)


new = '111111111111111111111'
old = '9999999999999999999999'


async def text_not_old(text):
    return text and SequenceMatcher(None, old, text).ratio() < 0.5


async def translate_and_make_audio(text):
    translated = gTTS(text=Translator().translate(text, 'uk', 'en').text, lang='uk')
    translated.save("C:\\ANKIsentences\\temporary.mp3")


async def extract_clear_text_with_thresholding():
    global old, new
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe '
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
            ).splitlines()
    text = ' '.join(line.replace('|', 'I') for line in text if len(line.replace(' .,_-|\'§—012345678"9=+*/°[]()~@#', '')) > 9)
    if await asyncio.create_task(text_not_old(text)):  # and SequenceMatcher(None, new, text).ratio() < 0.8
        keyboard.press('space')
        await asyncio.create_task(translate_and_make_audio(text))
        pygame.mixer.init()
        pygame.mixer.music.load("C:\\ANKIsentences\\temporary.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.mixer.quit()
        os.remove("C:\\ANKIsentences\\temporary.mp3")
        old = text
        keyboard.press('space')
        print(text)


exceptions = ('mm SB HB oo. E\n\n- You got any kids?',)
if __name__ == '__main__':
    while True:
        asyncio.run(extract_clear_text_with_thresholding())
