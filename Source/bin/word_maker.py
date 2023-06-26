from datetime import date

from Source.mp3name_detector import find_in_the

start = True


def ai_request_list():
    global start
    today = date.today().day
    file = f'C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\ANKI_CARDS\\MONTH\\{today}.txt'
    if start:
        start = False
        return sorted(find_in_the(file, 'mp3_words'))


def ai_request_for_10_sentences_at_time_from():
    """

    """
    global words_list
    leno = len(words_list)
    if leno:
        share = (10, leno)[leno < 9]
        now_list = words_list[:share]
        words_list = words_list[share:]
        return f'provide popular phrase with following words, with a translation into Russian, ' \
               f'highlighting these words and their corresponding-translation-words in a sentence with an uppercase.\n' \
               f'{now_list}'


if __name__ == '__main__':
    words_list = ai_request_list()
    print(ai_request_for_10_sentences_at_time_from())
    print(ai_request_for_10_sentences_at_time_from())
    print(ai_request_for_10_sentences_at_time_from())
    print(ai_request_for_10_sentences_at_time_from())
    print(ai_request_for_10_sentences_at_time_from())
