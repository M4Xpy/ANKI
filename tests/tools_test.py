from Source.bin.not_used_functions import open_google_translate
from Source.tools import *


class Test:
    # class Test:
    #     def test_(self):
    #         input_ = INPUT
    #         output = OUTPUT
    #         assert FUNCTION(input_) == output

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

    class TestEnRuTranslator:
        def test_en_ru_en_translator(self):
            input_ = 'apple'
            output = 'яблоко'
            assert en_ru_en_translator(input_) == output
            assert en_ru_en_translator(output) == input_

    class TestCtrl4OpenGoogleImage:
        def test_ctrl_4_open_google_image(self, monkeypatch):
            # Simulate clipboard text
            clipboard_text = ''
            monkeypatch.setattr('Source.tools.pyperclip.paste', lambda: clipboard_text)

            # Test case 1: When text parameter is empty
            ctrl_4_open_google_image('')
            # Add assertions here to verify the expected behavior

    class TestOpenGoogleImage:
        def test_open_google_image(self):
            assert open_google_image("TEST", 1) is None

    class TestOpenGoogleTranslate:
        def test_open_google_translate(self):
            assert open_google_translate('test') is None

    class TestCtrlCwRequestFor:
        def test_ctrl_c_w_request_for(self):
            assert True if git_hub else ctrl_c_w_request_for() is None

    class TestReplaceNonEnglishLetter:
        def test_replace_non_english_letter(self):
            input_ = 'test\n[sound:testy.mp3]'
            output = 'test\n'
            assert replace_non_english_letter(input_) == output

    class TestStarSeparatedWordsFrom:
        def test_star_separated_words_from(self):
            input_ = 'test\n[sound:test.mp3]'
            output = ' * test * '
            assert star_separated_words_from(input_) == output

    class TestRefersMp3s:
        def test_refers_mp3s(self):
            input_ = ' * SALIVA * salivary * salivation * SALINE * SALT * '
            output = ['[sound:SALIVA.mp3]', '[sound:salivary.mp3]', '[sound:salivation.mp3]', '[sound:SALINE.mp3]',
                      '[sound:SALT.mp3]']
            assert refers_mp3s(input_, -1) == output

    class TestNotNow:
        class TestHeaderTabMp3:
            def test_header_tab_mp3(self):
                pass

        class TestNewSingleWordCard:
            def test_new_single_word_card(self):
                pass

        class TestNakeFuncWrite:
            def test_make_func_write(self):
                pass

        class TestCtrlC3MultiTranslations:
            def test_ctrl_c_3_multi_translations(self):
                pass

        class TestPressKeys:
            def test_press_keys(self):
                assert press_keys(0.001) is None

        class TestCopyFuncPaste:
            def test_copy_func_paste(self):
                pass

        class TestCtrlCqFormatter:
            def test_ctrl_c_q_formatter(self):
                pass

        class TestCtrlAlistener:
            def test_ctrl_a_listener(self):
                pass

        class TestAlotOfNewSingleCard:
            def test_a_lot_of_new_single_card(self):
                pass

    class TestIfError:
        def test_if_error(self):
            assert if_error() == 'error'

    class TestTranslationsOfThe:
        def test_translations_of_the(self):
            input_ = 'ZAP'
            output = ['БЫСТРО', 'РАЗРЯД', 'РАЗРЯДКА', 'ЩЕЛКАТЬ']
            assert sorted(translations_of_the(input_)) == output

    class TestMultiTranslations:
        def test_multi_translations(self):
            in_put = 'ADJOIN_8068'
            output = 'ADJOIN_8068 * ПРИМЫКАТЬ * '
            assert output == multi_translations(in_put) == clone_multi_translations(in_put)

        class TestFilterLines:
            def test_0706(self):
                input_ = 'Nouns:\r\n\r\nChivalry (Russian translation: рыцарство)\r\nChivalrousness (rarely used) ' \
                         '(Russian translation: рыцарскость)\r\nVerbs:\r\n\r\nNone\r\nAdjectives:\r\n\r\nChivalrous ' \
                         '(Russian translation: рыцарский)\r\nAdverbs:\r\n\r\nChivalrously ' \
                         '(Russian translation: рыцарски)'
                output = '\nChivalry ( рыцарство)\nChivalrousness (rarely used) ( рыцарскость)\n\nChivalrous ' \
                         '( рыцарский)\n\nChivalrously ( рыцарски)'
                assert del_trash_lines_and_words(input_) == output

            def test_template(self):
                input_ = """"""
                output = """"""
                assert del_trash_lines_and_words(input_) == output

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
    "Act with integrity, guided by your principles." - "Действуйте с честностью, руководствуясь своими принципами." 
    (Deystvuyte s chestnost'yu, rukovodstvuyas' svoyimi printsipami)
    "The principal role in this play is challenging." - "Главная роль в этой пьесе вызывает сложности." 
    (Glavnaya rol' v etoy p'ese vyzyvaet slozhnosti)"""
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
    "Act with integrity, guided by your principles." - "Действуйте с честностью, руководствуясь своими принципами." 
    (Deystvuyte s chestnost'yu, rukovodstvuyas' svoyimi printsipami)
    "The principal role in this play is challenging." - "Главная роль в этой пьесе вызывает сложности." 
    (Glavnaya rol' v etoy p'ese vyzyvaet slozhnosti)"""
                assert del_trash_lines_and_words(input_) == output

            def test_6462(self):
                input_ = """Nouns:\r\n\r\nBeneath - под (preposition), низ (noun)\r
                Example: "The treasure lies beneath the surface." - Сокровище находится под поверхностью.\r
                Verbs:\r\n\r\nNone\r\nAdjectives:\r\n\r\n"""
                output = """\nBeneath - под (preposition), низ (noun)
                Example: "The treasure lies beneath the surface." - Сокровище находится под поверхностью.\n\n"""
                assert del_trash_lines_and_words(input_) == output

    class TestGetTemplate:
        def test_get_template(self):
            assert get_template('test', 'check') == 'This is a test'

    class TestRunProgram:
        def test_run_program(self):
            if not git_hub:
                assert run_program(True) is None

    # class Test:
    #     def test_(self):
    #         input_ = INPUT
    #         output = OUTPUT
    #         assert FUNCTION(input_) == output

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
