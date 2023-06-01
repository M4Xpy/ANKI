import re

file_path = 'E:\\test_txt.txt', 'C:\\Users\\Я\\Desktop\\D  .    3   .   1.txt', 'C:\\Users\\Я\\Desktop\\Все колоды.txt', \
            'C:\\Users\\Я\\Desktop\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\Карточки в простой текст.txt'


def find_mp3_resfers(path_of_file: str) -> set[str]:
    # """ find mp3 refers from *.txt anki file
    # >>> sorted(find_mp3_resfers(file_path[-1]))
    # ['ALCOVE.mp3', 'COVE.mp3', 'COVENANT.mp3', 'COVERT.mp3', 'COVET.mp3', 'OVERT.mp3', 'TENABLE.mp3']
    # """
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


def find_pictuare_refers(path_of_file: str) -> set[str]:
    """ find pictuare refers from *.txt anki file
    >>> find_pictuare_refers(file_path[-1])
    """
    pictuares = set()
    text = '<img src=""paste-'
    pictuare = ''
    with open(path_of_file, encoding="utf-8") as file:
        content = file.read()
        res = re.findall("<img src=.{29} />", content)
        while res:
            res = res[0]
            pictuares.add(res)
            content = content.replace(res, '')
            res = re.findall("<img src=.{29} />", content)

        # for part in file:
        #     for letter in part:
        #         if not pictuare:
        #             if text[-17:] == text:
        #                 pictuare = f'{pictuare}{letter}'
        #         else:
        #             if pictuare.count('"') > 2:
        #                 pictuares.add(pictuare)
        #             else:
        #                 pictuare = f'{pictuare}{letter}'
    return pictuares
