import json

from googletrans import Translator

from Source.srt_player_2.three_line_online_player import top_5000, top_2000, top_300

text = """
"""


def add_to_stat():
    global count
    with open('../../tests/exceptions/word_dict.json', 'r', encoding="utf-8") as file:
        stat = json.load(file)
    stat_5000 = {}
    stat_0000 = {}
    for word in stat.keys():
            translations, rate, pos, absolute_count, relative_count, level = stat[word]
            if rate > 5000:
                stat_5000[word] = (translations, rate, pos, 0, 0, level)
            else:
                stat_0000[word] = (translations, rate, pos, 0, 0, level)

    sorted_5000 = sorted(stat_5000.items(), key=lambda x: x[1][4], reverse=True)
    sorted_0000 = sorted(stat_0000.items(), key=lambda x: x[1][4], reverse=True)
    sorted_5000 = dict(sorted_5000)
    sorted_0000 = dict(sorted_0000)
    total = sorted_5000 | sorted_0000

    # sorted_stat_items = sorted(stat.items(), key=lambda x: (x[1][1] < 5001, x[1][4]))
    # sorted_stat = dict(sorted_stat_items)
    with open('../../tests/exceptions/word_dict.json', 'w', encoding="utf-8") as file:
        json.dump(total, file, indent=4, ensure_ascii=False)


add_to_stat()
