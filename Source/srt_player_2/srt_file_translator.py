from googletrans import Translator


def translate_subtitles():
    global text
    srt = "C:\\Users\\Я\\Desktop\\films\\hercules\\herculesSept21.txt"
    new_srt = "C:\\Users\\Я\\Desktop\\films\\hercules\\hercules.txt"
    with open(srt) as srt:
        text = srt.read()
    subtitles = text.split('\n\n')
    for number, subtitle in enumerate(subtitles):
        translated = Translator().translate(subtitle.splitlines()[2], 'ru', 'en').text
        print(translated)
        new_subtitles = f"{subtitle}\n{translated}\n{translated}\n\n"
        with open("C:\\Users\\Я\\Desktop\\films\\hercules\\hercules.txt", 'a+', encoding='utf-8') as new_srt:
            new_srt.write(new_subtitles)




if __name__ == '__main__':
    translate_subtitles()

    pass
