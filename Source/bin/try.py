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






def show_subtitle_text(text):
    # Function to close the window after a certain duration
    def close_window():
        root.destroy()

    root = tk.Tk()
    #root.title(text)  # Create the main window
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.overrideredirect(True)  # Remove the window frame

    # # Get screen dimensions
    # screen_width = root.winfo_screenwidth()
    # screen_height = root.winfo_screenheight()

    font = ('Arial', 25)
    label = tk.Label(root, text=text, font=font)
    label.pack()

    # # Calculate the desired position for the window
    # x = (screen_width - 10  * len(text)) // 2  # screen_width 1366
    # y = screen_height - root.winfo_reqheight()
    #
    # root.geometry(f'+{0}-{99}')  # Set the position of the window
    root.after(99 * len(text), close_window)  # Schedule the window to close after 5 seconds (5000 milliseconds)
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
            show_subtitle_text(text)
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
