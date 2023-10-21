import json

from googletrans import Translator

from Source.srt_player_2.three_line_online_player import top_2000, top_300

text = """
"""


def add_to_stat():
    global count
    with open('../../tests/exceptions/word_dict.json', 'r', encoding="utf-8") as file:
        stat = json.load(file)

    exclusions = []
    for key in stat.keys():
        if key in f"{top_2000} {top_300}":
            exclusions.append(key)
    for exclusion in exclusions:
        del stat[exclusion]

    for line in text.splitlines():
        words = line.lstrip("('\"").split(" xxxxxx")[0]
        for word in words.split():
            word = "".join(letter.lower() for letter in word if letter.isalpha() or letter in "'-")
            if word not in f"{top_2000} {top_300}":
                if word in stat:
                    count, level, translations = stat[word]
                    stat[word] = (count + 1 , level, translations)
                else:
                    translations = Translator().translate(word.lower(), 'ru', 'en').text
                    if translations.islower():
                        stat[word] = (1, 1, translations)
    sorted_stat_items = sorted(stat.items(), key=lambda x: (x[1][1], x[1][0]), reverse=True)
    sorted_stat = dict(sorted_stat_items)
    with open('../../tests/exceptions/word_dict.json', 'w', encoding="utf-8") as file:
        json.dump(sorted_stat, file, indent=4, ensure_ascii=False)


add_to_stat()
