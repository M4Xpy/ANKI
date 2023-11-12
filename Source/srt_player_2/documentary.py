import re
import threading
import time
import tkinter as tk

import keyboard
import mouse
import pygame
import pyperclip
from googletrans import Translator
from gtts import gTTS

from tests.exceptions.top_words import top_300, top_2000, top_5000

last_subtitle = ""
prelast_subtitle = ""
text_update = 170 * " "
updated_text = f"{text_update}\n{text_update}\n{text_update}\n " * 8
mp3_ru_audio = False
mp3_en_audio = False
play_track = False
keyboard_send_space = False
str_hub = " "
past_subtitles = "  "
delayed_text = ""
vol = 1
send_space = 0
press_space = 0
time_space = time.time() + 0.25
time_m = time_space
ad_skip = 0


def play_without_ecxeptions(text, extra_exceptions="", exceptions="*♪¤¶"):
    return "".join(sign for sign in text if sign not in f"{exceptions}{extra_exceptions}")



def keyboard_send(message, loop):
    keyboard.send(message)
    start = time.time() + loop
    while True:
        if start < time.time():
            start += loop + 0.2
            keyboard.send(message)
            time.sleep(0.2)
            keyboard.send(message)

def top_hub():
    # """
    # >>> top_hub()
    # """
    global str_hub
    file = "C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\tests\\exceptions\\top_hub.txt"
    with open(file, encoding='utf-8') as words:
        str_hub = words.read()


def en_ru_corrector(text, lang="en"):
    # """
    # >>> en_ru_corrector("l'm gоnnа rummаgе in thе stоrаgе сlоsеt")
    # """
    russian_to_english = {
            'А': 'A', 'В': 'B', 'С': 'C', 'Е': 'E', 'Н': 'H',
            'К': 'K', 'М': 'M', 'О': 'O', 'Р': 'P', 'Т': 'T',
            'Х': 'X', 'а': 'a', 'с': 'c', 'е': 'e', 'о': 'o',
            'р': 'p', 'х': 'x', 'у': 'y', 'к': 'k'
            }  # russian : english

    for russian, english in russian_to_english.items():
        if lang == "en":
            text = text.replace(russian, english)
        elif lang == "ru":
            text = text.replace(english, russian)
    return text


def volume(text):
    global vol, time_m
    if text and vol:
        while time.time() < time_m:
            pass
        time_m = time.time() + 0.25
        keyboard.send("m")
        vol = 0
    elif not text and not vol:
        vol = 1
        while time.time() < time_m:
            pass
        time_m = time.time() + 0.25
        keyboard.send("m")



def mouse_move():
    move = 1
    while True:
        move *= -1
        mouse.move(move, move, absolute=False, duration=0.1)

def online_player():
    global ad_skip, next_video_time, time_space, press_space, updated_text, mp3_ru_audio, mp3_en_audio, play_track, different, to_play_subtitle, translated, waite, keyboard_send_space, delayed_text, send_space

    waite = False
    pyperclip.copy("")
    prev_subtitle = ""
    keyboard.send('ctrl + a')
    time.sleep(0.3)
    keyboard.send('space')

    next_video_time = time.time() + 550
    keyboard.send("f10")


    time.sleep(0.3)
    move = 1
    play_track = False
    start_time = 0
    pause = 0
    no_title = 0
    while True:
        move *= -1
        mouse.move(move, move, absolute=False, duration=0.0001)
        keyboard.send('ctrl + c')

        subtitle_lines = " ".join(
                [
                        line for line in pyperclip.paste().splitlines()
                        if not
                        any(word in line for word in ["Качество", "Звук", "Субтитры", "Скорость", "Масштаб", '0:00/ 0:00', "/ 2:", "/ 1:", "/ 3:"]) and line
                        ]
                )
        if "Пропустить" in subtitle_lines:
            if not ad_skip:
                keyboard.send('y')
                ad_skip = 1
            time.sleep(0.1)
            continue
        if ad_skip and subtitle_lines.strip():
            time.sleep(0.1)
            ad_skip = 0
            keyboard.send('y')


        if not send_space and not subtitle_lines.strip():
            check_whether_next_video("f10", 550)

        if prev_subtitle != subtitle_lines:


            prev_subtitle = subtitle_lines
            subtitle = en_ru_corrector(subtitle_lines, "en")

            if subtitle:
                if send_space:

                    check_time_and_send_space()
                    press_space = 1
                    while send_space:
                        pass

                start_time = time_delay(pause, start_time, subtitle)
                threading.Thread(
                                target=execute, args=(subtitle,)
                                ).start()

            else:
                no_title += 1
                empty_text(no_title)
        else:
            no_title += 1
            empty_text(no_title)




def check_time_and_send_space():
    global time_space
    while time.time() < time_space:
        pass
    time_space = time.time() + 0.25
    keyboard.send("space")


def execute(subtitle):
    global to_play_subtitle, different, updated_text, send_space, press_space, time_space, next_video_time

    send_space = 1
    en_subtitle = subtitle

    subtitle, to_play_subtitle, different = no_repit(en_subtitle)

    ru_subtitle = Translator().translate(subtitle.lower().replace(".", ","), 'ru', 'en').text


    xxx = "\n".join(updated_text.splitlines()[6:])


    updated_text = f'{xxx}{subtitle}\n{ru_subtitle}\n{text_update}\n \n \n \n '
    if to_play_subtitle:
        ru_subtitle = Translator().translate(to_play_subtitle.lower().replace(".", ","), 'ru', 'en').text
    else:
        ru_subtitle = ""



    prepare_audio(ru_subtitle, subtitle)
    if press_space:

        check_whether_next_video("f10", 550)

        check_time_and_send_space()
        press_space = 0
    send_space = 0


def check_whether_next_video(message, loop):
    global next_video_time
    if next_video_time < time.time():

        if not press_space:
            keyboard.send('space')

        next_video_time += loop + 0.5
        keyboard.send(message)
        time.sleep(0.5)
        keyboard.send(message)
        if not press_space:
            keyboard.send('space')


def time_delay(pause, start_time, subtitle):
    global time_space
    while time.time() < start_time:
        if not pause:
            pause = 1
            check_time_and_send_space()
    if pause:
        time.sleep(0.2)
        check_time_and_send_space()
    start_time = 1 + time.time() + len(subtitle) * len(subtitle) * 0.0007
    return start_time


def empty_text(no_title):
    global updated_text, ad_skip
    time.sleep(0.1)
    if not send_space:
        if not ad_skip:
            keyboard.send('y')
            ad_skip = 1


def old_subtitles_delay(delayed_text):
    global updated_text
    while play_track:
        continue
    time.sleep(1)
    if updated_text == delayed_text:
        updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"


def prepare_audio( ru_subtitle, en_subtitle):
    global waite, play_track, updated_text, delayed_text, updated_text
    en_audio_file = 0

    en_subtitle = play_without_ecxeptions(en_subtitle)
    if en_subtitle:
        pygame.mixer.init()
        if ru_subtitle:
            ru_audio_file = gTTS(text=ru_subtitle, lang='ru')
            ru_audio_file.save("C:\\ANKIsentences\\temporary_ru_audio_file.mp3")
            ru_audio = "C:\\ANKIsentences\\temporary_ru_audio_file.mp3"
            pygame.mixer.music.load(ru_audio, "mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                if not en_audio_file:

                    en_audio_file = gTTS(text=en_subtitle.lower(), lang='en', slow=True)
                    en_audio_file.save("C:\\ANKIsentences\\temporary_en_audio_file.mp3")
                    en_audio = "C:\\ANKIsentences\\temporary_en_audio_file.mp3"
        if not en_audio_file:

            en_audio_file = gTTS(text=en_subtitle.lower(), lang='en')
            en_audio_file.save("C:\\ANKIsentences\\temporary_en_audio_file.mp3")
            en_audio = "C:\\ANKIsentences\\temporary_en_audio_file.mp3"

        pygame.mixer.music.load(en_audio, "mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.mixer.quit()




def show_subtitle_text():
    font = 20
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry('+0+0')
    root.overrideredirect(True)  # Remove the window frame
    font = ('Arial', font)
    label = tk.Label(
            root, text=updated_text, font=font, fg='white', bg='black'
            )  # Set text color to white and background to black
    label.pack()

    def update_text():
        label.config(text=updated_text)
        root.after(10, update_text)

    update_text()
    root.mainloop()


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


def split_text_with_punctuation(text, punctuation='].,;:!?)'):
    # """
    # >>> split_text_with_punctuation('what is it - it is ok ')
    # """
    parts = re.split(
        f"([{punctuation}])", text.replace(" mr.", " mr").replace("Mr.", "Mr").replace(" sir.", " sir").replace(
            "Sir.", "Sir"
            ).replace("*", "")
        )
    parts.append('')
    result = []
    compares = []
    severe = False
    for index in range(0, len(parts), 2):

        compare_count = 0
        compare = parts[index].strip(" -").lower()
        item_count = text.lower().count(compare)

        if compare and compare[0].isnumeric() and result and result[-1][-1] == ":" and result[-1][-2].isnumeric():
            result[-1] = result[-1] + parts[index] + parts[index + 1]
            continue

        if len(compare) == 1 and result and result[-1][-1] == "." == parts[index + 1]:
            result[-1] = result[-1] + parts[index] + "."
            severe = True
            continue
        elif severe:
            severe = False
            result[-1] = result[-1] + parts[index] + parts[index + 1]
            continue

        if item_count < 2:
            result.append(parts[index] + parts[index + 1])
        elif compare not in compares:
            for part in parts:
                if part.strip(" -").lower() == compare:
                    compare_count += 1
            if compare_count == item_count:
                result.append(parts[index] + parts[index + 1])
                compares.append(compare)

    parts = []
    for part in result:
        if "- " in part:
            chunks = part.split("- ")
            for chunk in chunks:
                parts.append(f"- {chunk}")
        else:
            parts.append(part)

    return parts


def no_repit(text, test=False):
    # """
    # >>> no_repit(' Mm-hmm.', test=True)
    # """
    global past_subtitles, str_hub, last_subtitle, prelast_subtitle
    punctuation = '].,;:!?)'
    start = split_text_with_punctuation(text, punctuation)
    # start = ['my abuela',]
    show_output = []
    play_output = []

    for part in start:

        if ":" in part:
            continue

        uniq = 0
        count_of_hard_word = 0
        part_strip_lower = part.strip(punctuation + " '-").lower()
        part_strip_lower_split = part_strip_lower.split()
        len_part_strip_lower_split = len(part_strip_lower_split)
        if part_strip_lower not in past_subtitles:


            for word in part_strip_lower_split:

                word = "".join(
                        letter for letter in word.strip(' -') if letter.isalpha() or letter in "'-"
                        ).rstrip("'s")
                if "-" in word:
                    var1, *vars = word.split('-')
                    if var1 == vars[0] == vars[-1]:
                        word = var1

                if word.replace('-', ""):
                    if word not in f"{top_300} {last_subtitle}" or len_part_strip_lower_split > 7:
                        if word not in f"{top_2000} {prelast_subtitle}" or len_part_strip_lower_split > 5:
                            past_subtitles_count = past_subtitles.count(word)
                            if word not in top_5000 or not past_subtitles_count or len_part_strip_lower_split > 3:
                                add_hurd_word = past_subtitles_count < 3
                                count_of_hard_word += add_hurd_word
                                if add_hurd_word:
                                    if Translator().translate(word.lower().replace(".", ","), 'ru', 'en').text.islower():
                                        play_output.append(part)
                                        uniq = 1
                                        break

        past_subtitles = past_subtitles + part_strip_lower
        if not uniq and len_part_strip_lower_split and count_of_hard_word / len_part_strip_lower_split > 0.5:
            play_output.append(part)
            uniq = 1


        if part.isupper():
            part = part.lower()
        if not uniq:
            part = part.upper().replace(" ", "  ")
        show_output.append(part)



    show = "".join(show_output)
    play = "".join(play_output)
    compare = show.lower() != play.lower() and play != ""
    if not test:
        stat_txt(f"('{text}', ' xxxxxx', '{show}', '{play}', {compare})")  # save all data to stat.txt for statictics

    last_subtitle, prelast_subtitle = text, last_subtitle

    return show, play, compare


def check_and_add_to_hub(len_part, part, punctuation):
    global str_hub
    if len_part == 1:
        var = part.strip(punctuation + " -").lower()
        if var not in f"{top_2000} {top_300} {str_hub}":
            str_hub = f"{str_hub} {var}"
            file = "C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\tests\\exceptions\\top_hub.txt"
            with open(file, "a", encoding='utf-8') as vars:
                vars.write(f" {var}")


def stat_txt(text):
    file = "C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\tests\\exceptions\\stat.txt"
    with open(file, "a", encoding='utf-8') as vars:
        vars.write(f"\n{text}")





if __name__ == '__main__':
    top_hub()
    threading.Thread(target=online_player).start()
    time.sleep(1)
    # threading.Thread(target=top_black_frame).start()
    # threading.Thread(target=mouse_move).start()
    show_subtitle_text()

    pass
