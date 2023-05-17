import os
import random
import time
import webbrowser
from typing import Optional, Union

import keyboard as keyboard
import pyperclip
from googletrans import Translator
from gtts import gTTS

from Source.templates import get_template


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
    return ''.join([char + char if random.random() < 0.05 else char for char in input_string[:20]])


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
    folder = ('C:\\Users\\Я\\Desktop\\audio', f"C:\\Users\\Я\\Documents\\Anki\\1-й пользователь\\collection.media")[
        save_file]
    if not lang:
        lang = detect_language(text)  # Detect language of the input_string
    audio_file_name = uniq_name(text) + '.mp3'  # Generate audio file name
    audio = gTTS(text=text, lang=lang, slow=False)  # Generate audio file
    audio_file_path = os.path.join(folder, audio_file_name)  # Save audio file to directory
    audio.save(audio_file_path)
    if not save_file:
        return audio_file_path


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
    except AttributeError:
        raise Exception("Translation failed. Check your network connection and try again.")


def open_google_image(text: Optional[str] = '') -> None:
    if not text:
        text = pyperclip.paste()
    for text in f'{text} gif', text:
        url = f'https://www.google.com/search?q={text}&tbm=isch&hl=en&tbs=itp:clipart&sa=X&ved=0CAIQpwVqFwoTCKCx4PzezvsCFQAAAAAdAAAAABAD&biw=1349&bih=625'
        webbrowser.open(url, new=0)


def open_google_translate(text: str) -> None:
    url = f'https://translate.google.com/?sl=en&tl=ru&text={text}%0A&op=translate'
    webbrowser.open(url, new=0, )

def request_for(text: str, template: Optional[str] = 'ai') -> str:
    """
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
    """
    return f" * {' * '.join(line.split()[0].strip('_1234567890') for line in text.splitlines() if line and '.mp3' not in line)} * "


def make_anki_card() -> None:
    header = pyperclip.paste()
    header = star_separated_words_from(header)
    keyboard.write(header)
    press_keys(.25, 'tab', .25)
    mp3_and_refer_from(header)


def mp3_and_refer_from(header):
    mp3refers = refers_mp3s(header)
    keyboard.send("ctrl + end")
    keyboard.write(mp3refers)


def refers_mp3s(header: str) -> str:
    """
    >>> refers_mp3s('test')[:-1]
    '[sound:test.mp3]'
    """
    word_s = header.strip(' *').split(' * ')
    mp3refers = ''
    for word in word_s:
        generate_audio_file(word, save_file=1, lang='en')
        mp3refers += f'[sound:{word}.mp3]\n'
    return mp3refers


def new_single_word_card() -> None:
    press_keys(0.25, 'tab', 0.25, 'tab', 0.25, 'enter')
    in_text = pyperclip.paste()
    word = in_text.split()[0].split()[0].strip('_1234567890')
    keyboard.write(f" * {word} *[sound:{word}.mp3]")
    press_keys(0.25, 'tab')
    keyboard.write(f'\n * {" * ".join(word for word in translations_of_the(word))} *\n\n')
    time.sleep(0.1)
    keyboard.send("ctrl + v")


def translations_of_the(word):
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

def ctrl_c_q_multi_translations():
    return copy_func_paste(multi_translations)


def multi_translations(word: str) -> str:
    """
    >>> assert multi_translations('ABLE_299') == ' * В СОСТОЯНИИ * СПОСОБНЫЙ * ' or ' * СПОСОБНЫЙ * В СОСТОЯНИИ * '
    """
    # word = word.strip(' _1234567890')
    # translations = translations_of_the(word)
    # result = f" * {' * '.join(word for word in translations)} * "
    # return result
    return f" * {' * '.join(word for word in translations_of_the(word.strip(' _1234567890')))} * "


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
    # chek_s = ('proverb', 'proverbs', 'Please note')
    # filtered_lines = []
    # for line in text.splitlines():
    #     if not any(check in line for check in chek_s):
    #         filtered_lines.append(line)
    # result = '\n'.join(filtered_lines)
    # result = result.replace('Translation:', '')
    # return result
    return '\n'.join(line for line in text.splitlines() if not any(
        check in line for check in ('proverb', 'proverb', 'Please note'))).replace('Translation:', '')


def copy_func_paste(func):
    """ return to the clipboard the text received from the clipboard, processed by the provided function """
    # text = pyperclip.paste()
    # text = func(text)
    # pyperclip.copy(text)
    pyperclip.copy(func(pyperclip.paste()))


def ctrl_c_3_formatter():
    return copy_func_paste(filter_lines)


def run_program():
    """ register set of hotkeys and their corresponding functions, starts a keyboard listener of hotkeys presses
    """
    # Create a dictionary of hotkeys and functions
    hotkeys = {
        'ctrl + c + w': ctrl_c_w_request_for,
        'ctrl + c + q': ctrl_c_q_multi_translations,
        'ctrl + c + 3': ctrl_c_3_formatter,
        'ctrl + 2': new_single_word_card,
        'ctrl + 0': make_anki_card,
        'ctrl + 4': open_google_image,

    }
    # Register the hotkeys and their corresponding functions
    for hotkey, function in hotkeys.items():
        keyboard.add_hotkey(hotkey, function)
    # Start the keyboard listener
    keyboard.wait()


if __name__ == '__main__':
    run_program()
