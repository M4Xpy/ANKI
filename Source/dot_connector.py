import time

import keyboard as keyboard
import pyperclip

from Source.tools import press_keys


def dot_connect():
    time.sleep(0.1)
    text = pyperclip.paste()
    lines = text.splitlines()
    keyboard.write(f"{lines[0]}\n{lines[1]}\n{lines[8]}\n{lines[3].rstrip(' .')}  {lines[-1].lstrip(' .')}\n{lines[4]}")
    for line in lines:
        print(line)
    print()
    keyboard.press('ctrl + c')






if __name__ == '__main__':
    while True:
        keyboard.wait("ctrl + x")
        dot_connect()
