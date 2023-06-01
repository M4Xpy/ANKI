import re
from typing import Optional

file_path = 'C:\\Users\\Я\\Desktop\\D  .    3   .   1.txt', 'C:\\Users\\Я\\Desktop\\Все колоды.txt', \
            'C:\\Users\\Я\\Desktop\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\Карточки в простой текст.txt', \
            'E:\\test_txt.txt',


def find_mp3_refers(path_of_file: str) -> set[str]:
    """ find mp3 refers from *.txt anki file
    >>> sorted(find_mp3_refers(file_path[2]))
    ['ALCOVE.mp3', 'COVE.mp3', 'COVENANT.mp3', 'COVERT.mp3', 'COVET.mp3', 'OVERT.mp3', 'TENABLE.mp3']
    """
    words = set()
    omit = True
    with open(path_of_file, encoding="utf-8") as file:
        for part in file:
            for letter in part:
                if omit:
                    if letter == '[':
                        omit = False
                        word = '['
                else:
                    word = f'{word}{letter}'
                    if letter == ']':
                        omit = True
                        words.add(word.strip('[sound:]'))
    return words


def find_picture_refers(path_of_file: str) -> set[str]:
    """ find pictuare refers from *.txt anki file
    >>> sorted(find_picture_refers(file_path[2]))
    ['63544041144321.jpg', '64312840290305.jpeg', '65081639436289.png']
    """
    with open(path_of_file, encoding="utf-8") as file:
        return set(refer.strip('paste-"') for refer in re.findall('paste-.{20}', file.read()))
    #     content = file.read()
    #     snips = re.findall('paste-.{20}', content)
    #     pictures = set()
    #     for refer in snips:
    #         picture = refer.strip('paste-"')
    #         pictures.add(picture)
    # return pictures


def refers_finder(path_of_file: str, pattern: Optional[str] = '.{10}.mp3', cut: Optional[str] = '[sound:') -> set[str]:
    """ find refers by given pattern from given *.txt anki file
    >>> sorted(refers_finder(file_path[2]))
    ['ALCOVE.mp3', 'COVE.mp3', 'COVENANT.mp3', 'COVERT.mp3', 'COVET.mp3', 'OVERT.mp3', 'TENABLE.mp3']
    >>> sorted(refers_finder(file_path[2], pattern='paste-.{20}', cut='paste-"'))
    ['63544041144321.jpg', '64312840290305.jpeg', '65081639436289.png']
    """
    with open(path_of_file, encoding="utf-8") as file:
        return set(refer.strip(cut) for refer in re.findall(pattern, file.read()))
    #     content = file.read()
    #     snips = re.findall(pattern, content)
    #     files = set()
    #     for refer in snips:
    #         file = refer.strip(cut)
    #         files.add(file)
    # return files