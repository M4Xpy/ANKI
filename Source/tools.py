import os
import random
import time
import traceback
import webbrowser
from typing import Optional, Union

import keyboard as keyboard
import pyperclip
from googletrans import Translator
from gtts import gTTS


def uniq_name(input_string: str, seed_sign: int = None) -> str:
    """ Cut the input string if it is longer than 20 characters, and randomly doubled some character.
    >>> uniq_name("This is a test string.", seed_sign=1)
    'This is a  testt strinn'
    """
    # check whether test or work mode
    if seed_sign:
        random.seed(seed_sign)
    # output_string = ""                        # save result in separate variable
    # for char in input_string[:20]:            # loop cutting to 20 signs string
    #     if random.random() < 0.05:            # 1 to 20 possibility of double sign
    #         output_string += char.upper()
    #     else:
    #         output_string += char.lower()     # 19 to 20 possibility of single sign
    # return output_string                      # #-lines fully equal last comprehension line
    return ''.join(char + char if random.random() < 0.05 else char for char in input_string[:20])


def detect_language(text: str) -> str:
    """
    >>> detect_language('если строка на русском')
    'ru'
    >>> detect_language('if string in english')
    'en'
    >>> detect_language("                    ")
    Traceback (most recent call last):
        ...
    ValueError: Input text cannot be empty.
    """
    if text := text.strip():
        return ('en', 'ru')[any(ord(char) > 127 for char in text)]
    raise ValueError('Input text cannot be empty.')


def generate_audio_file(text: str, save_file: Optional[int] = 0, lang: Optional[str] = None) -> Optional[str]:
    """Generates audio file of the input_string in its detected language."""
    text = text.lower()
    folder = ('C:\\Users\\Я\\Desktop\\audio', f"C:\\Users\\Я\\Documents\\Anki\\1-й пользователь\\collection.media",
              f"C:\\Users\\Я\\AppData\\Roaming\\Anki2\\User 1\\collection.media")[
        save_file]
    if not lang:
        lang = detect_language(text)  # Detect language of the input_string
    audio_file_name = f'{text}.mp3'  # Generate audio file name
    try:
        audio = gTTS(text=text, lang=lang, slow=False)  # Generate audio file
        audio_file_path = os.path.join(folder, audio_file_name)  # Save audio file to directory
        audio.save(audio_file_path)
        if not save_file:
            return audio_file_path
    except:
        return "audio_file_failed._Check_your_network_connection_and_try_again."


def en_ru_en_translator(input_text: str, lang: Optional[str] = None) -> str:
    """
    >>> en_ru_en_translator('apple')
    'яблоко'
    >>> en_ru_en_translator('яблоко')
    'apple'
    """
    out_of, onto = {'ru': ('ru', 'en'), 'en': ('en', 'ru')}[lang or detect_language(input_text)]
    try:
        return Translator().translate(input_text, src=out_of, dest=onto).text
    except :
        return "Translation_failed._Check_your_network_connection_and_try_again."


def ctrl_4_open_google_image(text: Optional[str] = '') -> None:
    """ open google image with received request """
    if not text:
        text = pyperclip.paste()
    if len(text.splitlines()) > 1:
        text = star_separated_words_from(text)
    if '*' in text:
        for word in text.replace('*', '').split()[::-1]:
            open_google_image(word)
    else:
        open_google_image(text.strip('_1234567890'))


def open_google_image(word: str) -> None:
    """ open google image with received request  """
    url = f'https://www.google.com/search?q={word}' \
          f'&tbm=isch&hl=en&tbs=itp:clipart&sa=X&ved=0CAIQpwVqFwoTCKCx4PzezvsCFQAAAAAdAAAAABAD&biw=1349&bih=625'
    webbrowser.open(url, new=0)


def open_google_translate(text: str) -> None:
    """ open google translated with received request """
    url = f'https://translate.google.com/?sl=en&tl=ru&text={text}%0A&op=translate'
    webbrowser.open(url, new=0, )


def request_for(text: str, template: Optional[str] = 'ai') -> str:
    """ insert request text to template
    >>> request_for(' _1234TEST34567890', template='check')
    'This is a TEST'
    """
    # text = text.strip(' _1234567890')
    # result = get_template(template, text)
    # return result                           # code above(for reading and refactoring) is the same code as under
    return get_template(template, text.strip(' _1234567890'))


def ctrl_c_w_request_for() -> None:
    return copy_func_paste(request_for)


def star_separated_words_from(text: str) -> str:
    """ extract first word of each line, removing any digits or underscores from the word, and join them with asterisks
    >>> star_separated_words_from('one , two\\n\\nthree , four\\nfive , six')
    ' * one * three * five * '
    >>> star_separated_words_from(' * MENACING * [sound:Menacer.mp3]')
    ' * MENACING * '
    """
    lines = [line.split()[0].strip('_1234567890') for line in text.splitlines() if line.strip() and '.mp3' not in line]
    if len(lines) < 2 and '*' in text:
        return f" * {' * '.join(word.strip('_1234567890') for word in text.split() if '*' not in word and '.mp3' not in word)} * "
    return f" * {' * '.join(lines)} * "


def header_tab_mp3() -> None:
    """write star_separated_words press tab and at the end of the page write mp3 refers"""
    press_keys("ctrl + a", 0.1)
    header = star_separated_words_from(new_data)
    keyboard.write(header)
    if header.count('*') > 2:
        press_keys(.25, 'tab', .25, "ctrl + end")
    time.sleep(.25)
    mp3_and_refer_from(header)
    ctrl_4_open_google_image(header)


def mp3_and_refer_from(header: str) -> None:
    """ make mp3s and write its refers """
    mp3refers = refers_mp3s(header)
    keyboard.write(f'\n\n{mp3refers}')


def refers_mp3s(header: str) -> str:
    """ make mp3 reference
    # >>> refers_mp3s('test')[:-1]
    # '[sound:test.mp3]'
    """
    word_s = header.strip(' *').split(' * ')
    mp3refers = ''
    for word in word_s:
        generate_audio_file(word, save_file=1, lang='en')
        mp3refers += f'[sound:{word}.mp3]\n'
    return mp3refers


def new_single_word_card() -> None:
    """ save old card , then made new card ready to save """
    try:
        press_keys(0.25, 'tab', 0.25, 'tab', 0.25, 'enter')
        in_text = pyperclip.paste()
        word = in_text.split()[0].split()[0].strip('_1234567890')
        keyboard.write(f" * {word} *[sound:{word}.mp3]")
        press_keys(0.25, 'tab')
        keyboard.write(f'\n * {" * ".join(word for word in translations_of_the(word))} *\n\n')
        time.sleep(0.1)
        keyboard.send("ctrl + v")
    except IndexError:
        where_error('wrong hotkey ?', in_text)
    except:
        where_error('unknown error provoked following data', in_text)


def where_error(report, *args):
    """ """
    traceback.print_exc()
    for arg in args:
        report = f"{report} , {arg=}"
    print(report)


def translations_of_the(word: str) -> set:
    """ Give different variants of word tranlation
    >>> translations_of_the('ADJOIN')
    {'ПРИМЫКАТЬ'}
    """
    word = word.lower()
    translate_s = set(
        en_ru_en_translator(input_text=f'{prefix} {word}', lang='en').upper() for prefix in ('', 'the', 'to'))
    adjective = en_ru_en_translator(input_text=f'too {word}', lang='en')
    translate_s.add(' '.join(word for word in adjective.split()[1:]).upper())
    time.sleep(0.25)
    return translate_s


def ctrl_c_3_multi_translations():
    return copy_func_paste(multi_translations)


def multi_translations(word: str) -> str:
    """ return star separated translated vars of getted word
    >>> multi_translations('ADJOIN')
    'ADJOIN * ПРИМЫКАТЬ * '
    >>> assert multi_translations('ABLE_299') == 'ABLE * В СОСТОЯНИИ * СПОСОБНЫЙ * ' or 'ABLE * СПОСОБНЫЙ * В СОСТОЯНИИ * '
    """
    # word = word.strip(' _1234567890')                                                  # return 'ABLE' from 'ABLE_299'
    # translations = translations_of_the(word)                               # gives up to four translations of the word
    # result = f"{word} * {' * '.join(map(str, translations))} * "                  # return star separated translations words
    # return result                                             #  one-liner below is full clone of above commented code
    return f"{word} * {' * '.join(map(str, translations_of_the(word.strip(' _1234567890'))))} * "


def press_keys(*args: Union[float, str]) -> None:
    """ Presses the given keys with optional time delays
    Args: *args (float or str): The keys to press, with optional time abcdelays between consecutive key presses.
    Raises:TypeError: If any argument in *args is not a float or string.
    >>> press_keys()
    """
    for arg in args:
        time.sleep(arg) if isinstance(arg, float) else keyboard.send(arg)


def filter_lines(text: str) -> str:
    """
    return text without lines with words from chek_s tuple, remove 'Translation:'
    >>> filter_lines("T\\nproverb\\nE\\nproverbs\\nS\\nPlease note\\nT\\nTranslation:").replace('\\n', '')
    'TEST'
    """
    # chek_s = ('proverb', 'please note', 'phrases')
    # filtered_lines = []
    # for line in text.splitlines():
    #     if not any(check in line.lower() for check in chek_s):
    #         filtered_lines.append(line)
    # result = '\n'.join(filtered_lines)
    # result = result.replace('Translation:', '')
    # return result
    return '\n'.join(line for line in text.splitlines() if not any(
        check in line.lower() for check in ('proverb', 'please note', 'phrases'))).replace('Translation:', '')


def copy_func_paste(func) -> None:
    """ return to the clipboard the text received from the clipboard, processed by the provided function """
    # text = pyperclip.paste()
    # text = func(text)
    # pyperclip.copy(text)
    pyperclip.copy(func(pyperclip.paste()))


def ctrl_c_q_formatter():
    return copy_func_paste(filter_lines)


def get_template(template: str, text: str) -> str:
    """
    >>> get_template(template='check', text='test')
    'This is a test'
    """
    return {
        'ai': f"Provide single-root words and forms for the word '{text}' , along with popular phrases(better proverbs)  that directly include these single-root words and their translations into Russian.",
        'check': f"This is a {text}"

    }[template]


def ctrl_5_get_data_from_damge_card():
    """ """
    count = 0
    press_keys('ctrl + a', 0.2)
    keyboard.write(f'{count}')
    count += 1
    press_keys('tab', 0.2, 'ctrl + a', 0.2, 'ctrl + c')


def ctrl_8_new_card_from_damage_card():
    """ """
    press_keys(0.25, 'tab', 0.25, 'tab', 0.25, 'enter')
    header_tab_mp3()
    press_keys(0.25, 'page up', 0.25, 'page up', 0.25, 'ctrl + v')

def ctrl_a_listener():
    """ """
    global new_data
    old_data = pyperclip.paste()
    time.sleep(0.1)
    press_keys('ctrl + c', 0.1)
    new_data = pyperclip.paste()
    time.sleep(0.1)
    pyperclip.copy(old_data)



def run_program():
    """ register set of hotkeys and their corresponding functions, starts a keyboard listener of hotkeys presses
    """
    hotkeys = {  # Create a dictionary of hotkeys and functions
        'ctrl + a': ctrl_a_listener,
        'ctrl + c + w': ctrl_c_w_request_for,  # return in clipboard template with copied word
        'ctrl + c + 3': ctrl_c_3_multi_translations,  # return in clipboard up to 4 translations of the copied word
        'ctrl + c + q': ctrl_c_q_formatter,  # return in clipboard text without certain words
        'ctrl + 1': header_tab_mp3,  # get word , make and save mp3 and write refer of mp3
        'ctrl + 2': new_single_word_card,  # get cursor at the answer field in 'add new card', before click
        'ctrl + 4': ctrl_4_open_google_image,  # open google image(s) with word(s) from clipboard
        # 'ctrl + 5': ctrl_5_get_data_from_damge_card,  # my private case
        # 'ctrl + 8': ctrl_8_new_card_from_damage_card,  # my private case
    }
    for hotkey, function in hotkeys.items():  # Register the hotkeys and their corresponding functions
        keyboard.add_hotkey(hotkey, function)
    keyboard.wait()  # Start the keyboard listener


if __name__ == '__main__':
    pass
