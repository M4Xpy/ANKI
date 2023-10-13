
text = "l'm gоnnа rummаgе in thе stоrаgе сlоsеt, sее if l саn find sоmеthing fоr Мurрh."



def en_ru_corrector(text):
    """
    >>> en_ru_corrector("l'm gоnnа rummаgе in thе stоrаgе сlоsеt")
    """
    russian_to_english = {
            'А': 'A', 'В': 'B', 'С': 'C', 'Е': 'E', 'Н': 'H',
            'К': 'K', 'М': 'M', 'О': 'O', 'Р': 'P', 'Т': 'T',
            'Х': 'X', 'а': 'a', 'с': 'c', 'е': 'e', 'о': 'o',
            'р': 'p', 'х': 'x', 'у': 'y', 'к': 'k'
            }

    for letter in text:
        if letter in russian_to_english:
            text = text.replace(letter, russian_to_english.get(letter))
    return text

