srt = "C:\\Users\\Я\\Desktop\\harry_potter_subtitles.txt"
srt_result = "C:\\Users\\Я\\Desktop\\harry_potter_subtitles_2.txt"
my_srt = "C:\\Users\\Я\\Desktop\\harry_potter_modified_subtitles.txt"

with open(srt, encoding='utf-8') as srt:
    srt_text = srt.read()

with open(my_srt, encoding='utf-8') as my_srt:
    my_srt_text = my_srt.read()

subtitles = srt_text.split("\n\n")
my_subtitles = my_srt_text.split("\n\n")

result = []
for index, subtitle in enumerate(subtitles):
    subtitle = subtitle.replace(' --> ', '\n').splitlines()
    subtitle = [subtitle[0], subtitle[1].replace(',', '.'), subtitle[2].replace(',', '.'),
                f" {' '.join(subtitle[3:])}".replace(' ', '  ').replace('?', ' ?').replace('!', ' !').replace(
                    '.', ' .'
                    ).replace(',', ' ,')]

    for my_subtitle in my_subtitles:
        if subtitle[1][:8] in my_subtitle:
            my_subtitle = my_subtitle.splitlines()
            subtitle.append(
                f' {my_subtitle[-1]}'.replace(' ', '  ').replace('?', ' ?').replace('!', ' !').replace(
                    '.', ' .'
                    ).replace(',', ' ,')
                )
    result.append('\n'.join(subtitle))

with open(srt_result, 'w', encoding='utf-8') as srt_result:
    srt_result.write('\n\n'.join(result))
