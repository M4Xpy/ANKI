import pytest

from Source.tools import detect_language, star_separated_words_from, filter_lines


class Test:
    class TestDetectLanguage:
        def test_detect_language_english(self) -> None:
            assert detect_language('Hello, world!') == 'en'

        def test_detect_language_russian(self) -> None:
            assert detect_language('Привет, мир!') == 'ru'

        def test_detect_language_unsupported(self) -> None:
            with pytest.raises(ValueError, match='Input text cannot be empty.'):
                detect_language('')

    class TestStarSeparatedWordsFrom:
        def test_star_separated_words_from(self):
            assert star_separated_words_from(
                f' * BLASPHEMY * blasphemous * blaspheme * blasphemer *\\n[sound:BLASPHEMY.mp3]\\n[sound:blasphemous.mp3]'
            ) == ' * BLASPHEMY * blasphemous * blaspheme * blasphemer * '

        def test_one_line_with_star(self):
            assert star_separated_words_from(
                'CLOUT_5008 _клочок, обрывок, лоскут; сильный удар, затрещина; сильный удар в бейсболе;'
            ) == ' * CLOUT * '

        def test_invisible_space(self):
            text = """COALESCE_11473 _сливаться, срастаться, слипаться, сходиться

coalesced  слились  * СЛИЛСЯ * СЛИВАТЬСЯ * СЛИЛИСЬ * """
            assert star_separated_words_from(text) == ' * COALESCE * coalesced * '

        def test_strip(self):
            assert star_separated_words_from(' * APPOSITE_11662 * ') == ' * APPOSITE * '

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
