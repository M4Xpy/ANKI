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

from Source.mp3name_detector import find_in_the

ai_request_for_sentence = 'Дайте мне популярные предложения параллельно с переводом на английский язык со словами'
new_data: str = ''
git_hub: str | None = os.getenv('GITHUB_ACTIONS')
count: list[int] = [0, 1]
start = True


def whether_test_mode():
    return True if not any([
        'PYTEST_CURRENT_TEST' in os.environ,
        '__pytest' in sys.modules,
        '__unittest' in sys.modules,
        'GITHUB_ACTIONS' in os.environ,
        'CI' in os.environ,
        'doctest' in sys.modules
    ]) else False


not_test = whether_test_mode()


def step_by_step_print_executing_line_number_and_data(func: Any) -> Any:
    """ Decorator that prints the executing line number and data.
    >>> run_program(True)
    """

    def wrapper(*args: tuple[Any, ...]) -> Any:
        if not_test:
            global count
            print(f'{count[0]:^3}  >>>  {inspect.currentframe().f_back.f_lineno:^3} >>> {args}')
            count[0] += 1
        return func(*args)

    return wrapper


@step_by_step_print_executing_line_number_and_data
def uniq_name(input_string: str,
              test: bool | None = False
              ) -> str:
    """ Cut the input string if it is longer than 20 characters, and randomly doubled some character.
    >>> uniq_name("This is a test string.", test=True)
    'This is a  testt strinn'
    """
    # check whether test or work mode
    if test:
        random.seed(test)
    # output_string: str = ""                        # save result in separate variable
    # for char in input_string[:20]:            # loop cutting to 20 signs string
    #     if random.random() < 0.05:            # 1 to 20 possibility of double sign
    #         output_string += char.upper()
    #     else:
    #         output_string += char.lower()     # 19 to 20 possibility of single sign
    # return output_string                      # #-lines fully equal last comprehension line
    return ''.join(char + char
                   if random.random() < 0.05
                   else char
                   for char in input_string[:20]
                   )


@step_by_step_print_executing_line_number_and_data
def detect_language(text: str) -> str:
    """
    >>> detect_language('если строка на русском')
    'ru'
    >>> detect_language('if string in english')
    'en'
    """
    return ('en', 'ru')[ord(text.strip()[1]) > 127]


@step_by_step_print_executing_line_number_and_data
def generate_audio_file(text: str,
                        save_file: int | None = 0,
                        language: str | None = ''
                        ) -> str | None:
    """Generates audio file of the input_string in its detected language.
    >>> generate_audio_file(text='test', save_file=-1, language='en')
    """
    text: str = text.lower()
    folder: str = ('C:\\Users\\Я\\Desktop\\audio',
                   f"C:\\Users\\Я\\Documents\\Anki\\1-й пользователь\\collection.media",
                   f"C:\\Users\\Я\\AppData\\Roaming\\Anki2\\User 1\\collection.media",
                   os.path.join(os.path.dirname(__file__), "..", "additional_data", "mp3s_for_tests"))[
        save_file]
    if not language:
        language = detect_language(text)  # Detect language of the input_string
    audio_file_name = f'{text}.mp3'  # Generate audio file name
    try:
        audio = gTTS(text=text, lang=language, slow=False)  # Generate audio file
        audio_file_path = os.path.join(folder, audio_file_name)  # Save audio file to directory
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
        text = pyperclip.paste()
    if len(text.splitlines()) > 1:
        text = star_separated_words_from(text)
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
    url = f'https://www.google.com/search?q={word}' \
          f'&tbm=isch&hl=en&tbs=itp:clipart&sa=X&ved=0CAIQpwVqFwoTCKCx4PzezvsCFQAAAAAdAAAAABAD&biw=1349&bih=625'
    webbrowser.open(url, new=new_page)


@step_by_step_print_executing_line_number_and_data
def open_google_translate(text: str) -> None:
    """ open google translated with received request
    >>> open_google_translate('test')
    """
    url = f'https://translate.google.com/?sl=en&tl=ru&text={text}%0A&op=translate'
    webbrowser.open(url, new=0, )


@step_by_step_print_executing_line_number_and_data
def request_for(text: str,
                template: str | None = 'ai'
                ) -> str:
    """ insert request text to template
    >>> request_for(' _1234TEST34567890', template='check')
    'This is a TEST'
    """
    # text = text.strip(' _1234567890')
    # result = get_template(template, text)
    # return result        # code above(for reading, debugging and refactoring) is the same steps as in under one-liner
    return get_template(template, text.strip(' _1234567890'))


@step_by_step_print_executing_line_number_and_data
def ctrl_c_w_request_for() -> None:
    """ return to the clipboard the text received from the clipboard, processed by request_for
    >>> ctrl_c_w_request_for()
    """
    return copy_func_paste(request_for)


@step_by_step_print_executing_line_number_and_data
def replace_non_english_letter(text: str) -> str:
    """
    >>> replace_non_english_letter('test-test\\n[sound:testy.mp3]')
    'test-test\n'
    """
    # text = text.replace('[sound:', ' ')
    # pattern = r"[^A-Za-z\n.]"
    # replaced_text = re.sub(pattern, " ", text)
    # splited_text = replaced_text.split(' ')
    # values = []
    # for item in splited_text:
    #     if item:
    #         if '.mp' not in item:
    #             values.append(item)
    # dot_result = ' '.join(values)
    # result = dot_result.replace('.', '')
    # return result
    return ' '.join(item
                    for item in re.sub(r"[^A-Za-z\n.-]", " ", text.replace('[sound:', ' ')
                                       ).split(' ')
                    if item and '.mp' not in item
                    ).replace('.', '')


# @step_by_step_print_executing_line_number_and_data
def star_separated_words_from(text: str) -> str:
    """ extract first word of each line, removing any digits or underscores from the word, and join them with asterisks
    >>> star_separated_words_from('test-test\\n[sound:test.mp3]')
    ' * test * '
    """
    text = replace_non_english_letter(text)
    lines = [line.split()[0]
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


# @step_by_step_print_executing_line_number_and_data
def header_tab_mp3_content(text: str) -> tuple[str, ...]:
    """
    >>> header_tab_mp3_content('test-test\\n[sound:test.mp3]') > ()
    True
    """
    header: str = star_separated_words_from(text)
    mp3refers: list[str] = refers_mp3s(header)
    len_mp3refers: int = -2 if len(mp3refers) > 3 else -(len(mp3refers) + 1)
    header = f" * {' * '.join(refer.removeprefix('[sound:').removesuffix('.mp3]') for refer in mp3refers[len_mp3refers:] + mp3refers[:len_mp3refers])} * "
    header = f"{header}\n{chr(10).join(mp3refers[len_mp3refers:])}"
    tab_mp3s_remainder = f"\n\n{chr(10).join(mp3refers[:len_mp3refers])}"
    return (header, tab_mp3s_remainder)


@step_by_step_print_executing_line_number_and_data
def refers_mp3s(header: str,
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
    answer, quuestion = new_single_word_card_content()
    keyboard.write(quuestion)
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
def if_error(doing: str | None = '_return',
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
    word = word.lower()
    translate_s: set[str | None] = set(
        en_ru_en_translator(f'{prefix} {word}', 'en').upper() for prefix in ('', 'the', 'to'))
    adjective: str = en_ru_en_translator(f'too {word}', 'en')
    translate_s.add(' '.join(word for word in adjective.split()[1:]).upper())
    return translate_s


@step_by_step_print_executing_line_number_and_data
def make_func_write(func: Callable[[str], str]
                    ) -> None:
    """ take data in clipboard , doing function , return result in clipboard"""
    # text = pyperclip.paste()
    # text = func(text)
    # keyboard.write(text)
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
    word_s_replace = word_s.replace(',', ' ')
    words_split = word_s_replace.split()
    for _word in words_split:
        word = _word.strip(' _1234567890')
        translations: set = translations_of_the(word)  # gives up to four translations of the word
        result: str = f"{_word} * {' * '.join(translations)} * "  # return star separated translations words
        result_s.append(result)
    result: str = '\n\n'.join(result_s)
    return result


@step_by_step_print_executing_line_number_and_data
def multi_translations(word_s: str) -> str:
    return '\n\n'.join(
        f"{word} * {' * '.join(translations_of_the(word.strip(' _1234567890')))} * "
        for word in word_s.replace(',', ' ').split()
    )


@step_by_step_print_executing_line_number_and_data
def press_keys(*args: float | str
               ) -> None:
    """ Presses the given keys with optional time delays
    Args: *args (float or str): The keys to press, with optional time abcdelays between consecutive key presses.
    Raises:TypeError: If any argument in *args is not a float or string.
    >>> press_keys(0.001)
    """
    for arg in args:
        time.sleep(arg) if isinstance(arg, float) else keyboard.send(arg)


@step_by_step_print_executing_line_number_and_data
def del_trash_lines_and_words(text: str,
                              del_lines: tuple[str, ...] | None = None,
                              del_words: tuple[str, ...] | None = None
                              ) -> str:
    """
    return text without lines with words from chek_s tuple, remove 'Translation:'
    >>> del_trash_lines_and_words("Nouns:\\r\\nT\\r\\proverb\\nE\\nproverbs\\nS\\nPlease note\\nT\\nTranslation:").replace('\\n', '')
    'TEST'
    """
    time.sleep(0.25)
    if not del_lines:
        del_lines = ('nouns:', 'verbs:', 'adjectives:', 'adverbs:', 'please note', 'phrases', 'None',
                     'Single-root nouns,', 'Noun:', 'Verb:', 'Adjective:', 'Adverb:')
    # filtered_lines: list[str] = []
    # for line in text.splitlines():
    #     if not any(check in line.lower() for check in chek_s):
    #         filtered_lines.append(line.replace('Translation:', ''))
    # result: str = '\n'.join(filtered_lines)
    # result: str = result.replace('Translation:', '')
    # return result
    return replace_all_exceptions_in(
        '\n'.join(line
                  for line in text.splitlines()
                  if not any(check.lower() in line.lower()
                             for check in del_lines
                             )
                  ),
        del_words)


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
            substitute = exception[1]
        text = text.replace(exception[0], substitute)
    while '\n\n\n' in text:
        text = text.replace('\n\n\n', '\n\n')
    return text


@step_by_step_print_executing_line_number_and_data
def copy_func_paste(func: Callable[[str], str]
                    ) -> None:
    """ return to the clipboard the text received from the clipboard, processed by the provided function """
    # input_text: str = pyperclip.paste()
    # output_text: str = func(input_text)
    # pyperclip.copy(output_text)
    pyperclip.copy(func(pyperclip.paste()))


@step_by_step_print_executing_line_number_and_data
def ctrl_c_q_formatter() -> None:
    """ take data from clipboard , filtered lines , return result to clipboard  """
    return copy_func_paste(del_trash_lines_and_words)


@step_by_step_print_executing_line_number_and_data
def get_template(template: str,
                 text: str
                 ) -> str:
    """ return chosen template with given word
    >>> get_template(template='check', text='test')
    'This is a test'
    """
    return {
        'ai': f"Provide popular phrases with word '{text}' , along with  translations into Russian\nProvide single-root"
              f" nouns, verbs, adjectives, adverbs for the word '{text}', along with translations into Russian.",
        'check': f"This is a {text}"

    }[template]


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
                    first = None
            except IndexError:
                raise IndexError('end of list')


@step_by_step_print_executing_line_number_and_data
def ai_request_list():
    global start
    today = date.today().day
    _31 = f'C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\ANKI_CARDS\\' \
          f'undone_anki_txt_format\\_31\\{today}.txt'
    _15 = f'C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\ANKI_CARDS\\' \
          f'undone_anki_txt_format\\_15\\{today}.txt'
    if start:
        start = False
        return sorted(find_in_the(_31, 'mp3_words'))


words_list = ai_request_list()


def ai_request_for_10_sentences_at_time_from():
    """

    """
    global words_list
    leno = len(words_list)
    if leno:
        share = (10, leno)[leno < 9]
        now_list = tuple(words_list[:share])
        words_list = words_list[share:]
        return f'{ai_request_for_sentence} {", ".join(now_list)}'


def page_down_ai_request_for_10_sentences_at_time():
    if words_list:
        pyperclip.copy(ai_request_for_10_sentences_at_time_from())
        press_keys(0.1, 'ctrl + v', 0.1, 'enter')


def home_ai_answer_handling():
    """
    >>> home_ai_answer_handling()
    """
    text = pyperclip.paste()
    lines = 'User', 'ChatGPT', ai_request_for_sentence
    gist = del_trash_lines_and_words(text, lines)
    print(gist)


def delete_backspace_page_down_presser():
    while words_list:
        time.sleep(4)
        page_down_ai_request_for_10_sentences_at_time()
        time.sleep(random.randint(100, 150))



@step_by_step_print_executing_line_number_and_data
def run_program(test: bool | None = None
                ) -> None:
    """ register set of hotkeys and their corresponding functions, starts a keyboard listener of hotkeys presses
    >>> if not git_hub: run_program(test=True)
    """
    hotkeys: dict[str:Callable] = {  # Create a dictionary of hotkeys and functions
        # 'space + enter': _a_lot_of_new_single_card,
        'backspace + delete': delete_backspace_page_down_presser,
        'home': home_ai_answer_handling,
        'page down': page_down_ai_request_for_10_sentences_at_time,
        'ctrl + c + w': ctrl_c_w_request_for,  # return in clipboard template with copied word
        'ctrl + c + 3': ctrl_c_3_multi_translations,  # return in clipboard up to 4 translations of the copied word
        'ctrl + c + q': ctrl_c_q_formatter,  # return in clipboard text without certain words
        'ctrl + 1': header_tab_mp3,  # get word , make and save mp3 and write refer of mp3
        'ctrl + 2': new_single_word_card,  # get cursor at the answer field in 'add new card', before click
        'ctrl + 4': ctrl_4_open_google_image,  # open google image(s) with word(s) from clipboard
    }
    for hotkey, function in hotkeys.items():  # Register the hotkeys and their corresponding functions
        keyboard.add_hotkey(hotkey, function)
    if not test:
        keyboard.wait()  # Start the keyboard listener
