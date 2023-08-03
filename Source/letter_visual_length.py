letters = "C:\\Users\\Я\\Desktop\\letterslength.txt"


def letter_multiple_writer():
    global result, letters
    result = ""
    for letter in '01234567890,-\'».)/—>«("!:<?':
        result = f"{result}\n{letter * 50}"
        result = f"{result}\n{'|' * 200}"
    result = f"{result}\n{'ё' * 50}"
    result = f"{result}\n{'|' * 200}"
    result = f"{result}\n{'Ё' * 50}"
    result = f"{result}\n{'|' * 200}"

    with open(letters, "w", encoding='utf-8') as letters:
        letters.write(result)


def letter_length_meter():
    global result, letters, text
    result = {}
    with open(letters, encoding='utf-8') as letters:
        text = letters.readlines()
        for letter in text:
            if letter[1] != "|":
                sign = letter[1]
            else:
                score = letter.count("|")
                result[sign] = score

    print(result)




def visual_len(text, start=0, end=9999999999, score=0):
    """
    >>> visual_len("!" + " " * 149 + "!")
    2989
    # >>> visual_len(" Постарайтесь  не  разбудить  ")
    # 3062
    """
    leter_visual_length = {
            ' ': 59, '0': 117, '1': 117, '2': 117, '3': 117, '4': 117, '5': 117, '6': 117, '7': 117, '8': 117, '9': 117,
            ',': 58, '-': 50, "'": 50, '»': 117, '.': 59, ')': 67, '/': 51, '—': 175, '>': 117, '«': 117, '(': 67,
            '"': 92,
            '!': 58, ':': 58, '<': 117, '?': 109, 'a': 117, 'A': 134, 'b': 117, 'B': 134, 'c': 117, 'C': 134, 'd': 117,
            'D': 134, 'e': 117, 'E': 125,
            'f': 75, 'F': 117, 'g': 117, 'G': 150, 'h': 117, 'H': 150, 'i': 59, 'I': 67, 'j': 59, 'J': 117, 'k': 117,
            'K': 150, 'l': 59, 'L': 117, 'm': 175, 'M': 167, 'n': 117, 'N': 150, 'o': 117, 'O': 150, 'p': 117, 'P': 125,
            'q': 117, 'Q': 150, 'r': 84, 'R': 134, 's': 109, 'S': 125, 't': 75, 'T': 125, 'u': 117, 'U': 150, 'v': 109,
            'V': 134, 'w': 167, 'W': 176, 'x': 117, 'X': 134, 'y': 109, 'Y': 134, 'z': 100, 'Z': 125, 'а': 117,
            'А': 134,
            'б': 117, 'Б': 134, 'в': 109, 'В': 134, 'г': 92, 'Г': 117, 'д': 117, 'Д': 150, 'е': 117, 'Е': 125, 'ё': 117,
            'Ё': 125, 'ж': 159,
            'Ж': 192, 'з': 117, 'З': 117, 'и': 125, 'И': 150, 'й': 125, 'Й': 150, 'к': 109, 'К': 126, 'л': 125,
            'Л': 142,
            'м': 150, 'М': 167, 'н': 125, 'Н': 150, 'о': 117, 'О': 150, 'п': 117, 'П': 150, 'р': 117, 'Р': 125,
            'с': 117,
            'С': 133, 'т': 92, 'Т': 125, 'у': 109, 'У': 117, 'ф': 175, 'Ф': 159, 'х': 117, 'Х': 134, 'ц': 125, 'Ц': 150,
            'ч': 117, 'Ч': 142, 'ш': 175, 'Ш': 192, 'щ': 175, 'Щ': 200, 'ъ': 134, 'Ъ': 176, 'ы': 158, 'Ы': 192,
            'ь': 109,
            'Ь': 134, 'э': 117, 'Э': 142, 'ю': 167, 'Ю': 200, 'я': 108, 'Я': 133
            }
    if end == 9999999999:
        end = -~len(text)
    for letter in text[start:end]:
        score += leter_visual_length.get(letter, 59)
    return score


if __name__ == '__main__':
    pass
