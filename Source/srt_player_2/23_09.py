import tkinter as tk

from Source.letter_visual_length import visual_len
import tkinter as tk

from Source.letter_visual_length import visual_len

vaiable_flag = True

import threading
import time

updated_text = " " * 165
ru_title = "2"


def top_black_frame():
    top_message = "                                                             "
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry('+0+0')
    root.overrideredirect(True)  # Remove the window frame
    font = ('Arial', 63)
    label = tk.Label(
            root, text=top_message, font=font, fg='white', bg='black'
            )  # Set text color to white and background to black
    label.pack()
    label.config(text=top_message)
    root.mainloop()




def ttt():
    global updated_text
    count = 1
    while 1:
        time.sleep(0.1)



        text = ' ' * count
        max_len = max(visual_len(text), visual_len(text))
        indent = round((10100 - max_len) / 118) * "1"
        updated_text = f'{indent}{text}{indent}\n{indent}{text}{indent}'
        ru_title = "4444444444"
        count += 1


if __name__ == '__main__':
    threading.Thread(target=ttt).start()
    threading.Thread(target=top_black_frame).start()
