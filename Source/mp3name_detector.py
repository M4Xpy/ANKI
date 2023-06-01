import re
from typing import Optional

file_path = 'E:\\test_txt.txt', \
            "..\\additional_data\\Карточки в простой текст.txt"


def refers_finder(path_of_file: str, pattern: Optional[str] = '.{10}.mp3', cut: Optional[str] = '[sound:') -> set[str]:
    """ find refers by given pattern from given *.txt anki file
    >>> sorted(refers_finder(file_path[1]))
    ['ALCOVE.mp3', 'COVE.mp3', 'COVENANT.mp3', 'COVERT.mp3', 'COVET.mp3', 'OVERT.mp3', 'TENABLE.mp3']
    >>> sorted(refers_finder(file_path[1], pattern='paste-.{20}', cut='paste-"'))
    ['63544041144321.jpg', '64312840290305.jpeg', '65081639436289.png']
    """
    with open(path_of_file, encoding="utf-8") as file:
        return set(refer.strip(cut) for refer in re.findall(pattern, file.read()))
    #     content = file.read()
    #     snips = re.findall(pattern, content)                                     # find snippets with certain pattern
    #     files = set()
    #     for refer in snips:
    #         file = refer.strip(cut)                                                 # cut out file-refer from snippet
    #         files.add(file)
    # return files     # commented code(for reading, debugging and refactoring) is the same steps as in above one-liner
