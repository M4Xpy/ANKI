remainder = f"C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\ANKI_CARDS\\" \
            f"undone_anki_txt_format\\remainder\\all731.txt"
part = f"C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\ANKI_CARDS\\" \
       f"undone_anki_txt_format\\remainder\\"
path = f"C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\additional_data\\ANKI_CARDS\\" \
              f"undone_anki_txt_format\\remainder\\chutGPT\\13chutGPT.txt"


def write_split_files():
    with open(remainder, encoding="utf-8") as file:
        file731 = file.read()
        beg = 0
        fin = 0
        for day in range(1, 31, 1):
            fin += 8599
            print(f"{beg} - {fin}")
            with open(f"{part}{day}.txt", "w", encoding="utf-8") as part_file:
                part_file.write(file731[beg:fin])
            beg = fin
write_split_files()


def ru_by_en_line_order(path,
                        splitter,
                        ):
    with open(path, encoding="utf-8") as file:
        lines = file.read()
        print(lines)

ru_by_en_line_order(path, '" - "')
