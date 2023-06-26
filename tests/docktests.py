from Source.tools import *


def doctests_for_star_separated_words_from():
    """
    >>> star_separated_words_from('SCUM \\n \\n \\n \\nSCAM \\n')
    ' * SCUM * SCAM * '
    >>> star_separated_words_from('test\\n[sound:test.mp3]')
    ' * test * '
    """


def doctests_for_replace_non_english_letter():
    """
    >>> replace_non_english_letter('one. * test.mp3  \\n / два _1234567890')
    'one \\n'
    >>> replace_non_english_letter('SCUM_10131 _подонок, накипь, пена, мразь, пенка, тина\\n* ОТБРОСЫ * МРАЗЬ * ПОДОНОК * НАКИПЕТЬ *\\n\\n\\nSCAM_9007 _мошенничество\\n * МОШЕННИЧЕСТВО * МОШЕННИЧАТЬ * АФЕРА *')
    'SCUM \\n \\n\\n\\nSCAM \\n'
    """
