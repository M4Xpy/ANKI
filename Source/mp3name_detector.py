from Source.tools import translations_of_the

file_path = 'E:\\test_txt.txt'

def find_words_with_letter_combinations(file_path: str) -> set[str]:
    words = set()
    ommit = True
    with open(file_path, encoding="utf-8") as file:
        for part in file:
            for letter in part:
                if ommit:
                    if letter == '[':
                        ommit = False
                        word = '['
                else:
                    word = f'{word}{letter}'
                    if letter == ']':
                        ommit = True
                        words.add(word)
    return words




text = """word = word.strip(' _1234567890')
translations = translations_of_the(word)
result = f" * {' * '.join(word for word in translations)} * "
return result"""


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
    return result

