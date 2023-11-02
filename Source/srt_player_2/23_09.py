def en_ru_corrector(text, lang="en"):
    # """
    # >>> en_ru_corrector("l'm gоnnа rummаgе in thе stоrаgе сlоsеt")
    # """
    russian_to_english = {
            'А': 'A', 'В': 'B', 'С': 'C', 'Е': 'E', 'Н': 'H',
            'К': 'K', 'М': 'M', 'О': 'O', 'Р': 'P', 'Т': 'T',
            'Х': 'X', 'а': 'a', 'с': 'c', 'е': 'e', 'о': 'o',
            'р': 'p', 'х': 'x', 'у': 'y', 'к': 'k'
            }  # russian : english

    for russian, english in russian_to_english.items():
        if lang == "en":
            text = text.replace(russian, english)
        elif lang == "ru":
            text = text.replace(english, russian)
    return text


print(en_ru_corrector("o", "ru") == "о")

# 37:46/ 1:33:12
# Cкopee пpибaвлю.
# Ho в следyющий paз пoстapaйcя.
