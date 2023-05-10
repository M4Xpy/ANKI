import pytest

from Source.tools import detect_language


class TestDetectLanguage:
    def test_detect_language_english(self):
        assert detect_language('Hello, world!') == 'en'

    def test_detect_language_russian(self):
        assert detect_language('Привет, мир!') == 'ru'

    def test_detect_language_unsupported(self):
        with pytest.raises(ValueError, match='Input text cannot be empty.'):
            detect_language('')
