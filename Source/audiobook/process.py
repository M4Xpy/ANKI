import json
import time
import tkinter as tk

from googletrans import Translator

from Source.audiobook.texts_of_the_books.frankenstein import text_of_the_book_5
from Source.audiobook.texts_of_the_books.great_getsbey import text_of_the_book_6
from Source.audiobook.texts_of_the_books.pride_and_prejudice import text_of_the_book_4




def text_analyze(text):
    non_leters = ""
    for sign in text:
        if not sign.isalnum() and sign not in f"{non_leters} \n":
            non_leters = non_leters + sign
    print(f"non_leters = ' \\n{non_leters}'")
    print(f"_len = {len(text)}")

# text_analyze(text_of_the_book_5)

def divide_text_on_parts_and_save_as_list(text_of_book, name):
    signs = '?,.;!:'
    quote_s = '"([])'
    omit_signs = "' \n-—"
    change = "_"
    quote = 0
    part_s = [""]
    part = ""
    _n = 0
    divide = 80
    errors = ("&c.",)
    text_of_book = text_of_book.replace(
            "\n", ".", 2).replace("\n", " ").replace("Mr.", "Mr ").replace("Mrs.", "Mrs ").replace("*", "")
    for index, sign in enumerate(text_of_book[1:-1]):
        if not sign.isalnum() and sign not in f"{signs}{quote_s}{omit_signs}{change}":
            print((sign,))
        if sign in change:
            sign = "'"
        if sign in signs:
            part_s.append(part + sign)
            part = ""
        elif sign in omit_signs:
            part = part + sign
        elif sign in quote_s:
            if not quote:
                part_s.append(part)
                part = sign
                quote = 1
            else:
                part_s.append(part + sign)
                part = ""
                quote = 0
        elif sign == "\n":
            if text_of_book[index + 1] == "\n":
                part_s.append(part)
                part = ""
            else:
                part = part + " "
        elif sign == "-" and text_of_book[index + 1] == "-":
            part_s.append(part)
            part = ""
        elif sign == " " and text_of_book[index + 1]:
            part = part + sign
        else:
            part = part + sign
        part_s[-1] = part_s[-1].replace("    ", "  ").replace("  ", " ")
    part_s.append(part)
    result = []
    for part in part_s:
        if any(error in part for error in errors):
            continue
        if part.strip(f"{signs}{quote_s}{omit_signs}{change}"):
            part = part.strip()
            len_part = len(part)
            if len_part < divide:
                result.append(part)
            else:
                sentence = ""
                part_split = part.split()
                len_part = len(part)
                parts_count, remainder = divmod(len_part, divide)
                if remainder:
                    parts_count += 1
                longevity = len_part / parts_count

                for word in part_split:
                    if len(f"{sentence} {word}") < longevity:
                        sentence = f"{sentence} {word}"
                    else:
                        result.append(f"{sentence} {word}")
                        sentence = ""
                if sentence:
                    result.append(sentence)
        # if "END OF VOL." in part:
        #     break

    with open(f'../../Source/audiobook/texts_of_the_books/jsons_files/book_list_{name}.json', 'w', encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


divide_text_on_parts_and_save_as_list(text_of_the_book_6, "text_of_the_book_6")


def line_translate():
    with open('../../Source/audiobook/book_list.json', 'r', encoding="utf-8") as file:
        line_list = json.load(file)
    coef_limit = 0.25
    stock = 0
    top_words = {
            "who": [0, 0, 10, ['кто']], "the": [0, 0, 10, ['этот']], "a": [0, 0, 10, ['тот']], "an": [0, 0, 10, ['тот']]
            }
    # perm_index = 2535 + 2
    text_of_book_lower = text_of_book.lower()
    for line_number, line in enumerate(line_list[perm_index:], perm_index):
        if not line.strip("-' `?,.:;!\"'([])*"):
            continue
        ru_line = Translator().translate(line, 'ru', 'en').text
        ru_words = []
        en_words = []
        top_line = ""
        en_line = ""
        for word in line.split():
            en_words.append(word)
            word_lower = word.strip("-' `?,.:;!\"'([])*'").lower()

            if word_lower not in top_words:
                coef = text_of_book_lower.count(word_lower) / 1000
                if word_lower:
                    translations_of_the_word = [Translator().translate(word_lower, 'ru', 'en').text]
                    for item in [Translator().translate(f"too {word_lower}", 'ru', 'en').text.split()[-1],
                                 Translator().translate(f"the {word_lower}", 'ru', 'en').text,
                                 Translator().translate(f"to {word_lower}", 'ru', 'en').text]:
                        if item not in translations_of_the_word:
                            translations_of_the_word.append(item)
                else:
                    translations_of_the_word = [""]

                top_words[word_lower] = [line_number, 0.05, coef, translations_of_the_word]
                if coef > coef_limit:
                    print(f" {word} coef = {coef}")
            else:
                pre_line_number, occurence, coef, translations_of_the_word = top_words[word_lower]
                if coef < coef_limit:
                    if pre_line_number == line_number:
                        pre_line_number = 0
                    coef = (0.1 / (line_number - pre_line_number)) + occurence + coef
                    top_words[word_lower] = [line_number, occurence + 0.05, coef, translations_of_the_word]
            len_ru_word = len(translations_of_the_word[0])
            len_word_lower = len(word_lower)
            if len_word_lower < len_ru_word:
                stock += len_word_lower
            else:
                stock = 0

            if coef > coef_limit and stock:
                ru_words.append(" " * len(word))
            else:
                stock = 0
                ru_word = ""
                count = 0
                for ru in translations_of_the_word:
                    new_count = f" {ru_line} ".count(f" {ru} ")
                    if new_count > count:
                        ru_word = ru
                        count = new_count
                if not ru_word:
                    ru_word = translations_of_the_word[0]
                ru_words.append(ru_word.replace(' ', '_'))

        for index, en_word in enumerate(en_words):
            ru_word = ru_words[index]
            len_en = len(f"{en_line}{en_word}")
            len_ru = len(f"{top_line}{ru_word}")
            diff = len_en - len_ru
            if diff == 1:
                before = " "
                after = ""
            elif diff:
                before = after = " " * abs(diff // 2)

            if diff > 0:
                top_line = f"{top_line}{before}{ru_word}{after}"
                en_line = f"{en_line} {en_word}"
            elif diff < 0:
                top_line = f"{top_line} {ru_word}"
                en_line = f"{en_line}{before}{en_word}{after}"
            else:
                top_line = f"{top_line} {ru_word}"
                en_line = f"{en_line} {en_word}"
        ru_line = ru_line.replace(" ", f" {((len(en_line) - len(ru_line)) // max(ru_line.count(' '), 1)) * ' '}")
        three_line = [top_line, en_line, ru_line]
        print(top_line)
        print(en_line)
        print(ru_line)
        print(line_number - 1)

        with open('../../Source/audiobook/three_line_list.json', 'r', encoding="utf-8") as file:
            three_line_list = json.load(file)
            three_line_list.append(three_line)

        with open('../../Source/audiobook/three_line_list.json', 'w', encoding="utf-8") as file:
            json.dump(three_line_list, file, indent=4, ensure_ascii=False)


def combine_parts():
    with open('../../Source/audiobook/three_line_list.json', 'r', encoding="utf-8") as file:
        three_line_list = json.load(file)
    new_part_s = []
    chunk_words = ""
    chunk_en = ""
    chunk_ru = ""
    omit_next = 0
    sss = 0
    for index, (words, en, ru) in enumerate(three_line_list):
        print(index)
        max_len = max(len(words), len(en), len(ru))
        words = words.center(max_len)
        en = en.center(max_len)
        ru = ru.center(max_len)

        if len(f"{chunk_words} {words}") < 82:
            chunk_words = f"{chunk_words} {words}"
            chunk_en = f"{chunk_en} {en}"
            chunk_ru = f"{chunk_ru} {ru}"
        elif chunk_words:
            new_part_s.append([chunk_words, chunk_en, chunk_ru])
            chunk_words = words
            chunk_en = en
            chunk_ru = ru


    if chunk_words:
        new_part_s.append([chunk_words, chunk_en, chunk_ru])
    with open('../../Source/audiobook/ready_three_line_list.json', 'w', encoding="utf-8") as file:
        json.dump(new_part_s, file, indent=4, ensure_ascii=False)


def audio_book_player():
    global lines_zero_words, lines_zero, lines_zero_ru
    with open('../../Source/audiobook/ready_three_line_list.json', 'r', encoding="utf-8") as file:
        three_line_list = json.load(file)
        score = 0
        zero = " " * 105
        new_max = 0
        for (words, en, ru) in three_line_list:
            lines_zero_words, lines_zero, lines_zero_ru = (words, en, ru)
            time.sleep(2)
            # if len(words) > new_max:
            #     new_max = len(words)
            #     print(len(words), en,)
            #     lines_plus_three = f"{words}\n{en}\n{ru}\n{zero}"
            # else:
            #     lines_plus_three = f"{zero}\n{zero}\n{words}\n{en}\n{ru}\n{zero}\n{zero}"
            # print(lines_plus_three)
            # time.sleep(5)


def font_size(text):
    len_line = len(text)
    if len_line < 82:
        return 22, 81 * " "
    elif len_line < 87:
        return 20, 86 * " "
    elif len_line < 93:
        return 19, 92 * " "
    elif len_line < 99:
        return 18, 98 * " "
    elif len_line < 107:
        return 16, 106 * " "
    elif len_line < 115:
        return 15, 114 * " "
    elif len_line < 126:
        return 14, 125 * " "
    elif len_line < 138:
        return 13, 137 * " "
    else:
        return 11, 150 * " "


def show_zero(disposition="+0+306", colour='white', background="black"):
    global lines_zero, old_line
    old_line = lines_zero
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry(disposition)
    root.overrideredirect(True)  # Remove the window frame
    initial_font_size, len_line = font_size(lines_zero) # Initial font size calculation
    label = tk.Label(root, text=f"{len_line}\n{lines_zero}\n{len_line}", font=('Courier New', initial_font_size), fg=colour, bg=background)
    label.pack()

    def update_text():
        # Update font size dynamically
        global old_line
        if old_line != lines_zero:
            old_line = lines_zero
            current_font_size, len_line = font_size(old_line)
            to_show = f"{len_line}\n{old_line}\n{len_line}"
            label.config(text=to_show, font=('Courier New', current_font_size))
        root.after(10, update_text)

    update_text()
    root.mainloop()


if __name__ == '__main__':
    # Example usage:
    # lines_zero = "Your text goes here"
    # show_zero()

    # measure_line = "         1         2         3         4         5         6         7         8         9         0         1         2         3         4         5         6         7         8         9         0\n12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
    # central_line = " " * 79 + "a"
    # threading.Thread(target=show_zero).start()
    # audio_book_player()
    pass



