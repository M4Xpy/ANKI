import os
import time

import keyboard


def add_prefix_to_files(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            new_filename = f'{filename.replace("(", "").replace(")", "")}'
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))


# Example usage
folder_path = f"C:\\ANKIsentences\\triples_audio\\15\\10"


def lazy_mouse():
    while True:
        keyboard.press('down')
        time.sleep(10)
