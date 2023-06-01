
def one_line_code_compressor(code: str):
    """ Make one-line code from many-line code
    >>> print(one_line_code_compressor(text))
    return f" * {' * '.join(word.strip(' _1234567890') for word in translations_of_the(word))} * "
    """
    result = ''
    for line in reversed(code.splitlines()):
        if ' = ' in line:
            result = result.replace(*line.split(' = '), 1)
        else:
            result = f"{line}{result}"
    return result.strip(' \n')



text = """
word = word.strip(' _1234567890')
translations = translations_of_the(word)
result = f" * {' * '.join(word for word in translations)} * "
return result"""


def test1():
    """
    >>> test1()
    return f" * {' * '.join(word.strip(' _1234567890') for word in translations_of_the(word))} * "
    """
    print(one_line_code_compressor(text))


text2 = """
header = star_separated_words_from(new_data)
mp3refers = refers_mp3s(header)
len_mp3refers = -2 if len(mp3refers) > 3 else -(len(mp3refers) + 1)
"""


def test2():
    """
    >>> test2()
    return f" * {' * '.join(word.strip(' _1234567890') for word in translations_of_the(word))} * "
    """
    print(one_line_code_compressor(text2))