import json

from googletrans import Translator

from Source.srt_player_2.three_line_online_player import top_5000, top_2000, top_300


def take_text_from_stat_txt():
    file = "C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\tests\\exceptions\\stat.txt"
    with open(file, "r", encoding='utf-8') as vars:
        return vars.read()

def clean_stat_txt():
    file = "C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\tests\\exceptions\\stat.txt"
    with open(file, "w", encoding='utf-8') as vars:
        vars.write("")


text = """
"""


def add_to_stat():
    global count
    text = take_text_from_stat_txt()
    with open('../../tests/exceptions/word_dict.json', 'r', encoding="utf-8") as file:
        stat = json.load(file)

    count_all_words = stat["hIsToRyYrOtSiH"][4]
    new_words = []
    for line in text.splitlines():
        words = line.lstrip("('\"").split("xxxxxx',")[0]
        for word in words.split():
            word = word.lower()
            word = "".join(letter for letter in word if letter in "'-abcdefghijklmnopqrstuvwxyz").removesuffix("'s"
                                                                                                    ).strip("'-")
            if word:
                new_words.append(word)
    count_all_words += len(new_words)

    stat_5000 = {}
    stat_0000 = {}
    for word in stat.keys():
        translations, rate, pos, absolute_count, relative_count, _ = stat[word]
        level = (111, 0)[translations.isupper()]
        rate = 300 if word in top_300 else 2000 if word in top_2000 else 5000 if word in top_5000 else 12500 if word in stat else 99999
        if rate > 5000 and level == 111:
            stat_5000[word] = (translations, rate, pos, absolute_count, absolute_count / count_all_words, level)
        else:
            stat_0000[word] = (translations, rate, pos, absolute_count, absolute_count / count_all_words, level)



    for word in new_words:

        rate = 300 if word in top_300 else 2000 if word in top_2000 else 5000 if word in top_5000 else 12500 if word in stat else 99999
        if rate < 99999 and word in stat:
            translations, rate, pos, absolute_count, relative_count, level = stat[word]
            values = (translations, rate, pos, absolute_count + 1, (absolute_count + 1) / count_all_words, level)
        else:
            if word in stat_5000:
                translations = stat_5000[word][0]
            elif word in stat_0000:
                translations = stat_0000[word][0]
            else:
                translations = Translator().translate(word.lower(), 'ru', 'en').text
                print(translations)
            level = (111, 0)[translations.isupper()]
            values = (translations, rate, "ZERO", 1, 1 / count_all_words, level)


        if rate > 5000 and level == 111:
            stat_5000[word] = values
        else:
            stat_0000[word] = values






    stat_5000["hIsToRyYrOtSiH"] = ("HISTORY", 99999, 99999, 0, count_all_words, 111)

    sorted_5000 = sorted(stat_5000.items(), key=lambda x: x[1][4], reverse=True)
    sorted_0000 = sorted(stat_0000.items(), key=lambda x: x[1][4], reverse=True)
    sorted_5000 = dict(sorted_5000)
    sorted_0000 = dict(sorted_0000)
    total = sorted_5000 | sorted_0000

    print(sum(1 for item in total.values() if item[3] > 0)) # demonstrate amount of used words

    with open('../../tests/exceptions/word_dict.json', 'w', encoding="utf-8") as file:
        json.dump(total, file, indent=4, ensure_ascii=False)

    clean_stat_txt()


add_to_stat()
