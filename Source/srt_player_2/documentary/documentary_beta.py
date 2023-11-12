import threading
import time
import tkinter as tk

import keyboard
import mouse
import pygame
import pyperclip
from googletrans import Translator
from gtts import gTTS

from Source.srt_player_2.documentary.variables import prelast_subtitle, last_subtitle, past_subtitles, text_update, lines_minus_one, lines_minus_two, lines_minus_three, lines_zero, lines_plus_one, lines_plus_two, lines_plus_three, next_video_time, time_space, time_pause, pause, send_space, press_space
from Source.srt_player_2.en_two_line import split_text_with_punctuation
from tests.exceptions.top_words import top_300, top_2000, top_5000


# from Source.srt_player_2.en_two_line import  no_repit


def no_repit(text, test=False):
    global past_subtitles, last_subtitle, prelast_subtitle
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
    # if not test:
    #     stat_txt(f"('{text}', ' xxxxxx', '{show}', '{play}', {compare})")  # save all data to stat.txt for statictics

    last_subtitle, prelast_subtitle = text, last_subtitle

    return show, play, compare



def check_whether_next_video(message, loop, text=""):
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


def mouse_move():
    move = 1
    while True:
        move *= -1
        mouse.move(move, move, absolute=False, duration=0.1)


def start():
    global lines_minus_one, lines_minus_two, lines_minus_three, lines_zero, lines_plus_one, lines_plus_two, lines_plus_three, next_video_time, time_space, time_pause, pause, send_space, press_space

    keyboard.send('ctrl + a')
    pyperclip.copy("")
    time.sleep(0.3)
    keyboard.send('space')
    next_video_time = time.time() + 550
    keyboard.send("f10")


def en_ru_corrector(text, lang="en"):
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


def check_time_and_send_space():
    global time_space
    while time.time() < time_space:
        pass
    time_space = time.time() + 0.25
    keyboard.send("space")


def check_time_and_make_pause():
    global time_pause, pause
    while time.time() < time_pause:
        pass
    time_pause = time.time() + 0.5
    keyboard.send("y")
    pause = (1, 0)[pause == 1]


def main_cycle(till="888888"):
    global text_update, lines_minus_one, lines_minus_two, lines_minus_three, lines_zero, lines_plus_one, lines_plus_two, lines_plus_three, next_video_time, time_space, time_pause, pause, send_space, press_space

    pyperclip.copy("")
    prev_subtitle = ""
    keyboard.send('space')
    temporary_lines = []


    keyboard.send("f10")
    next_video_time = time.time() + 550
    # check_time_and_make_pause()

    while True:
        keyboard.send('ctrl + c')
        paste = pyperclip.paste()

        if till in pyperclip.paste():
            break
        subtitle_lines = make_subtitle_from(paste)
        subtitle_lines_strip = subtitle_lines.strip()
        if subtitle_lines_strip and prev_subtitle != subtitle_lines:
            prev_subtitle = subtitle_lines
            subtitle = en_ru_corrector(subtitle_lines, "en")

            subtitle, to_play_subtitle, different = no_repit(subtitle)
            ru_subtitle = Translator().translate(subtitle.lower().replace(".", ","), 'ru', 'en').text
            temporary_lines.append((subtitle, to_play_subtitle, ru_subtitle, different))

            if len(temporary_lines) > 3:
                if send_space:
                    check_time_and_send_space()
                    press_space = 1
                    while send_space:
                        pass
                _1, _2, _3, _4 = temporary_lines.pop(0)

                lines_minus_one = lines_minus_two
                lines_minus_two = lines_minus_three
                lines_minus_three = f"{lines_zero}"
                lines_zero = f"{_1}\n{_3}\n{text_update}"
                lines_plus_one = f"{text_update}\n{temporary_lines[0][0]}\n{temporary_lines[0][2]}"
                lines_plus_two = f"{text_update}\n{temporary_lines[1][0]}\n{temporary_lines[1][2]}"
                lines_plus_three = f"{text_update}\n{temporary_lines[2][0]}\n{temporary_lines[2][2]}"
                threading.Thread(
                        target=execute, args=(_1, _2, _3, _4)
                        ).start()
            else:
                time.sleep(0.1)
        else:
            time.sleep(0.1)


def execute(subtitle, to_play_subtitle, ru_subtitle, different):
    global lines_minus_one, lines_minus_two, lines_minus_three, lines_zero, lines_plus_one, lines_plus_two, lines_plus_three, next_video_time, time_space, time_pause, pause, send_space, press_space

    send_space = 1

    if not to_play_subtitle:
        ru_subtitle = ""
    elif different:
        ru_subtitle = Translator().translate(to_play_subtitle.lower().replace(".", ","), 'ru', 'en').text

    prepare_audio(ru_subtitle, subtitle)
    if press_space:

        check_whether_next_video("f10", 550)

        check_time_and_send_space()
        press_space = 0
    send_space = 0


def prepare_audio(ru_subtitle, en_subtitle):
    global lines_minus_one, lines_minus_two, lines_minus_three, lines_zero, lines_plus_one, lines_plus_two, lines_plus_three, next_video_time, time_space, time_pause, pause, send_space, press_space
    en_audio_file = 0

    en_subtitle = play_without_ecxeptions(en_subtitle)
    if en_subtitle:
        pygame.mixer.init()
        if ru_subtitle:
            ru_audio_file = gTTS(text=ru_subtitle, lang='ru')
            ru_audio_file.save("C:\\ANKIsentences\\temporary_ru_audio_file.mp3")
            ru_audio = "C:\\ANKIsentences\\temporary_ru_audio_file.mp3"
            pygame.mixer.music.load(ru_audio, "mp3")
            # check_time_and_make_pause()

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
        # if pause:
        #     check_time_and_make_pause()
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.mixer.quit()
        # check_time_and_make_pause()


def play_without_ecxeptions(text, extra_exceptions="", exceptions="*♪¤¶"):
    return "".join(sign for sign in text if sign not in f"{exceptions}{extra_exceptions}")


def make_subtitle_from(paste):
    return " ".join(
            [
                    line for line in paste.splitlines()
                    if not
                       any(
                               word in line for word in
                               ["Качество", "Звук", "Субтитры", "Скорость", "Масштаб", "/", '0:00/ 0:00', "/ 2:",
                                "/ 1:",
                                "/ 3:"]
                               ) and line
                    ]
            )


def show_minus_one(disposition="+0+0", colour='yellow', font=('Arial', 20), background="black"):
    global lines_minus_one
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(disposition)
    root.overrideredirect(True)  # Remove the window frame
    label = tk.Label(root, text=lines_minus_one, font=font, fg=colour, bg=background)
    label.pack()

    def update_text():
        label.config(text=lines_minus_one)
        root.after(10, update_text)

    update_text()
    root.mainloop()


def show_minus_two(disposition="+0+102", colour='yellow', font=('Arial', 20), background="black"):
    global lines_minus_two
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(disposition)
    root.overrideredirect(True)  # Remove the window frame
    label = tk.Label(root, text=lines_minus_two, font=font, fg=colour, bg=background)
    label.pack()

    def update_text():
        label.config(text=lines_minus_two)
        root.after(10, update_text)

    update_text()
    root.mainloop()


def show_minus_three(disposition="+0+204", colour='yellow', font=('Arial', 20), background="black"):
    global lines_minus_three
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(disposition)
    root.overrideredirect(True)  # Remove the window frame
    label = tk.Label(root, text=lines_minus_three, font=font, fg=colour, bg=background)
    label.pack()

    def update_text():
        label.config(text=lines_minus_three)
        root.after(10, update_text)

    update_text()
    root.mainloop()


def show_zero(disposition="+0+306", colour='white', font=('Arial', 20), background="black"):
    global lines_zero
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(disposition)
    root.overrideredirect(True)  # Remove the window frame
    label = tk.Label(root, text=lines_zero, font=font, fg=colour, bg=background)
    label.pack()

    def update_text():
        label.config(text=lines_zero)
        root.after(10, update_text)

    update_text()
    root.mainloop()


def show_lines_plus_one(disposition="+0+376", colour='yellow', font=('Arial', 20), background="black"):
    global lines_plus_one
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(disposition)
    root.overrideredirect(True)  # Remove the window frame
    label = tk.Label(root, text=lines_plus_one, font=font, fg=colour, bg=background)
    label.pack()

    def update_text():
        label.config(text=lines_plus_one)
        root.after(10, update_text)

    update_text()
    root.mainloop()


def show_lines_plus_two(disposition="+0+478", colour='yellow', font=('Arial', 20), background="black"):
    global lines_plus_two
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(disposition)
    root.overrideredirect(True)  # Remove the window frame
    label = tk.Label(root, text=lines_plus_two, font=font, fg=colour, bg=background)
    label.pack()

    def update_text():
        label.config(text=lines_plus_two)
        root.after(10, update_text)

    update_text()
    root.mainloop()


def show_lines_plus_three(disposition="+0+580", colour='yellow', font=('Arial', 20), background="black"):
    global lines_plus_three
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(disposition)
    root.overrideredirect(True)  # Remove the window frame
    label = tk.Label(root, text=lines_plus_three, font=font, fg=colour, bg=background)
    label.pack()

    def update_text():
        label.config(text=lines_plus_three)
        root.after(10, update_text)

    update_text()
    root.mainloop()


if __name__ == '__main__':
    time.sleep(1)
    threading.Thread(target=mouse_move).start()
    time.sleep(1)
    threading.Thread(target=show_minus_one).start()
    time.sleep(1)
    threading.Thread(target=show_minus_two).start()
    time.sleep(1)
    threading.Thread(target=show_minus_three).start()
    time.sleep(1)
    threading.Thread(target=show_zero).start()
    time.sleep(1)
    threading.Thread(target=show_lines_plus_one).start()
    time.sleep(1)
    threading.Thread(target=show_lines_plus_two).start()
    time.sleep(1)
    threading.Thread(target=show_lines_plus_three).start()
    time.sleep(1)

    main_cycle()
