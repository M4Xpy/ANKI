import os
import random
from typing import Optional

from gtts import gTTS


def uniq_name(input_string: str, seed_sign: int = None) -> str:
    """ Cut the input string if it is longer than 20 characters, and randomly change the case of each character.
    >>> uniq_name("This is a test string.", seed_sign=1)
    'ThiS Is A tEsT sTriN'
    """
    random.seed(seed_sign)
    # output_string = ""
    # for char in input_string[:20]:
    #     if random.random() < 0.5:
    #         output_string += char.upper()
    #     else:
    #         output_string += char.lower()
    # return output_string
    return ''.join([char.upper() if random.random() < 0.5 else char.lower() for char in input_string[:20]])


def detect_language(text: str) -> str:
    """
    >>> detect_language('если строка на русском')
    'ru'
    >>> detect_language('if string in russian')
    'en'
    """
    if text:
        if any(ord(char) > 127 for char in text):
            return 'ru'
        else:
            return 'en'
    raise ValueError('Input text cannot be empty.')


def generate_audio_file(input_string: str, directory: Optional[str] = None) -> Optional[str]:
    """Generates audio file of the input_string in its detected language."""
    directory = 'C:\\Users\\Я\\Desktop\\audio'
    # Detect language of the input_string
    lang = detect_language(input_string)

    # Generate audio file name
    audio_file_name = uniq_name(input_string) + '.mp3'

    # Generate audio file
    audio = gTTS(text=input_string, lang=lang, slow=False)

    # Save audio file to directory
    audio_file_path = os.path.join(directory, audio_file_name)
    audio.save(audio_file_path)
    if not directory:
        return audio_file_path


generate_audio_file('все ок')
