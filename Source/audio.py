def new_card_from():
    keyboard.send("tab")
    time.sleep(0.1)
    keyboard.send("tab")
    time.sleep(0.1)
    keyboard.send("enter")
    time.sleep(0.1)
    in_text = pyperclip.paste()
    time.sleep(0.1)
    split_text = in_text.split()
    header = ""
    for letter in split_text[0]:
        if letter != "_":
            header += f"{letter}"
        elif letter == "_":
            break
    time.sleep(0.1)
    header = split_text[0].split()[0]
    print(header)
    to_translate = header.strip('_1234567890')
    keyboard.write(f" * {header} *[sound:{to_translate}.mp3]")
    time.sleep(0.1)
    keyboard.send("tab")

    header = to_translate.lower()
    total = []
    trans = f"{header}"
    translated = en_ru_en_translator(input_text=trans, lang='en')
    total.append(translated.upper())
    # print(translated.text.upper())
    trans = f"the {header} "
    translated = en_ru_en_translator(input_text=trans, lang='en')
    if translated.upper() not in total:
        total.append(translated.upper())
    # print(translated.upper())
    trans = f"to {header} "
    translated = en_ru_en_translator(input_text=trans, lang='en')
    adj = translated.upper()
    too = adj
    if too not in total:
        total.append(too)
    print(adj)
    trans = f"too {header} "
    translated = en_ru_en_translator(input_text=trans, lang='en')
    adj = translated.upper()
    adjective = adj.split()
    too = adjective[1:]
    too = " ".join([str(a) for a in too])
    if too not in total:
        total.append(too)
    print(adj, too)
    keyboard.write("\n" + " * ".join(str(s) for s in total) + "\n\n")
    time.sleep(0.1)
    keyboard.send("ctrl + v")