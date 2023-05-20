import pytest

from Source.tools import detect_language, star_separated_words_from


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