from datetime import time

import gTTS as gTTS
import keyboard as keyboard
from moviepy.editor import concatenate_audioclips, AudioFileClip

from Source.tools import *


@step_by_step_print_executing_line_number_and_data
def raw_txt_to_sentences_list(folder):
    file_path: tuple[str, str] = (
            f'C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\ANKI_CARDS\\' \
            f'undone_ChatGPT\\_{folder}_undone_chut_ChatGPT\\{today} undone_ChatGPT.txt',
            f"C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\ANKI_CARDS\\" \
            f"undone_anki_txt_format\\remainder\\chutGPT\\{today}chutGPT")
    with open(file_path[0], encoding="utf-8") as file:
        content: str = file.read()
    lines: tuple[str, ...] = (
            'Дайте мне популярные предложения', 'User', 'ChatGPT', 'Hide sidebar', 'Chat history', 'Конечно!',
            'Send a message.', 'Regenerate response', "2 / 2", "3 / 3",
            ai_request_for_sentence)
    gist: str = del_trash_lines_and_words(content, lines)
    return gist


@step_by_step_print_executing_line_number_and_data
def home_ai_answer_handling(folder):
    """
    >>> home_ai_answer_handling(15)
    """
    gist: str = raw_txt_to_sentences_list(folder)
    loop_sentences_list(gist, folder)


@step_by_step_print_executing_line_number_and_data
def loop_sentences_list(gist, folder):
    global count
    count[2] = 0
    odd: bool = True
    for line in gist.splitlines():
        if len(line) > 3:
            if odd:
                odd: bool = False
                russian: str = line
            else:
                odd: bool = True
                make_single_and_triple_audio(line, russian, folder)
            count[2] += 1


@step_by_step_print_executing_line_number_and_data
def concatenate_audio(audio_clips_paths, output_path):
    clips: list[AudioFileClip] = [AudioFileClip(path) for path in audio_clips_paths]
    final_clip: AudioFileClip = concatenate_audioclips(clips)
    final_clip.write_audiofile(output_path, codec='mp3')


@step_by_step_print_executing_line_number_and_data
def make_single_and_triple_audio(english_sentence,
                                 russian_sentence,
                                 folder
                                 ):
    english: str = english_sentence.upper().strip('.!?,()')
    russian: str = russian_sentence.upper().strip('.!?,()')
    audio_path: str = f"C:\\ANKIsentences\\triples_audio\\{folder}\\{today}\\{english}.mp3"
    en_temporary: str = f"C:\\ANKIsentences\\singles_audio\\{folder}\\{today}\\{english}_en.mp3"
    ru_temporary: str = f"C:\\ANKIsentences\\singles_audio\\{folder}\\{today}\\{russian}_ru.mp3"

    if no_error_in_files(en_temporary, english, ru_temporary, russian):
        en_audio: gTTS = gTTS(text=english_sentence, lang='en', slow=True)
        ru_audio: gTTS = gTTS(text=russian_sentence, lang='ru', slow=False)

        en_audio.save(en_temporary)
        ru_audio.save(ru_temporary)
        concatenate_audio([en_temporary, ru_temporary, en_temporary], audio_path)
        keyboard.press('down')
        time.sleep(10)
    else:
        print('UPS')


@step_by_step_print_executing_line_number_and_data
def no_error_in_files(en_temporary,
                      english,
                      ru_temporary,
                      russian
                      ):
    conditions: list[bool] = [
            detect_language(russian) == 'ru',
            detect_language(english) == 'en',
            not os.path.exists(en_temporary),
            not os.path.exists(ru_temporary),
            ]

    return all(conditions)
