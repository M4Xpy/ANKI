from Source.tools import detect_language, filter_lines, uniq_name, refers_mp3s, header_tab_mp3_content, \
    generate_audio_file


class Test:
    # class Test:
    #     def test_(self):
    #         input_ = INPUT
    #         output = OUTPUT
    #         assert FUNCTION == OUTPUT

    class TestUniqName:
        def test_2(self):
            input_ = "one two three"
            output = 'one two thhree'
            assert uniq_name(input_, True) == output

        def test_uniq_name(self):
            input_ = "This is a test string."
            output = 'This is a  testt strinn'
            assert uniq_name(input_, True) == output

    class TestDetectLanguage:
        def test_detect_language_english(self) -> None:
            input_ = 'Hello, world!'
            output = 'en'
            assert detect_language(input_) == output

        def test_detect_language_russian(self) -> None:
            input_ = 'Привет, мир!'
            output = 'ru'
            assert detect_language(input_) == output

    class TestGenerateAudioFile:
        def test_generate_audio_file(self):
            input_ = 'test'
            output = None
            assert generate_audio_file(input_, -1, 'en') == output

    class TestFilterLines:
        def test_filter_lines(self):
            input_ = """Nouns:

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
            output = """
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
            assert filter_lines(input_) == output

        def test_6462(self):
            input_ = """Nouns:\r\n\r\nBeneath - под (preposition), низ (noun)\r\nExample: "The treasure lies beneath the surface." - Сокровище находится под поверхностью.\r\nVerbs:\r\n\r\nNone\r\nAdjectives:\r\n\r\n"""
            output = """\nBeneath - под (preposition), низ (noun)\nExample: "The treasure lies beneath the surface." - Сокровище находится под поверхностью.\n\n"""
            assert filter_lines(input_) == output

    class TestRefersMp3s:
        def test_refers_mp3s(self):
            input_ = ' * SALIVA * salivary * salivation * SALINE * SALT * '
            output = ['[sound:SALIVA.mp3]', '[sound:salivary.mp3]', '[sound:salivation.mp3]', '[sound:SALINE.mp3]',
                      '[sound:SALT.mp3]']
            assert refers_mp3s(input_, -1) == output

    #
    class TestHeaderTabMp3Content:
        def test_0306(self):
            input_ = """relays * РЕЛЕ * К РЕЛЕ *

relaid * МНОГО * ПЕРЕСКАЗАТЬ * ПЕРЕДАННЫЙ * РЕЛЕ *

relayed * РЕТРАНСЛИРУЕМЫЙ * РЕТРАНСЛИРУЕТСЯ * ПЕРЕДАННЫЙ * ПЕРЕДАВАТЬ *

relaying   ретрансляция"""
            output = (' * relayed * relaying * relays * relaid * \n[sound:relayed.mp3]\n[sound:relaying.mp3]',
                      '\n\n[sound:relays.mp3]\n[sound:relaid.mp3]')
            assert header_tab_mp3_content(input_) == output

        def test_header_tab_mp3_content(self):
            input_ = ' * TEST * TEST * TEST * TEST * '
            output = (
                ' * TEST * TEST * TEST * TEST * \n[sound:TEST.mp3]\n[sound:TEST.mp3]',
                '\n\n[sound:TEST.mp3]\n[sound:TEST.mp3]')
            assert header_tab_mp3_content(input_) == output

        def test_heeded_insteed_heede(self):
            input_ = ' * HEED * heedless * heeded * heeding * '
            output = (' * heeded * heeding * HEED * heedless * \n[sound:heeded.mp3]\n[sound:heeding.mp3]',
                      '\n\n[sound:HEED.mp3]\n[sound:heedless.mp3]')
            assert header_tab_mp3_content(input_) == output

        def test_error(self):
            input_ = 'test[sound:test.mp3]'
            output = (' * test * \n[sound:test.mp3]', '\n\n')
            assert header_tab_mp3_content(input_) == output
