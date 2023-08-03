# from Source.en_ru_srt_align import en_ru_var_data
from Source.letter_visual_length import visual_len


# return en_after, en_before, en_visual_before, en_word_visual_len, ru_after, ru_before, ru_visual_before, ru_word_visual_len


# ("So  even  if  Columbus  got  lost  and  wasn't  the  first  to  discover  America , ", ' ', 59, 318,
#  'Так  что  даже  если  Колумб  заблудился  и  не был  первым , открывшим  Америку , ', ' ', 59, 226)


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

    print(new_en_string)
    print(new_ru_string)
    print()
en_ru_var_data('I', " No , no , I  don't  want  to  keep  him .  I  don't . ", 'я', ' Нет , нет , я  не  хочу  оставлять  его  .  Я  не . ')
en_ru_var_data('want', " No , no ,    I  don't  want  to  keep  him .  I  don't . ", 'хочу', ' Нет , нет , я  не  хочу  оставлять  его  .  Я  не . ')
en_ru_var_data(
    'him', " No , no ,    I  don't  want  to  keep  him .  I  don't . ", 'его',
    ' Нет , нет , я  не     хочу  оставлять  его  .  Я  не . '
    )
en_ru_var_data('I', " No , no ,    I  don't  want  to  keep    him .  I  don't . ", 'Я', ' Нет , нет , я  не     хочу  оставлять  его  .  Я  не . ')
# print(
#         en_ru_var_data(
#             'test', 'testtest', " Why  don't  you  tell  testtest  about  it  in  the  morning ?  How  does  that  sound ? ",
#             'тест', ' Почему  бы  тебе  не сказать  тест  об  этом  утром ?  Как  это  звучит ? '
#             ),
# en_ru_var_data(
#             'test', 'testtest', " Why  don't  you  tell  testtest  about  it  in  the  morning ?  How  does  that  sound ? ",
#             'тесттест', ' Почему  бы  тебе  не сказать  тесттест  об  этом  утром ?  Как  это  звучит ? '
#             ),
# en_ru_var_data(
#             'test', 'testtest', " Why  don't  you  tell  testtest  about  it  in  the  morning ?  How  does  that  sound ? ",
#             'тест', ' Почему  тест  бы  тебе  не сказать  об  этом  утром ?  Как  это  звучит ? '
#             ),
# en_ru_var_data(
#             'test', 'testtest', " Why  don't  you  tell  testtest  about  it  in  the  morning ?  How  does  that  sound ? ",
#             'тесттест', ' Почему  тесттест  бы  тебе  не сказать  об  этом  утром ?  Как  это  звучит ? '
#             ),
# en_ru_var_data(
#             'test', 'test', " Why  don't  you  tell  test  about  it  in  the  morning ?  How  does  that  sound ? ",
#             'тесттест', ' Почему  бы  тебе  не сказать  тесттест  об  этом  утром ?  Как  это  звучит ? '
#             ),
# en_ru_var_data(
#             'test', 'test', " Why  don't  you  tell  test  about  it  in  the  morning ?  How  does  that  sound ? ",
#             'тест', ' Почему  бы  тебе  не сказать  тест  об  этом  утром ?  Как  это  звучит ? '
#             ),
# en_ru_var_data(
#             'test', 'test', " Why  don't  you  tell  test  about  it  in  the  morning ?  How  does  that  sound ? ",
#             'тесттест', ' Почему  тесттест  бы  тебе  не сказать  об  этом  утром ?  Как  это  звучит ? '
#             ),
# en_ru_var_data(
#             'test', 'test', " Why  don't  you  tell  test  about  it  in  the  morning ?  How  does  that  sound ? ",
#             'тест', ' Почему  тест  бы  тебе  не сказать  об  этом  утром ?  Как  это  звучит ? '
#             ),
#
#
#
#         sep="\n")
