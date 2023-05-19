# star_separated_words_from
# description for make_anki_card
# description for new_single_word_card

def star_separated_words_from(text: str) -> str:
    """ extract first word of each line, removing any digits or underscores from the word, and join them with asterisks
    >>> star_separated_words_from('one , two\\n\\nthree , four\\nfive , six')
    ' * one * three * five * '
    >>> star_separated_words_from(' * MENACING * [sound:Menacer.mp3]')
    '* MENACING *'
    """
    lines = [line for line in text.splitlines() if line and '.mp3' not in line]
    if len(lines) < 2:
        return ' '.join(word for word in text.split() if '[sound:' not in word)
    return f" * {' * '.join(l.split()[0].strip('_1234567890') for l in lines if l and '.mp3' not in l)} * "
