import os
import random
import webbrowser
from typing import Optional

import keyboard as keyboard
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


def generate_audio_file(text: str, save_file: Optional[int] = 0) -> Optional[str]:
    """Generates audio file of the input_string in its detected language."""
    folder = ('C:\\Users\\Я\\Desktop\\audio', f"C:\\Users\\Я\\Documents\\Anki\\1-й пользователь\\collection.media")[
        save_file]
    lang = detect_language(text)  # Detect language of the input_string
    audio_file_name = uniq_name(text) + '.mp3'  # Generate audio file name
    audio = gTTS(text=text, lang=lang, slow=False)  # Generate audio file
    audio_file_path = os.path.join(folder, audio_file_name)  # Save audio file to directory
    audio.save(audio_file_path)
    if not save_file:
        return audio_file_path


def en_ru_en_translator(input_text: str) -> str:
    """
    >>> en_ru_en_translator('apple')
    'яблоко'
    >>> en_ru_en_translator('яблоко')
    'apple'
    """
    out_of, onto = {'ru': ('ru', 'en'), 'en': ('en', 'ru')}[detect_language(input_text)]
    try:
        return Translator().translate(input_text, src=out_of, dest=onto).text
    except AttributeError:
        raise Exception("Translation failed. Check your network connection and try again.")


def open_google_image(text: str) -> None:
    url = f'https://www.google.com/search?q={text}&tbm=isch&hl=en&tbs=itp:clipart&sa=X&ved=0CAIQpwVqFwoTCKCx4PzezvsCFQAAAAAdAAAAABAD&biw=1349&bih=625'
    webbrowser.open(url, new=0)


def open_google_translate(text: str) -> None:
    url = f'https://translate.google.com/?sl=en&tl=ru&text={text}%0A&op=translate'
    webbrowser.open(url, new=0, )


def run_program():
    """ register set of hotkeys and their corresponding functions, starts a keyboard listener of hotkeys presses """
    # Create a dictionary of hotkeys and functions
    hotkeys = {

    }
    # Register the hotkeys and their corresponding functions
    for hotkey, function in hotkeys.items():
        keyboard.add_hotkey(hotkey, function)
    # Start the keyboard listener
    keyboard.wait()


if __name__ == '__main__':
    pass
