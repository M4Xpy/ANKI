import os
import random
from typing import Optional

from gtts import gTTS


def uniq_name(input_string: str, seed_sign: int = None) -> str:
    """ Cut the input string if it is longer than 20 characters, and randomly doubled some character.
    >>> uniq_name("This is a test string.", seed_sign=1)
    'This is a  testt strinn'
    """
    if seed_sign:
        random.seed(seed_sign)
    # output_string = ""
    # for char in input_string[:20]:
    #     if random.random() < 0.5:
    #         output_string += char.upper()
    #     else:
    #         output_string += char.lower()
    # return output_string
    return ''.join([char + char if random.random() < 0.05 else char for char in input_string[:20]])


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


def generate_audio_file(input_string: str, save_file: Optional[int] = 0) -> Optional[str]:
    """Generates audio file of the input_string in its detected language."""
    folder = 'C:\\Users\\Я\\Desktop\\audio'                     # default directory
    lang = detect_language(input_string)                        # Detect language of the input_string
    audio_file_name = uniq_name(input_string) + '.mp3'          # Generate audio file name
    audio = gTTS(text=input_string, lang=lang, slow=False)      # Generate audio file
    audio_file_path = os.path.join(folder, audio_file_name)     # Save audio file to directory
    audio.save(audio_file_path)
    if not save_file:
        return audio_file_path
