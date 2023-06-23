import inspect
import os
import random
import re
import sys
import time
import traceback
import webbrowser
from datetime import date
from typing import Callable, Any

import keyboard as keyboard
import pyperclip
from googletrans import Translator
from gtts import gTTS
from moviepy.editor import concatenate_audioclips, AudioFileClip

from Source.mp3name_detector import find_in_the

ai_request_for_sentence: str = {
        1: 'Дайте мне популярные предложения , параллельно с переводом этих предложений на английский язык ,'
           ' с английскими словами',
        2: 'A simple sentences,in past or future tense, '
           'along with the translation of these sentences into russian, with English words',
        3: 'Popular sentences with the words'
        }[1]

new_data: str = ''
git_hub: str | None = os.getenv('GITHUB_ACTIONS')
count: list[int] = [0, 1, 0]
start: bool = True
today: callable = date.today().day


def whether_test_mode() -> bool:
    return False if not any(
            [
                    'CI' in os.environ,
                    'GITHUB_ACTIONS' in os.environ,
                    'PYTEST_CURRENT_TEST' in os.environ,
                    'doctest' in sys.modules,
                    '__pytest' in sys.modules,
                    '__unittest' in sys.modules,
                    ]
            ) else True


now_test: bool = whether_test_mode()


def step_by_step_print_executing_line_number_and_data(func: Any
                                                      ) -> Any:
    """ Decorator that prints the executing line number and data.
    >>> run_program(True)
    """

    def wrapper(*args: tuple[Any, ...]
                ) -> Any:
        if not now_test:
            global count
            print(f'{count[0]:^3}  >>>  {inspect.currentframe().f_back.f_lineno:^3} >>> {args}')
            count[0] += 1
        return func(*args)

    return wrapper


@step_by_step_print_executing_line_number_and_data
def detect_language(text: str
                    ) -> str:
    """
    >>> detect_language('если строка на русском')
    'ru'
    >>> detect_language('if string in english')
    'en'
    """
    return ('en', 'ru')[ord(text.strip()[1]) > 127]


# @step_by_step_print_executing_line_number_and_data
def generate_audio_file(text: str,
                        save_file: int | None = 0,
                        language: str | None = '',
                        ) -> str | None:
    """Generates audio file of the input_string in its detected language.
    >>> generate_audio_file(text='test', save_file=-1)
    """
    text: str = text.lower()
    folder: str = ('C:\\Users\\Я\\Desktop\\audio',
                   f"C:\\Users\\Я\\Documents\\Anki\\1-й пользователь\\collection.media",
                   f"C:\\Users\\Я\\AppData\\Roaming\\Anki2\\User 1\\collection.media",
                   os.path.join(os.path.dirname(__file__), "..", "additional_data", "mp3s_for_tests"))[
        save_file]
    language: str = language or detect_language(text)  # Detect language of the input_string
    audio_file_name: str = f'{text}.mp3'  # Generate audio file name
    try:
        audio: gTTS = gTTS(text=text, lang=language, slow=False)  # Generate audio file
        audio_file_path: str = os.path.join(folder, audio_file_name)  # Save audio file to directory
        audio.save(audio_file_path)
        if not save_file:
            return audio_file_path
    except:
        if_error("_return", "generate_audio_file_failed._Check_your_network_connection_and_try_again.")


@step_by_step_print_executing_line_number_and_data
def en_ru_en_translator(input_text: str,
                        lang: str | None = None
                        ) -> str:
    """
    >>> en_ru_en_translator('apple')
    'яблоко'
    >>> en_ru_en_translator('яблоко')
    'apple'
    """
    out_of, onto = {'ru': ('ru', 'en'), 'en': ('en', 'ru')}[lang or detect_language(input_text)]
    try:
        return Translator().translate(input_text, src=out_of, dest=onto).text
    except:
        if_error("_return", "Translation_failed._Check_your_network_connection_and_try_again.")


@step_by_step_print_executing_line_number_and_data
def ctrl_4_open_google_image(text: str | None = ''
                             ) -> None:
    """ open google image with received request
    >>> ctrl_4_open_google_image('test')
    """
    if not text:
        text: str = pyperclip.paste()
    if len(text.splitlines()) > 1:
        text: str = star_separated_words_from(text)
    if '*' in text:
        for word in text.replace('*', '').split()[::-1]:
            open_google_image(word)
    else:
        open_google_image(text.strip('_1234567890'))


@step_by_step_print_executing_line_number_and_data
def open_google_image(word: str,
                      new_page: int | None = 0
                      ) -> None:
    """ open google image with received request
    >>> open_google_image("TEST", 1)
    """
    url: str = f'https://www.google.com/search?q={word}' \
               f'&tbm=isch&hl=en&tbs=itp:clipart&sa=X&ved=0CAIQpwVqFwoTCKCx4PzezvsCFQAAAAAdAAAAABAD&biw=1349&bih=625'
    webbrowser.open(url, new=new_page)


@step_by_step_print_executing_line_number_and_data
def ctrl_c_w_request_for() -> None:
    """ return to the clipboard the text received from the clipboard, processed by request_for
    >>> ctrl_c_w_request_for()
    """
    return copy_func_paste(get_template)


@step_by_step_print_executing_line_number_and_data
def get_template(text: str,
                 template: str = 'ai',
                 ) -> str:
    """ return chosen template with given word
    >>> get_template(template='check', text='test')
    'This is a test'
    """
    text: str = text.strip(' _1234567890')
    return {
            'ai'   : f"Provide popular phrases with word '{text}' , along with  translations into Russian\n"
                     f"Provide single-root nouns, verbs, adjectives, adverbs for the word '{text}', "
                     f"along with translations into Russian.",
            'check': f"This is a {text}"

            }[template]


def clone_replace_non_english_letter(text: str
                                     ) -> str:
    """
    >>> clone: str = clone_replace_non_english_letter('test-test\\n[sound:testy.mp3]')
    >>> assert 'test-test\\n' == clone == replace_non_english_letter('test-test\\n[sound:testy.mp3]')
    """
    text: str = text.replace('[sound:', ' ')
    pattern: str = r"[^A-Za-z\n.-]"
    replaced_text: str = re.sub(pattern, " ", text)
    split_text_list: list[str] = replaced_text.split(' ')
    values: list[str] = []
    for item in split_text_list:
        if item:
            if '.mp' not in item:
                values.append(item)
    dot_result: str = ' '.join(values)
    result: str = dot_result.replace('.', '')
    return result


@step_by_step_print_executing_line_number_and_data
def replace_non_english_letter(text: str
                               ) -> str:
    return ' '.join(
            item
            for item in re.sub(
                    r"[^A-Za-z\n.-]", " ", text.replace('[sound:', ' ')
                    ).split(' ')
            if item and '.mp' not in item
            ).replace('.', '')


@step_by_step_print_executing_line_number_and_data
def star_separated_words_from(text: str
                              ) -> str:
    """ extract first word of each line, removing any digits or underscores from the word, and join them with asterisks
    >>> star_separated_words_from('test-test\\n[sound:test.mp3]')
    ' * test * '
    """
    text: str = replace_non_english_letter(text)
    lines: list[str] = [line.split()[0]
                        for line in text.splitlines()
                        if line.strip()
                        ]
    if len(lines) < 2:
        return f" * {' * '.join(word for word in text.split() if detect_language(word) == 'en')} * "
    return f" * {' * '.join(lines)} * "


@step_by_step_print_executing_line_number_and_data
def header_tab_mp3() -> None:
    """write star_separated_words press tab and at the end of the page write mp3 refers"""
    press_keys("ctrl + a", 0.1)
    data: Any = pyperclip.paste()
    header, tab_mp3s_remainder = header_tab_mp3_content(data)
    keyboard.write(header)
    press_keys(.25, 'tab', .25, "ctrl + end")
    keyboard.write(tab_mp3s_remainder)


@step_by_step_print_executing_line_number_and_data
def header_tab_mp3_content(text: str) -> tuple[str, ...]:
    """
    >>> header_tab_mp3_content('test-test\\n[sound:test.mp3]') > ()
    True
    """
    header: str = star_separated_words_from(text)
    mp3refers: list[str] = refers_mp3s(header)
    len_mp3refers: int = -2 if len(mp3refers) > 3 else -(len(mp3refers) + 1)
    header: str = f" * {' * '.join(refer.removeprefix('[sound:').removesuffix('.mp3]') for refer in mp3refers[len_mp3refers:] + mp3refers[:len_mp3refers])} * "
    header: str = f"{header}\n{chr(10).join(mp3refers[len_mp3refers:])}"
    tab_mp3s_remainder: str = f"\n\n{chr(10).join(mp3refers[:len_mp3refers])}"
    return header, tab_mp3s_remainder


@step_by_step_print_executing_line_number_and_data
def refers_mp3s(
        header: str,
        save_file: int | None = 1
        ) -> list[str]:
    """ make mp3 reference
    >>> refers_mp3s('test', save_file=-1)
    ['[sound:test.mp3]']
    """
    word_s: list[str] = header.strip(' *').split(' * ')
    mp3refers: list[str] = []
    for word in word_s:
        generate_audio_file(word, save_file, 'en')
        mp3refers.append(f'[sound:{word}.mp3]')
    return mp3refers


@step_by_step_print_executing_line_number_and_data
def new_single_word_card() -> None:
    """ save old card , then made new card ready to save """
    global count
    press_keys('ctrl + e', 0.1)
    if count[1]:
        count[1] = 0
    else:
        press_keys(0.1, 'ctrl + enter')
    answer, question = new_single_word_card_content()
    keyboard.write(question)
    press_keys(0.01, 'tab', 0.01)
    keyboard.write(answer)
    press_keys(0.01, 'ctrl + v', 0.01)


@step_by_step_print_executing_line_number_and_data
def new_single_word_card_content() -> tuple[str, str]:
    in_text: str = pyperclip.paste()
    word: str = in_text.split()[0].split()[0].strip('_1234567890')
    question: str = f" * {word} *\n{refers_mp3s(word)[0]}"
    answer: str = f' * {" * ".join(word for word in translations_of_the(word))} *\n'
    return answer, question


@step_by_step_print_executing_line_number_and_data
def if_error(
        doing: str | None = '_return',
        report: str | None = 'error'
        ) -> str | None:
    """ write traceback , error message
    >>> if_error()
    error
    'error'
    """
    traceback.print_exc()
    print(report)
    if doing == 'keyboard_write':
        keyboard.write(report)
    elif doing == 'pyperclip_copy':
        pyperclip.copy(report)
    elif doing == '_return':
        return report


@step_by_step_print_executing_line_number_and_data
def translations_of_the(word: str) -> set:
    """ Give different variants of word tranlation
    >>> sorted(translations_of_the('ZAP'))
    ['БЫСТРО', 'РАЗРЯД', 'РАЗРЯДКА', 'ЩЕЛКАТЬ']
    """
    word: str = word.lower()
    translate_s: set[str | None] = set(
            en_ru_en_translator(f'{prefix} {word}', 'en').upper() for prefix in ('', 'the', 'to')
            )
    adjective: str = en_ru_en_translator(f'too {word}', 'en')
    translate_s.add(' '.join(word for word in adjective.split()[1:]).upper())
    return translate_s


@step_by_step_print_executing_line_number_and_data
def make_func_write(
        func: Callable[[str], str]
        ) -> None:
    """ take data in clipboard , doing function , return result in clipboard"""
    keyboard.write(func(pyperclip.paste()))


@step_by_step_print_executing_line_number_and_data
def ctrl_c_3_multi_translations() -> None:
    """ take data in clipboard , make up to 4 translations , return result in clipboard"""
    return make_func_write(multi_translations)


def clone_multi_translations(word_s: str) -> str:
    """ return star separated translated vars of getted word
    >>> in_put, out_put = "ADJOIN_8068", "ADJOIN_8068 * ПРИМЫКАТЬ * "
    >>> assert out_put == multi_translations(in_put) == clone_multi_translations(in_put)
    """
    result_s: list[str] = []
    word_s_replace: str = word_s.replace(',', ' ')
    words_split: list[str] = word_s_replace.split()
    for _word in words_split:
        word: str = _word.strip(' _1234567890')
        translations: set = translations_of_the(word)  # gives up to four translations of the word
        result: str = f"{_word} * {' * '.join(translations)} * "  # return star separated translations words
        result_s.append(result)
    result: str = '\n\n'.join(result_s)
    return result


@step_by_step_print_executing_line_number_and_data
def multi_translations(word_s: str
                       ) -> str:
    return '\n\n'.join(
            f"{word} * {' * '.join(translations_of_the(word.strip(' _1234567890')))} * "
            for word in word_s.replace(',', ' ').split()
            )


@step_by_step_print_executing_line_number_and_data
def press_keys(
        *args: float | str
        ) -> None:
    """ Presses the given keys with optional time delays
    Args: *args (float or str): The keys to press, with optional time abcdelays between consecutive key presses.
    Raises:TypeError: If any argument in *args is not a float or string.
    >>> press_keys(0.001)
    """
    for arg in args:
        time.sleep(arg) if isinstance(arg, float) else keyboard.send(arg)


@step_by_step_print_executing_line_number_and_data
def ctrl_c_q_formatter() -> None:
    """ take data from clipboard , filtered lines , return result to clipboard  """
    return copy_func_paste(del_trash_lines_and_words)


def clone_del_trash_lines_and_words(text: str,
                                    del_lines: tuple[str, ...] | None = None,
                                    del_words: tuple[str, ...] | None = None,
                                    ) -> str:
    """
    return text without lines with words from chek_s tuple, remove 'Translation:'
    >>> del_trash_lines_and_words("Nouns:\\r\\nT\\r\\nE\\nS\\nPlease note\\nT\\nTranslation:").replace('\\n', '')
    'TEST'
    >>> clone_del_trash_lines_and_words("Nouns:\\r\\nT\\r\\nE\\nS\\nPlease note\\nT\\nTranslation:").replace('\\n', '')
    'TEST'
    """
    time.sleep(0.25)
    if not del_lines:
        del_lines: tuple[str, ...] = ('nouns:', 'verbs:', 'adjectives:', 'adverbs:', 'please note', 'phrases', 'None',
                                      'Single-root nouns,', 'Noun:', 'Verb:', 'Adjective:', 'Adverb:')
    filtered_lines: list[str] = []
    text_split_lines: list[str] = text.splitlines()
    for line in text_split_lines:
        if not any(check in line.lower() for check in del_lines):
            filtered_lines.append(line.replace('Translation:', ''))
    result: str = '\n'.join(filtered_lines)
    rr_result: str = replace_all_exceptions_in(result, del_words)
    return rr_result


@step_by_step_print_executing_line_number_and_data
def del_trash_lines_and_words(text: str,
                              del_lines: tuple[str, ...] | None = None,
                              del_words: tuple[str, ...] | None = None,
                              ) -> str:
    time.sleep(0.25)
    return replace_all_exceptions_in(
            '\n'.join(
                    line
                    for line in text.splitlines()
                    if not any(
                            check.lower() in line.lower()
                            for check in del_lines or ('nouns:', 'verbs:', 'adjectives:', 'adverbs:', 'please note',
                                                       'phrases', 'None', 'Single-root nouns,', 'Noun:', 'Verb:',
                                                       'Adjective:', 'Adverb:')
                            )
                    ),
            del_words
            )


@step_by_step_print_executing_line_number_and_data
def replace_all_exceptions_in(text: str,
                              del_words: list[str] | None = None
                              ) -> str:
    """
    >>> replace_all_exceptions_in('aabbcc', del_words=['a'])
    'bbcc'
    """
    if not del_words:
        del_words = ['Translation:', ''], ['Russian translation:', '']
    for exception in del_words:
        if len(exception) < 2:
            substitute: str = ''
        else:
            substitute: str = exception[1]
        text: str = text.replace(exception[0], substitute)
    while '\n\n\n' in text:
        text;
        str = text.replace('\n\n\n', '\n\n')
    return text


@step_by_step_print_executing_line_number_and_data
def copy_func_paste(func: Callable[[str], str]
                    ) -> None:
    """ return to the clipboard the text received from the clipboard, processed by the provided function """
    pyperclip.copy(func(pyperclip.paste()))


@step_by_step_print_executing_line_number_and_data
def _a_lot_of_new_single_card() -> None:
    """ take new line from lines_hub, make new card , open google image"""
    lines_hub: str = """ """

    lines: list[str] = [line
                        for line in lines_hub.splitlines()
                        if len(line.strip(' *@')) > 3
                        ]
    first: str | None = lines[-1].split()[0]  # while cycle of card making , google image opened
    while True:
        if keyboard.is_pressed('space + enter'):
            try:
                text: str = lines.pop()
                pyperclip.copy(text)
                time.sleep(0.1)
                new_single_word_card()
                time.sleep(0.1)
                ctrl_4_open_google_image(lines[-1].split()[0])
                if first:
                    ctrl_4_open_google_image(first)
                    first: str | None = None
            except IndexError:
                raise IndexError('end of list')


@step_by_step_print_executing_line_number_and_data
def ai_request_list():
    global start
    _31: str = f'C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\ANKI_CARDS\\' \
               f'undone_anki_txt_format\\_31\\{today}.txt'
    _15: str = f'C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\ANKI_CARDS\\' \
               f'undone_anki_txt_format\\_15\\{(today, today - 15)[today < 15]}.txt'
    remainder: str = f"C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\ANKI_CARDS\\" \
                     f"undone_anki_txt_format\\remainder\\{today}.txt"
    if start:
        start = False

        return sorted(find_in_the(_15, 'mp3_words'))


words_list: list[str | None] = ai_request_list()


@step_by_step_print_executing_line_number_and_data
def ai_request_for_10_sentences_at_time_from():
    """

    """
    global words_list
    leno: int = len(words_list)
    if leno:
        share: int = (10, leno)[leno < 9]
        now_list = tuple(words_list[:share])
        words_list = words_list[share:]
        return f'{ai_request_for_sentence} ({", ".join(now_list)})'


@step_by_step_print_executing_line_number_and_data
def page_down_ai_request_for_10_sentences_at_time():
    if words_list:
        keyboard.write(ai_request_for_10_sentences_at_time_from())
        # press_keys(0.1, 'enter')


@step_by_step_print_executing_line_number_and_data
def concatenate_audio(audio_clips_paths, output_path):
    clips: list[AudioFileClip] = [AudioFileClip(path) for path in audio_clips_paths]
    final_clip: AudioFileClip = concatenate_audioclips(clips)
    final_clip.write_audiofile(output_path, codec='mp3')


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
def raw_txt_to_sentences_list(folder):
    file_path: str = f'C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\ANKI_CARDS\\' \
                     f'undone_ChatGPT\\_{folder}_undone_chut_ChatGPT\\{today} undone_ChatGPT.txt'
    # file_path: str = f"C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\ANKI_CARDS\\" \
    #           f"undone_anki_txt_format\\remainder\\chutGPT\\{today}chutGPT"
    with open(file_path, encoding="utf-8") as file:
        content: str = file.read()
    lines: tuple[str, ...] = (
            'Дайте мне популярные предложения', 'User', 'ChatGPT', 'Hide sidebar', 'Chat history', 'Конечно!',
            'Send a message.', 'Regenerate response', "2 / 2", "3 / 3",
            ai_request_for_sentence)
    gist: str = del_trash_lines_and_words(content, lines)
    return gist


@step_by_step_print_executing_line_number_and_data
def make_single_and_triple_audio(english_sentense,
                                 russian_sentence,
                                 folder
                                 ):
    english: str = english_sentense.upper().strip('.!?,()')
    russian: str = russian_sentence.upper().strip('.!?,()')
    audio_path: str = f"C:\\ANKIsentences\\triples_audio\\{folder}\\{today}\\{english}.mp3"
    en_temporary: str = f"C:\\ANKIsentences\\singles_audio\\{folder}\\{today}\\{english}_en.mp3"
    ru_temporary: str = f"C:\\ANKIsentences\\singles_audio\\{folder}\\{today}\\{russian}_ru.mp3"

    if no_error_in_files(en_temporary, english, ru_temporary, russian):
        en_audio: gTTS = gTTS(text=english_sentense, lang='en', slow=True)
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


@step_by_step_print_executing_line_number_and_data
def error_exception_but_file_present(folder,
                                     file_names,
                                     format,
                                     ):
    for file_name in file_names:
        if not any(
                (os.path.exists(f"{folder}{file_name.upper}_en{format}"),
                 os.path.exists(f"{folder}{file_name.upper()}_ru{format}"))
                ):
            print(f'{file_name} ')


@step_by_step_print_executing_line_number_and_data
def whole_folder_error_handling(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            new_filename: str = f'{filename.replace("(", "").replace(")", "")}'
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))


@step_by_step_print_executing_line_number_and_data
def delete_backspace_page_down_presser():
    while words_list:
        time.sleep(4)
        page_down_ai_request_for_10_sentences_at_time()
        time.sleep(random.randint(55, 77))


def home_add_single_phrase():
    press_keys('ctrl + c', 0.1)
    phrase: str | None = pyperclip.paste()
    translate: str = en_ru_en_translator(phrase, 'en')
    result: str = f'{phrase} *** {translate}\n'
    file_path: str = 'C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\ANKI_CARDS\\REPETE_ME\\' \
                     f'{today}.txt'
    with open(file_path, 'a+', encoding="utf-8") as fl:
        fl.write(result)


@step_by_step_print_executing_line_number_and_data
def run_program(test: bool | None = None
                ) -> None:
    """ register set of hotkeys and their corresponding functions, starts a keyboard listener of hotkeys presses
    >>> if not git_hub: run_program(test=True)
    """
    hotkeys: dict[str:Callable] = {  # Create a dictionary of hotkeys and functions
            # 'space + enter': _a_lot_of_new_single_card,
            # 'home': home_ai_answer_handling,
            'delete'            : home_add_single_phrase,
            'backspace + delete': delete_backspace_page_down_presser,
            'page down'         : page_down_ai_request_for_10_sentences_at_time,
            'ctrl + c + w'      : ctrl_c_w_request_for,  # return in clipboard template with copied word
            'ctrl + c + 3'      : ctrl_c_3_multi_translations,  # in clipboard up to 4 translations of the copied word
            'ctrl + c + q'      : ctrl_c_q_formatter,  # return in clipboard text without certain words
            'ctrl + 1'          : header_tab_mp3,  # get word , make and save mp3 and write refer of mp3
            'ctrl + 2'          : new_single_word_card,  # get cursor at answer field in 'add new card', before click
            'ctrl + 4'          : ctrl_4_open_google_image,  # open google image(s) with word(s) from clipboard
            }
    for hotkey, function in hotkeys.items():  # Register the hotkeys and their corresponding functions
        keyboard.add_hotkey(hotkey, function)
    if not test:
        keyboard.wait()  # Start the keyboard listener
