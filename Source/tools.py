import random


def uniq_name(input_string: str, seed_sign: int = None) -> str:
    """ Cut the input string if it is longer than 20 characters, and randomly change the case of each character.
    >>> uniq_name("This is a test string.", seed_sign=1)
    'ThiS Is A tEsT sTriN'
    >>> uniq_name("A short string", seed_sign=1)
    'A sHORt STrInG'
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
