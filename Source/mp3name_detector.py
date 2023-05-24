file_path = 'E:\\test_txt.txt'

def find_words_with_letter_combinations(file_path: str) -> set[str]:
    words = set()
    ommit = True
    with open(file_path, encoding="utf-8") as file:
        for part in file:
            for letter in part:
                if ommit:
                    if letter == '[':
                        ommit = False
                        word = '['
                else:
                    word = f'{word}{letter}'
                    if letter == ']':
                        ommit = True
                        words.add(word)




    return words


result = find_words_with_letter_combinations(file_path)
print(sorted(result))

