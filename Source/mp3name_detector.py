import os
import re

file_path = 'E:\\test_txt.txt', \
            os.path.join(os.path.dirname(__file__), "..", "additional_data", "Карточки в простой текст.txt")


def find_in_the(path_of_file: str,
                content: str | None = None,
                pattern: str | None = None,
                cut_prefix: str | None = None,
                cut_suffix: str | None = None,
                cut_before: str | None = None
                ) -> set[str | None]:
    """ find refers by given pattern from given *.txt anki file
    >>> sorted(find_in_the(file_path[1], 'mp3', pattern='.{15}.mp3'))
    ['ALCOVE.mp3', 'COVE.mp3', 'COVENANT.mp3', 'COVERT.mp3', 'COVET.mp3', 'OVERT.mp3', 'TENABLE.mp3']
    >>> sorted(find_in_the(file_path[1], content='image_refers'))
    ['63544041144321.jpg', '64312840290305.jpeg', '65081639436289.png']
    """
    pattern, cut_prefix, cut_suffix, cut_before = {
        None: (pattern, cut_prefix, cut_suffix, cut_before),
        'mp3_words': ('.{15}.mp3', None, '.mp3', ':'),
        'mp3': ('.{15}.mp3', None, None, ':'),
        'image_refers': ('paste-.{20}', 'paste-"', '" ', None),

    }[content]
    with open(path_of_file, encoding="utf-8") as file:
        return set(map(lambda refer: refer.lstrip(cut_prefix).rstrip(cut_suffix).split(cut_before)[-1],
                       re.findall(pattern, file.read()
                                  )
                       )
                   )
