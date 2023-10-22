import json

from googletrans import Translator

from Source.srt_player_2.three_line_online_player import top_5000, top_2000, top_300

text = """("Thank goodness. If I wasn't, this'd probably never work.", ' xxxxxx', "Thank goodness. IF I WASN'T, this'd probably never work.", "Thank goodness. this'd probably never work.", True)
('And that was without even a single drop of rum.', ' xxxxxx', 'And that was without even a single drop of rum.', 'And that was without even a single drop of rum.', False)
"""


def add_to_stat():
    global count
    with open('../../tests/exceptions/word_dict.json', 'r', encoding="utf-8") as file:
        stat = json.load(file)

    stat_5000 = {}
    stat_0000 = {}
    for word in stat.keys():
            translations, rate, pos, absolute_count, relative_count, level = stat[word]
            rate = 300 if word in top_300 else 2000 if word in top_2000 else 5000 if word in top_5000 else 12500 if word in stat else 99999
            if rate > 5000:
                stat_5000[word] = (translations, rate, pos, absolute_count, relative_count, level)
            else:
                stat_0000[word] = (translations, rate, pos, absolute_count, relative_count, level)


    for line in text.splitlines():
        words = line.lstrip("('\"").split(" xxxxxx")[0]
        len_words = 1 / len(words)
        for word in words.split():
            word = "".join(letter.lower() for letter in word if letter.isalpha() or letter in "'-")
            rate = 300 if word in top_300 else 2000 if word in top_2000 else 5000 if word in top_5000 else 12500 if word in stat else 99999
            if rate < 99999 and word in stat:
                translations, rate, pos, absolute_count, relative_count, level = stat[word]
                values = (translations, rate, pos, absolute_count + 1, relative_count + len_words, level)
            else:
                translations = Translator().translate(word.lower(), 'ru', 'en').text
                values = (translations, rate, "ZERO", 1, len_words, 111)

            if rate > 5000:
                stat_5000[word] = values
            else:
                stat_0000[word] = values

    sorted_5000 = sorted(stat_5000.items(), key=lambda x: x[1][4], reverse=True)
    sorted_0000 = sorted(stat_0000.items(), key=lambda x: x[1][4], reverse=True)
    sorted_5000 = dict(sorted_5000)
    sorted_0000 = dict(sorted_0000)
    total = sorted_5000 | sorted_0000

    with open('../../tests/exceptions/word_dict.json', 'w', encoding="utf-8") as file:
        json.dump(total, file, indent=4, ensure_ascii=False)


add_to_stat()
