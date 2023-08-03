import time
from difflib import SequenceMatcher

from Source.letter_visual_length import visual_len
from Source.multi_google_translate import sss
from Source.tools import translations_of_the, step_by_step_print_executing_line_number_and_data
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import json




film = "hatico"



old_srt = f"C:\\Users\\Я\\Desktop\\films\\{film}\\{film}_2.txt"
new_srt = f"C:\\Users\\Я\\Desktop\\films\\{film}\\{film}_en_ru_align_{''.join(time.ctime().split()[1:3])}.txt"

new_word_set = f"C:\\Users\\Я\\Desktop\\films\\ru_words_total_dictionary_{''.join(time.ctime().split()[1:3])}.json"
all_words = f"C:\\Users\\Я\\Desktop\\films\\ru_words_total_dictionary.json"
draft = "C:\\Users\\Я\\Desktop\\draft.txt"



@step_by_step_print_executing_line_number_and_data
def has_similar_word(word, word_list):
    if word in word_list:
        return word, word, 1
    thresh = len(word)
    threshold = {
            0 : 0.999,
            1 : 0.999,
            2 : 0.999,
            3 : 0.999,
            4 : 0.74999,
            5 : 0.79,
            6 : 0.66,
            7 : 0.71,
            8 : 0.62,
            9 : 0.65,
            10: 0.69,

            }[thresh] if thresh < 11 else 0.63

    word_lower = word.lower()  # Convert the word to lowercase for a case-insensitive comparison
    if type(word_list) == str:
        word_list = [word_list]

    vars = "", "", 0
    for item in word_list:
        item_lower = item.lower()  # Convert the list item to lowercase for a case-insensitive comparison

        # Calculate the similarity ratio between the two words
        similarity_ratio = SequenceMatcher(None, word_lower, item_lower).ratio()

        if similarity_ratio == 1:
            return item, word, similarity_ratio
        if similarity_ratio > max(vars[2], threshold):
            vars = item, word, similarity_ratio
    return vars


# @step_by_step_print_executing_line_number_and_data
def srt_list_from_srt(path):
    with open(path, encoding='utf-8') as old_srt:
        text = old_srt.read()
        return text.split('\n\n')

# @step_by_step_print_executing_line_number_and_data
def word_punctuator(word):
    # """
    # # >>> assert word_punctuator("?,.ap'ple.,?") == "?,. ap'ple .,?"
    # >>> word_punctuator(",")
    # """
    cut = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~0123456789«»'
    prefix = ""
    suffix = ""
    while word and word[0] in cut and word[1:]:
        prefix = f"{prefix}{word[0]}"
        word = word[1:]

    while word and word[-1] in cut and word[1:]:
        suffix = f"{word[-1]}{suffix}"
        word = word[:-1]

    return f"{prefix} {word} {suffix}".strip()


def replace_all(text, *patterns):
    for pattern in patterns:
        text = text.replace(f"  {pattern}  ", f"  {pattern} ")
    return text



# @step_by_step_print_executing_line_number_and_data
def unpack(subtitle):
    ru_string, ru_string_lower_words = '', ''
    cut = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~0123456789»«'
    subtitle = subtitle.splitlines()
    en_string =  ''.join(f" {word_punctuator(word)} " for word in subtitle[2].replace('<i>', '').replace('</i>', '').split())


    en_words = []
    en_words_lower = ['in', 'to', 'a', 'an', 'the', '!', '?', ',', "'", '"', ":"]
    for word in en_string.split():
        if word.lower() not in en_words_lower:
            en_words.append(word)
            en_words_lower.append(word.lower())



    ru_string = ''.join(f" {word_punctuator(word)} " for word in subtitle[3].replace('<i>', '').replace('</i>', '').split()).replace(' ,  ', ' , ')

    ru_string_words = []
    ru_string_words_lower = ['!', '?', ',', "'", '"', ":", 'и', 'не',  'в',  'но',  'на',  'ни',  'к', 'до',  'ко']
    for word in ru_string.split():
        if word.lower() not in ru_string_words_lower:
            ru_string_words.append(word)
            ru_string_words_lower.append(word.lower())
    print(ru_string_words, en_words)
    if len(subtitle) > 4:
        return en_string, en_words, ru_string, ru_string_words, subtitle[1], subtitle[4] + '\n'
    return en_string, en_words, ru_string, ru_string_words, subtitle[1], ""






# @step_by_step_print_executing_line_number_and_data
def en_ru_anligner(old_srt, new_srt):
    with open(all_words, encoding='utf-8-sig') as words_set_file:
        all_words_set = json.load(words_set_file)

    absent = {}
    subtitles = srt_list_from_srt(old_srt)
    for sub_id, subtitle in enumerate(subtitles[:]):   # 78 , 105 , 146, 163 , 208 , 243 , 274 , 329 ЮЮ
        en_var_lower = ""

        en_string, en_words, ru_string, ru_string_words, timing, mp3  = unpack(subtitle)
        empty = max(abs(len(en_words) - len(ru_string_words)), 4)
        for ru_string_word in ru_string_words:
            ru_string_word_lower = ru_string_word.lower()
            if ru_string_word_lower not in all_words_set:
                absent_set = sss(ru_string_word_lower)
                absent[ru_string_word_lower] = absent_set
                all_words_set[ru_string_word_lower] = absent_set

            not_1 = 0
            for en_var in all_words_set.get(ru_string_word_lower, ""):
                en_var_lower = en_var.lower()
                _0, _1, _2 = has_similar_word(en_var_lower, (en_words[:empty]))
                if _2 > not_1:
                    en_word, en_var_lower, not_1 = _0, _1, _2

                if not_1 < 1:
                    continue
                # print(en_word, ru_string_word, en_words[:empty])

                if en_var_lower:
                    en_string, ru_string = en_ru_var_data(
                            en_word, en_string, ru_string_word, ru_string
                            )
                    en_words.remove(en_word)
                    break
            empty += (not bool(en_var_lower))
        with open(new_srt, "a", encoding='utf-8') as xxx:
            xxx.write(f"{sub_id}\n{timing}\n{en_string}\n{ru_string}\n{mp3}\n")

    all_words_set |= absent
    res_res = {}
    for word in sorted(all_words_set):
        res_res[word] = all_words_set[word]



    # with open(new_word_set, "w" , encoding='utf-8') as words_set_file:
    #     words_set_file.write(json.dumps(res_res, ensure_ascii=False, indent=1))
    # print(len(sorted(res_res)))






# @step_by_step_print_executing_line_number_and_data
def align_subtitles(en_after, en_before, en_string, en_visual_before, en_word, en_word_visual_len, ru_after, ru_before,
                    ru_string, ru_visual_before, ru_word_visual_len
                    ):
    en_add, ru_add, en_add_before, ru_add_before, en_word_add, ru_word_add = "", "", 0, 0, 0, 0
    if abs(ru_visual_before - en_visual_before) > 29:
        difference_before = round(abs(ru_visual_before - en_visual_before) / 59)
        en_add_before, ru_add_before = ((difference_before, 0),
                                        (0, difference_before))[
            ru_visual_before == min(ru_visual_before, en_visual_before)]
    if abs(ru_word_visual_len - en_word_visual_len) > 29:
        difference_before = round((abs(ru_word_visual_len - en_word_visual_len) / 59) / 2)
        en_word_add, ru_word_add = ((difference_before, 0),
                                    (0, difference_before))[
            ru_word_visual_len == min(ru_word_visual_len, en_word_visual_len)]
    if en_add_before and ru_word_add:
        if en_add_before > ru_word_add:
            en_add = (en_add_before - ru_word_add) * " "
        else:
            ru_add = (ru_word_add - en_add_before) * " "
    if ru_add_before and en_word_add:
        if ru_add_before > en_word_add:
            ru_add = (ru_add_before - en_word_add) * " "
        else:
            en_add = (en_word_add - ru_add_before) * " "
    else:
        en_add = (en_add_before + en_word_add) * " "
        ru_add = (ru_word_add + ru_add_before) * " "
    ru_string = f"{ru_before}{ru_add}{ru_after}"
    en_string = f"{en_before}{en_add}{en_after}"
    # print(en_string)
    # print(en_word, )
    # print(ru_string)
    return en_string, ru_string

@step_by_step_print_executing_line_number_and_data
def en_ru_var_data(en_ru_var, en_string, ru_word, ru_string):

    ru_before, ru_after = ru_string.split(f" {ru_word} ", 1)
    en_before, en_after = en_string.split(f" {en_ru_var} ", 1)

    ru_start = visual_len(ru_before)
    en_start = visual_len(en_before)

    ru_word_visual_len = visual_len(f" {ru_word}")
    en_word_visual_len = visual_len(f" {en_ru_var}")

    while ru_start > en_start + 59:
        if en_start + en_word_visual_len + 59 > ru_start + ru_word_visual_len:
            break
        en_before = en_before + " "
        en_start = visual_len(en_before)

    while en_start > ru_start + 59:
        if en_start + en_word_visual_len < ru_start + ru_word_visual_len + 59:
            break
        ru_before = ru_before + " "
        ru_start = visual_len(ru_before)

    new_ru_string = f"{ru_before} {ru_word} {ru_after}"
    new_en_string = f"{en_before} {en_ru_var} {en_after}"

    return new_en_string, new_ru_string


if __name__ == '__main__':
    en_ru_anligner(old_srt, new_srt)

