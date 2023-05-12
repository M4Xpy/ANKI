from unittest.mock import patch

import pytest

from Source.tools import detect_language, run_program, request_for


class TestRunProgram:

    @patch('keyboard.add_hotkey')
    @patch('keyboard.wait')
    def test_run_program(self, mock_wait, mock_add_hotkey):
        run_program()
        mock_add_hotkey.assert_called_once_with('w', request_for)
        mock_wait.assert_called_once()


class TestDetectLanguage:
    def test_detect_language_english(self):
        assert detect_language('Hello, world!') == 'en'

    def test_detect_language_russian(self):
        assert detect_language('Привет, мир!') == 'ru'

    def test_detect_language_unsupported(self):
        with pytest.raises(ValueError, match='Input text cannot be empty.'):
            detect_language('')
