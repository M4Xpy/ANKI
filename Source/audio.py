# star_separated_words_from

import pyperclip as pyperclip


def filter_lines(text: str) -> str:
    """
    return text without lines with words from chek_s tuple, remove 'Translation:'
    >>> filter_lines("T\\nproverb\\nE\\nproverbs\\nS\\nPlease note\\nT\\nTranslation:").replace('\\n', '')
    'TEST'
    """
    # chek_s = ('proverb', 'proverbs', 'Please note')
    # filtered_lines = []
    # for line in text.splitlines():
    #     if not any(check in line for check in chek_s):
    #         filtered_lines.append(line)
    # result = '\n'.join(filtered_lines)
    # result = result.replace('Translation:', '')
    # return result
    return '\n'.join(line for line in text.splitlines() if not any(
        check in line for check in ('proverb', 'proverb', 'Please note'))).replace('Translation:', '')


def copy_func_paste(func):
    """ return to the clipboard the text received from the clipboard, processed by the provided function """
    # text = pyperclip.paste()
    # text = func(text)
    # pyperclip.copy(text)
    pyperclip.copy(func(pyperclip.paste()))


def ctrl_c_3_formatter():
    return copy_func_paste(filter_lines)