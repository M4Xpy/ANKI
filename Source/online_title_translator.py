import asyncio as asyncio
import os
from difflib import SequenceMatcher
import pymsgbox
import cv2
import keyboard as keyboard
import np as np
import pyautogui
import pygame
import pytesseract
from googletrans import Translator
from gtts import gTTS
import tkinter as tk
import threading

from Source.letter_visual_length import visual_len


def show_subtitle_text(text1, text2="", delay=0, position='+0+0', font=25) :

    max_len = max(visual_len(text1), visual_len(text2))
    indent = round((8907 - max_len) / 118) * " "
    font = (round((8907 / max_len) * 25), 25)[9262 > max_len]
    text = f'{indent}{text1}{333 * " "}\n{indent}{text2}{333 * " "}'

    # Function to close the window after a certain duration

    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(position)   # f'+{root.winfo_screenwidth() // 2}+100' == '+683+100'
    root.overrideredirect(True)  # Remove the window frame
    font = ('Arial', font)
    label = tk.Label(root, text=text, font=font, fg='white', bg='black')  # Set text color to white and background to black
    label.pack()
    root.after(delay, root.destroy)  # Schedule the window to close after 5 seconds (5000 milliseconds)
    root.mainloop()

def r_o_i(path):
    global image, x, y

    image = cv2.threshold(
        cv2.cvtColor(np.array(pyautogui.screenshot(region=(165, 570, 1050, 160))), cv2.COLOR_RGB2GRAY), 0, 255,
        cv2.THRESH_BINARY
        )[1]

    # Load the colored image
    image = cv2.imread(path)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply thresholding to obtain binary image
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # Apply image processing techniques to identify black-white sectors (e.g., contour detection)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Iterate over the identified contours and extract the regions of interest
    text = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        roi = image[y:y + h, x:x + w]

        # Perform OCR on the extracted region of interest using Pytesseract
        text.append(pytesseract.image_to_string(roi))
    return ' '.join(text)


old = 'aaaaaa'


async def text_not_old(text):
    return SequenceMatcher(None, old, text).ratio() < 0.5


async def translate_and_make_audio(text):
    translated = gTTS(text=Translator().translate(text, 'uk', 'en').text, lang='uk')
    translated.save("C:\\ANKIsentences\\temporary.mp3")
    # await asyncio.create_task(show_subtitle_text(text))



async def extract_clear_text_with_thresholding():
    global old
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    text = pytesseract.image_to_string(
            cv2.threshold(
                    cv2.cvtColor(np.array(pyautogui.screenshot(region=(165, 585, 1050, 160))), cv2.COLOR_RGB2GRAY), 0,
                    255,
                    cv2.THRESH_BINARY
                    )[1]
            ).splitlines()
    print(text)
    text = ' '.join(
            line.lstrip(
                    '°,.?!\n™1234567890-=*~@#$%^&*()—_+[]{}|/\>< '
                    ).rstrip(
                    '°\n™1234567890-=*~@#$%^&*()—_+[]{}|/\>< '
                    ).replace('|', 'I') for line in text if len(line) > 5
            )
    if text:
        if await asyncio.create_task(text_not_old(text)):
            keyboard.press('space')

            #await asyncio.create_task(pymsgbox.alert(text))
            await asyncio.create_task(translate_and_make_audio(text))
            pygame.mixer.init()
            pygame.mixer.music.load("C:\\ANKIsentences\\temporary.mp3")
            pygame.mixer.music.play()
            ttt = ' one two three four five six seven eight nine ten eleven twelve thirteen fourteen fiveteen '
            subtitle_thread = threading.Thread(target=show_subtitle_text, args=(text, 11111111))
            subtitle_thread.start()
            while pygame.mixer.music.get_busy():
                continue
            pygame.mixer.quit()
            os.remove("C:\\ANKIsentences\\temporary.mp3")
            old = text
            keyboard.press('space')
            print(text)
            print(888888888888888888888888888888888888888888888888888888888888888888888888888888888888888)





async def wait_for_space():
    keyboard.wait('space')


if __name__ == '__main__':



    while True:
        asyncio.run(extract_clear_text_with_thresholding())
