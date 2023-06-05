import pytest

from Source.tools import detect_language, filter_lines, refers_mp3s, header_tab_mp3_content


class Test:
    class TestDetectLanguage:
        def test_detect_language_english(self) -> None:
            assert detect_language('Hello, world!') == 'en'

        def test_detect_language_russian(self) -> None:
            assert detect_language('Привет, мир!') == 'ru'

        def test_detect_language_unsupported(self) -> None:
            with pytest.raises(ValueError, match='Input text cannot be empty.'):
                detect_language('')

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
        def test_0306(self):
            assert header_tab_mp3_content(test="""relays * РЕЛЕ * К РЕЛЕ * 

relaid * МНОГО * ПЕРЕСКАЗАТЬ * ПЕРЕДАННЫЙ * РЕЛЕ * 

relayed * РЕТРАНСЛИРУЕМЫЙ * РЕТРАНСЛИРУЕТСЯ * ПЕРЕДАННЫЙ * ПЕРЕДАВАТЬ * 

relaying   ретрансляция""") == (' * relayed * relaying * relays * relaid * \n[sound:relayed.mp3]\n[sound:relaying.mp3]',
                                '\n\n[sound:relays.mp3]\n[sound:relaid.mp3]')

        def test_header_tab_mp3_content(self):
            assert header_tab_mp3_content(test=' * TEST * TEST * TEST * TEST * ') == (
                ' * TEST * TEST * TEST * TEST * \n[sound:TEST.mp3]\n[sound:TEST.mp3]',
                '\n\n[sound:TEST.mp3]\n[sound:TEST.mp3]')

        def test_heeded_insteed_heede(self):
            assert header_tab_mp3_content(test=' * HEED * heedless * heeded * heeding * ') == (
                ' * heeded * heeding * HEED * heedless * \n[sound:heeded.mp3]\n[sound:heeding.mp3]',
                '\n\n[sound:HEED.mp3]\n[sound:heedless.mp3]')

        def test_error(self):
            assert header_tab_mp3_content(test='test[sound:test.mp3]') == (' * test * \n[sound:test.mp3]', '\n\n')
