import pytest

from Source.tools import detect_language, star_separated_words_from, filter_lines, refers_mp3s, header_tab_mp3_content, \
    replace_non_english_letter


class Test:
    class TestDetectLanguage:
        def test_detect_language_english(self) -> None:
            assert detect_language('Hello, world!') == 'en'

        def test_detect_language_russian(self) -> None:
            assert detect_language('Привет, мир!') == 'ru'

        def test_detect_language_unsupported(self) -> None:
            with pytest.raises(ValueError, match='Input text cannot be empty.'):
                detect_language('')

    class TestReplaceNonEnglishLetter:
        def test_replace_non_english_letter(self):
            assert replace_non_english_letter("""SCUM_10131 _подонок, накипь, пена, мразь, пенка, тина
 * ОТБРОСЫ * МРАЗЬ * ПОДОНОК * НАКИПЕТЬ *

 
SCAM_9007 _мошенничество
 * МОШЕННИЧЕСТВО * МОШЕННИЧАТЬ * АФЕРА *""") == 'SCUM \n \n\n \nSCAM \n'

    # class TestStarSeparatedWordsFrom:
    #     def test_by_docktest_star_separated_words_from(self):
    #         assert star_separated_words_from('SCUM \\n \\n \\n \\nSCAM \\n') == ' * SCUM * SCAM * '


#         def test_heede_insteed_heeded(self):
#             assert star_separated_words_from("""HEED_7701 _внимание, осторожность
#
# heedless * ЛЕГКОМЫСЛЕННЫЙ * НЕБРЕЖНО * БЕСПЕЧНЫЙ *
#
# heeded * ПРИСЛУШАТЬСЯ * УСЛЫШАННЫЙ * ПРИСЛУШАЛСЯ * ПРИСЛУШИВАЛСЯ *
#
# heeding * ВНИМАТЕЛЕН * ВНИМАНИЕ * ПРИСЛУШИВАТЬСЯ * ПРИСЛУШИВАЯСЬ * """) == ' * HEED * heedless * heeded * heeding * '
#
#         def test_star_separated_russian_words(self):
#             assert star_separated_words_from(
#                 """SALIVA_9006 _слюна
#
# salivary * СЛЮНОТЕЧЕНИЕ * СЛЮНООТДЕЛЕНИЕ * К СЛЮНЕ * СЛЮННЫЕ ЖЕЛЕЗЫ *
#
# salivation * СЛЮНООТДЕЛЕНИЕ * ДО СЛЮНООТДЕЛЕНИЯ *
#
# SALINE_8131 _соляной, физиологический раствор, солончак, солевой раствор, солевой, соленый, соль
#
# SALT_2685 _соль, солить, соленый, соляной, поваренная соль, солевой, засаливать, засоленный, изюминка
#
#
# """
#             ) == ' * SALIVA * salivary * salivation * SALINE * SALT * '
#
#         def test_star_separated_words_from(self):
#             assert star_separated_words_from(
#                 f' * BLASPHEMY * blasphemous * blaspheme * blasphemer *\\n[sound:BLASPHEMY.mp3]\\n[sound:blasphemous.mp3]'
#             ) == ' * BLASPHEMY * blasphemous * blaspheme * blasphemer * '
#
#         def test_one_line_with_star(self):
#             assert star_separated_words_from(
#                 'CLOUT_5008 _клочок, обрывок, лоскут; сильный удар, затрещина; сильный удар в бейсболе;'
#             ) == ' * CLOUT * '
#
#         def test_invisible_space(self):
#             text = """COALESCE_11473 _сливаться, срастаться, слипаться, сходиться
#
# coalesced  слились  * СЛИЛСЯ * СЛИВАТЬСЯ * СЛИЛИСЬ * """
#             assert star_separated_words_from(text) == ' * COALESCE * coalesced * '
#
#         def test_strip(self):
#             assert star_separated_words_from(' * APPOSITE_11662 * ') == ' * APPOSITE * '
#
#         def test_one_line_no_russian(self):
#             assert star_separated_words_from('PUNDIT_8205 * УМНЫЙ * ЭКСПЕРТ * _пандит,ученый ') == ' * PUNDIT * '

    class TestFilterLines:
        def test_filter_lines(self):
            text = """Nouns:

Principal - Директор (Direktor)
Principals - Директоры (Direktory)
Principality - Княжество (Knyazhestvo)
Principals - Главные лица (Glavnye litsa)
Verbs:

Principal - Основной (Osnovnoy)
Adjectives:

Principal - Главный (Glavnyy)
Principled - Принципиальный (Principial'nyy)
Adverbs:

Principally - Преимущественно (Preimushchestvenno)
Popular phrases (proverbs) with the word 'principal' and their translations into Russian:

"The principal of success is hard work." - "Принцип успеха - тяжелая работа." (Printsip uspekha - tyazhelaya rabota)
"Stick to your principles." - "Придерживайтесь своих принципов." (Priderzhivaytes' svoykh printsipov)
"The principal aim is to learn." - "Главная цель - учиться." (Glavnaya tsel' - uchit'sya)
"Act with integrity, guided by your principles." - "Действуйте с честностью, руководствуясь своими принципами." (Deystvuyte s chestnost'yu, rukovodstvuyas' svoyimi printsipami)
"The principal role in this play is challenging." - "Главная роль в этой пьесе вызывает сложности." (Glavnaya rol' v etoy p'ese vyzyvaet slozhnosti)"""
            assert filter_lines(text) == """
Principal - Директор (Direktor)
Principals - Директоры (Direktory)
Principality - Княжество (Knyazhestvo)
Principals - Главные лица (Glavnye litsa)

Principal - Основной (Osnovnoy)

Principal - Главный (Glavnyy)
Principled - Принципиальный (Principial'nyy)

Principally - Преимущественно (Preimushchestvenno)

"The principal of success is hard work." - "Принцип успеха - тяжелая работа." (Printsip uspekha - tyazhelaya rabota)
"Stick to your principles." - "Придерживайтесь своих принципов." (Priderzhivaytes' svoykh printsipov)
"The principal aim is to learn." - "Главная цель - учиться." (Glavnaya tsel' - uchit'sya)
"Act with integrity, guided by your principles." - "Действуйте с честностью, руководствуясь своими принципами." (Deystvuyte s chestnost'yu, rukovodstvuyas' svoyimi printsipami)
"The principal role in this play is challenging." - "Главная роль в этой пьесе вызывает сложности." (Glavnaya rol' v etoy p'ese vyzyvaet slozhnosti)"""

    class TestRefersMp3s:
        def test_refers_mp3s(self):
            assert refers_mp3s(' * SALIVA * salivary * salivation * SALINE * SALT * ', save_file=-1) == [
                '[sound:SALIVA.mp3]', '[sound:salivary.mp3]', '[sound:salivation.mp3]', '[sound:SALINE.mp3]',
                '[sound:SALT.mp3]']

    class TestHeaderTabMp3Content:
        def test_header_tab_mp3_content(self):
            assert header_tab_mp3_content(test=' * TEST * TEST * TEST * TEST * ') == (
                ' * TEST * TEST * TEST * TEST * \n[sound:TEST.mp3]\n[sound:TEST.mp3]',
                '\n\n[sound:TEST.mp3]\n[sound:TEST.mp3]')

        def test_heeded_insteed_heede(self):
            assert header_tab_mp3_content(test=' * HEED * heedless * heeded * heeding * ') == (
            ' * heeded * heeding * HEED * heedless * \n[sound:heeded.mp3]\n[sound:heeding.mp3]',
            '\n\n[sound:HEED.mp3]\n[sound:heedless.mp3]')

        def test_error(self):
            assert header_tab_mp3_content(test=' * HEED * heedless * heeded * heeding * ') == (
            ' * heeded * heeding * HEED * heedless * \n[sound:heeded.mp3]\n[sound:heeding.mp3]',
            '\n\n[sound:HEED.mp3]\n[sound:heedless.mp3]')



def test_docktests_for_star_separated_words_from():
    """
    >>> star_separated_words_from('SCUM \\n \\n \\n \\nSCAM \\n')
    ' * SCUM * SCAM * '
    """

