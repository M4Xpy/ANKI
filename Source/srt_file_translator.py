from googletrans import Translator

srt = "C:\\Users\\Я\\Desktop\\harry_potter_subtitles.txt"
new_srt = "C:\\Users\\Я\\Desktop\\harry_potter_modified_subtitles.txt"
with open(srt) as srt:
    text = srt.read()

subtitles = text.split('\n\n')

new_subtitles = ''
for number, subtitle in enumerate(subtitles):
    subtitle = subtitle.splitlines()
    on_text = ' '.join(subtitle[2:])

    translated = Translator().translate(on_text, 'ru', 'en').text
    print(translated)
    new_subtitles = f"\n\n{number}\n{subtitle[1].split(',')[0]}\n{on_text}\n{translated}"
    with open("C:\\Users\\Я\\Desktop\\harry_potter_modified_subtitles.txt", 'a+', encoding='utf-8') as new_srt:
        new_srt.write(new_subtitles)

if __name__ == '__main__':
    # print(new_subtitles)

    pass
