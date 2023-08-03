import random
import webbrowser

from Source.tools import now_test, step_by_step_print_executing_line_number_and_data


def clone_uniq_name(input_string: str,
              ) -> str:
    # """ Cut the input string if it is longer than 20 characters, and randomly doubled some character.
    # >>> uniq_name("This is a test string."), clone_uniq_name("This is a test string.")
    # ('This is a  testt strinngg.', 'this is a tesT striNG.')
    # """
    random.seed(now_test)
    output_string: str = ""                        # save result in separate variable
    for char in input_string:
        if random.random() < 0.05:            # 1 to 20 possibility of double sign
            output_string += char.upper()
        else:
            output_string += char.lower()     # 19 to 20 possibility of single sign
    return output_string                      # #-lines fully equal last comprehension line


@step_by_step_print_executing_line_number_and_data
def uniq_name(input_string: str,
              ) -> str:
    random.seed(now_test)
    return ''.join(
            char + char
            if random.random() < 0.05
            else char
            for char in input_string
            )


def open_google_translate(text: str) -> None:
    # """ open google translated with received request
    # >>> open_google_translate('you')
    # """
    webbrowser.open(f'https://translate.google.com/?sl=en&tl=ru&text={text}%0A&op=translate' )
open_google_translate('you')