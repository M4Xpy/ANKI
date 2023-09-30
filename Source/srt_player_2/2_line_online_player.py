import threading
import time
import tkinter as tk

import keyboard
import mouse
import pygame
import pyperclip
from googletrans import Translator
from gtts import gTTS

text_update = 170 * " "
updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"
mp3_ru_audio = False
mp3_en_audio = False
play_track = False
past_subtitles = """ family sorry kill girlfriend schoolgirl schoolboy boyfriend did it's sir can't lord don't okay tv please the be of and a in to have it for i that you he on with do at by not this but from they his she or which as we an say will would can if their go what there all get her make who out up see know time take them some could so him year into its then think my come than love more about now last your me no other give just these people two also well any only new very when may way look like use such how because good find man our want day between even many one after down thing tell back must child here over too put work old part three life great where woman us need feel system each much ask group number yes another again world area show course company under problem against never most service try call hand party american high something school small place before why away house different country really week large member off always end mr start help every home night play book four young room car line big name friend five talk market hour door office let war full sort read mother police price little today open bad programme minute moment girl stop control class six learn father real plan product city boy game food bank black town history white """


def online_player():
    global updated_text, mp3_ru_audio, mp3_en_audio, play_track, different, to_play_subtitle, translated, wate

    wate = False






    prev_subtitle = ""
    keyboard.send('ctrl + a')
    time.sleep(0.3)
    keyboard.send('space')
    time.sleep(0.3)
    move = 1
    play_track = False

    while 1:
        move *= -1
        mouse.move(move, move, absolute=False, duration=0.0001)
        keyboard.send('ctrl + c')

        subtitle_lines = pyperclip.paste().splitlines()
        len_subtitle_lines = len(subtitle_lines)
        index = {
                0: 99,
                1: 99,
                2: 99,
                3: 2,
                4: 2,
                5: 99,
                6: 99,
                7: 99,
                8: 7,
                9: 7
                }[len_subtitle_lines if len_subtitle_lines < 10 else 0]
        subtitle = " ".join(subtitle_lines[index:])

        if prev_subtitle != subtitle:
            prev_subtitle = subtitle

            if play_track:
                keyboard.send('space')
                wate = False
                while not wate:
                    continue



            if subtitle:

                subtitle, to_play_subtitle, different = no_repit(subtitle, True)
                updated_text = f'{subtitle}\n{text_update}\n{text_update}\n{text_update}'
                translated = Translator().translate(subtitle.lower(), 'ru', 'en').text
                if len(translated) > 99:
                    halve = translated.split()
                    point = len(halve) // 2
                    first = " ".join(halve[:point])
                    second = " ".join(halve[point:])
                    updated_text = f'{subtitle}\n{first}\n{second}\n{text_update}'
                else:
                    updated_text = f'{subtitle}\n{translated}\n{text_update}\n{text_update}'
                if to_play_subtitle:
                    play_track = True
                    threading.Thread(target=prepare_audio, args=(different, to_play_subtitle, translated)).start()




            else:
                if updated_text != f'{subtitle}\n{translated}\n{text_update}\n{text_update}':
                    delayed_text = updated_text
                    threading.Thread(target=old_subtitles_delay, args=(delayed_text,)).start()
                time.sleep(0.1)
        else:
            time.sleep(0.1)


def old_subtitles_delay(delayed_text):
    global updated_text
    while play_track:
        continue
    time.sleep(len(updated_text.splitlines()[0]) * 0.04)
    if updated_text == delayed_text:
        updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"


def prepare_audio(different, to_play_subtitle, translated):
        global wate, play_track

        if different:
            translated = Translator().translate(to_play_subtitle.lower(), 'ru', 'en').text
        ru_audio_file = gTTS(text=translated, lang='ru')
        ru_audio_file.save("C:\\ANKIsentences\\temporary.mp3")
        ru_audio = "C:\\ANKIsentences\\temporary.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(ru_audio, "mp3")
        pygame.mixer.music.set_volume(0.5)

        while wate:
            continue


        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        wate = True
        play_track = False
        keyboard.send('space')
        pygame.mixer.quit()




def show_subtitle_text():
    font = 20
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry('+0+668')
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


def no_repit(text, test=False):
    # """
    # >>> no_repit(' Whatever happens,')
    # """
    global past_subtitles
    in_put = text
    text = f"{text}*".replace(" mr.", "mr").replace(" Mr.", "Mr")
    compares = [" "]
    to_play_output = [" "]
    part = ""
    now_past_subtitles = ""
    for letter in text:
        part = part + letter
        if letter not in "abcdefghijklmnopqrstuvwxyz' \"ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
            now_compare = 1
            for index, compare in enumerate(compares):
                now_compare = part.strip(' -?!,.:*').lower()  #################################
                if compare.strip(' -?!,.:*').lower() == now_compare and now_compare:
                    compares[index] = compares[index][:-1] + letter
                    now_compare = 0
                    break
            if now_compare or part == compares[-1][-1] or compares == [" "]:
                compares.append(part)
                compare_part = part.lower().replace("*", " ").strip(' -?!,.:*')  #################################
                if compare_part not in past_subtitles:

                    add_compare_part = compare_part.lower().strip(' ?!,.:*').replace("-", " ")
                    compare_part = add_compare_part.split()
                    if len(compare_part) > 5 or any(item not in past_subtitles for item in compare_part):
                        past_subtitles = past_subtitles + add_compare_part + " "
                        to_play_output.append(part)

                    # print(past_subtitles)
                    # print(part)
                    # print()
            part = ""
    out_put = "".join(compares).replace("*", " ").strip()
    to_play_output = "".join(to_play_output).replace("*", " ").strip()
    # list_to_play_output = to_play_output.lower().strip(' ?!,.:*').replace("-", " ").replace(" a ", " ").replace(
    #     " the ", " ").split()
    # if len(list_to_play_output) < 5 and all(item in past_subtitles for item in list_to_play_output):
    #     to_play_output = ""
    # past_subtitles = past_subtitles + now_past_subtitles + " "

    in_put = in_put.replace("*", " ")

    diff = (1, 0)[in_put == to_play_output]
    print((out_put, to_play_output, diff))

    if len(in_put.strip()) - 3 < len(out_put.strip()):
        return in_put, to_play_output, diff
    if test:
        print()
        print(f"{in_put}\n{out_put}\n", len(in_put.strip()), len(out_put.strip()))
        print()

    return out_put, to_play_output, diff


if __name__ == '__main__':
    threading.Thread(target=online_player).start()
    threading.Thread(target=top_black_frame).start()
    show_subtitle_text()

    pass
