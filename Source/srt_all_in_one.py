import os
import random
import time

import keyboard as keyboard
import pyperclip
from googletrans import Translator
from gtts import gTTS
import json

from Source.multi_google_translate import sss

def sort_exist_json_dict(json_dict):
    with open(json_dict, encoding='utf-8') as words_set_file:
        raw_set = json.load(words_set_file)
        print(len(sorted(raw_set)))
        new_total_set = {}
        for key in sorted(raw_set):
            new_total_set[key] = raw_set[key]
    with open(json_dict, 'w', encoding='utf-8') as words_set_file:
        words_set_file.write(json.dumps(new_total_set, ensure_ascii=False, indent=1))
    print(len(sorted(new_total_set)))




def en_wors_set_filler(from_file, result_name):
    new_total_set = {}
    from_file = f"C:\\Users\\Я\\Desktop\\films\\{from_file}.json"
    result_name = f"C:\\Users\\Я\\Desktop\\films\\{result_name}.json"
    total_dictionary = f"C:\\Users\\Я\\Desktop\\films\\ru_words_total_dictionary.json"

    with open(from_file, encoding='utf-8') as from_filewords_set_file:
        from_set = json.load(from_filewords_set_file)

    with open(total_dictionary, encoding='utf-8') as words_set_file:
        the_total_dictionary = json.load(words_set_file)

    for words in from_set.items():
        xxx = set(word.lower() for word in words[1])
        now_word = words[0]
        print(now_word)
        if now_word not in the_total_dictionary:
            print(111)
            if xxx:
                print(222)
                add = sss(now_word)
                for ad in add:
                    if ad not in xxx:
                        print(333)
                        xxx.add(ad)

                new_total_set[now_word] = list(xxx)
                print(now_word, 888, xxx)
    new_total_set |= the_total_dictionary

    with open(result_name, "w", encoding='utf-8') as words_set_file:
        words_set_file.write(json.dumps(new_total_set, ensure_ascii=False, indent=1))
    print(len(sorted(new_total_set)))









def en_words_set(film):
    srt = f"C:\\Users\\Я\\Desktop\\films\\{film}_2.txt"
    words_set_json = f"C:\\Users\\Я\\Desktop\\films\\words_set.json"
    with open(srt, encoding='utf-8') as srt_file:
        subtitles = srt_file.read()
    with open(words_set_json, encoding='utf-8') as words_set_file:
        total_set = json.load(words_set_file)
        print(total_set)
    subtitles = subtitles.split('\n\n')
    for subtitle in subtitles:
        subtitle = subtitle.splitlines()[3]
        words = subtitle.split()
        for word in words:
            word = word.replace('i>', '').strip('!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~0123456789»«').lower()
            if word and word not in total_set:
                translated_word = Translator().translate(word, 'en', 'ru').text
                total_set[word] = [translated_word]
                print(word, translated_word)
    with open(words_set_json, 'w', encoding='utf-8') as en_set:
        json.dump(total_set, en_set, ensure_ascii=False)


def write_audio(film, begin='00:00:00.000'):
    file = f"C:\\Users\\Я\\Desktop\\films\\{film}_2.txt"
    folder = f"C:\\ANKIsentences\\films\\{film}"
    with open(file, encoding='utf-8') as srt:
        text = srt.read()
    subtitles = text.split('\n\n')
    for subtitle in subtitles:
        subtitle = subtitle.splitlines()
        mp3name = subtitle[1][:8].replace(':', '_') + '.mp3'
        ru_sentence = subtitle[4] if len(subtitle) > 4 else ""
        if subtitle[1][:12] > f"{f'{begin}'[:9]}000":
            if ru_sentence:
                print(ru_sentence, mp3name)
                audio: gTTS = gTTS(text=ru_sentence, lang='ru', slow=False)  # Generate audio file
                audio_file_path: str = os.path.join(folder, mp3name)  # Save audio file to directory
                audio.save(audio_file_path)
                time.sleep(random.randint(1, 2))


def new_count(film_name):
    new_srt = f"C:\\Users\\Я\\Desktop\\films\\{film_name}_2.txt"
    w_ru = f"C:\\Users\\Я\\Desktop\\films\\{film_name}_3.txt"
    with open(new_srt, 'w+', encoding='utf-8') as srt:
        text = srt.read()
        subtitles = text.split('\n\n')
        for number, subtitle in enumerate(subtitles, 1):
            _, *content, ru = subtitle.splitlines()
            new_subtitles = f"\n\n{number}\n{content}\n{ru}\n{ru}"
            with open(w_ru, 'a+', encoding='utf-8') as w_ru_file:
                w_ru_file.write(new_subtitles)


def translate_srt(film_name):
    srt = f"C:\\Users\\Я\\Desktop\\films\\{film_name}.txt"
    new_srt = f"C:\\Users\\Я\\Desktop\\films\\{film_name}_2.txt"
    with open(srt, encoding='utf-8') as srt:
        text = srt.read()
    subtitles = text.split('\n\n')
    for number, subtitle in enumerate(subtitles):
        subtitle = subtitle.splitlines()
        on_text = ' '.join(subtitle[2:])

        translated = Translator().translate(on_text, 'ru', 'en').text
        print(translated)
        new_subtitles = f"\n\n{number}\n{subtitle[1].replace(',', '.')}\n{on_text}\n{translated}\n"
        with open(new_srt, 'a+', encoding='utf-8') as new_srt_file:
            new_srt_file.write(new_subtitles)


def dot_join():
    while True:
        keyboard.wait("ctrl + x")
        time.sleep(0.1)
        text = pyperclip.paste()
        before, after = text.split('\r\n\r\n')
        before1, before2, *before3 = before.split('\r\n')
        if type(before3) == list:
            before3 = ' '.join(before3)
        before_start, before_stop = before2.split(' --> ')
        after1, after2, *after3 = after.splitlines()
        if type(after3) == list:
            after3 = ' '.join(after3)
        after_start, after_stop = after2.split(' --> ')
        keyboard.write(f"{before1}\n{before_start} --> {after_stop}\n{before3.rstrip('.')} {after3.lstrip('.')}")


if __name__ == '__main__':
    # dot_join()
    # translate_srt('hatico')
    # new_count()
    # write_audio('hatico')
    # en_words_set('hatico')
    # en_wors_set_filler()
    # sort_exist_json_dict(f"C:\\Users\\Я\\Desktop\\films\\words_set.json")
    en_wors_set_filler("words_set" , "words_set2")
    pass
