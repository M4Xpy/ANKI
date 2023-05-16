from unittest.mock import patch, MagicMock

import pytest

from Source.tools import detect_language, run_program, get_request_text_from_paste


# class TestRunProgram:
#
#     @patch('keyboard.add_hotkey')
#     @patch('keyboard.wait')
#     def test_run_program(self, mock_wait: MagicMock, mock_add_hotkey: MagicMock) -> None:
#         run_program()
#         mock_add_hotkey.assert_called_once_with('w', request_for)
#         mock_wait.assert_called_once()



class TestDetectLanguage:
    def test_detect_language_english(self) -> None:
        assert detect_language('Hello, world!') == 'en'

    def test_detect_language_russian(self) -> None:
        assert detect_language('Привет, мир!') == 'ru'

    def test_detect_language_unsupported(self) -> None:
        with pytest.raises(ValueError, match='Input text cannot be empty.'):
            detect_language('')
