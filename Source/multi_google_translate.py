import random
import time
import webbrowser

import keyboard as keyboard
import mouse as mouse
import pyperclip

from Source.tools import press_keys, detect_language

old_res = "88888888888888888888888888888888888888888"

old_list = ['вам', 'вами', 'вас', 'вы', 'тебе', 'тебя', 'тобой', 'ты']
count = 22
def time_measure(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Execution time of '{func.__name__}': {elapsed_time:.6f} seconds")
        return result

    return wrapper


def get_screen_data():
    result = ""
    while "help_outline" not in result:
        press_keys(0.05, 'tab', 0.05, 'ctrl + a', 0.05, 'ctrl + c', 0.05)
        result = pyperclip.paste()
    press_keys(0.01, 'ctrl + w')
    return result


@time_measure
def get_all_multi_translations(word):
    webbrowser.open(f'https://translate.google.com/?sl=en&tl=ru&text={word}%0A&op=translate')
    return set(
            word for word in get_screen_data().split('help_outline')[1].splitlines()[2:-2]
            if detect_language(word) == 'ru' and word.islower()
            )


# @time_measure
def sss(word):
    global old_res, resss, old_list,count

    press_keys(0.1, 'ctrl + a', 0.1)
    for leter in word:
        keyboard.write(leter.lower())
        time.sleep(random.randint(5, 15) / 500)
    mouse.move(5, 275, absolute=True, duration=0.9)
    mouse.click('left')
    press_keys(0.9, 'tab', 0.9, 'ctrl + a', 0.9)
    #
    # resss = "*********************************************"
    #
    # while resss != old_res:
    #     old_res = resss
    #     press_keys(0.1, 'ctrl + c', 0.1)
    #     resss = pyperclip.paste()
    many = super_set()


    # while any((set(old_list) >= set(many) , any('.' in _ for _ in many))) and count :
    #
    #     print(word, many)
    #     count -= 1
    #     many = super_set()

    old_list = sorted(many)
    mouse.move(200, 275, absolute=True, duration=0.1)
    mouse.click('left')
    time.sleep(0.1)
    return list(many)


def super_set():
    press_keys(0.9, 'ctrl + c', 0.9)
    result = pyperclip.paste()
    many = set()
    if 'help_outline' in result:
        many = set(
                word for word in result.split('help_outline')[1].splitlines()[2:-2] if
                detect_language(word) == 'en' and word.islower()
                )
    result = result.splitlines()
    for index, line in enumerate(result):
        if "5 000" in line and "Результаты перевода" in result[index + 1] and 'Перевод' in result[index + 2]:
            many.add(result[index + 3].lower())
    return many


if __name__ == '__main__':
    time.sleep(0.9)
    for word in "or may require additional permissions to simulate mouse events on the screen".split():
        print(word, sss(word))

