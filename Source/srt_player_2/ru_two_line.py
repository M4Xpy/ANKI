import re
import threading
import time
import tkinter as tk

import keyboard
import mouse
import pygame
import pyperclip
from googletrans import Translator
from gtts import gTTS

text_update = 160 * " "
updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"
mp3_ru_audio = False
mp3_en_audio = False
play_track = False
keyboard_send_space = False
top_300 = """ l'm you'll won't forever gentlemen calypso barbossa pirates sumbhajee jones this'd world's whoa you'd haven't we'll they'll river's captain's it'll he'd doesn't everybody's aren't secret water's toxic toxins we'd wasn't they've admiral's where's o'clock he'll we're they're she's i've he's who's isn't we've that'll yahhhhhhh how'd were motorcycle karate demons why'd didn't l've she'll tattooed cigarettes worked there's that's bikers yellow dragons ain't i'll angels i'd what's golden children trying i'm you're oldest been you've haahh aah soft uhh speaking fantastics juice macho eh hah huh shh mmm-mmm mmm-hmm oops on any is niggers munro  mike jerry  warren glenn wendy jeez burt jim mister bible's captains whisky whiskey negros hmmm padre monsters wow goodnights pardon excuse devils bonn appetit nobodys tours address idiots everybody zeros stress queens russians concentrations finances errors transfers modules instructions democratics parks bottless thanks blocks codes madams metals experts experiments e-mails congress golds displays combinations cats liberals catholics components literatures informs englishs instruments surprises restaurants fruits motors incidents focus index mechanisms atmospheres milks religions greys first channels revolutions criminals signals plastics connects fundamentals ministers mornings parents lands situations collections cards suns officials july seconds documents hotdogs options concepts greens junes fully scene peace aprils nine september partners brothers hotels january balance sisters august octobers africans december november artists contacts telephones europeans februarys credits plus limits goodbyes videos regionals egypts contrasts farmers traffics coffees categorys museums internets italys crisis professors victorys dialects comments contents australians sexuals actuals visitors transports winters christmas progres conflicts studios professionals versions mrs context effective bests lady holidays express box totals kings clients sectors originals presidents summers daughters photocopy baby smiles lefts leaders everyones websites anyways seasons happy answers serious organisations securitys anyones personals details easys theorys financials officers directors everythings structures methods teachers records materials departments managements footballs facebooks papas publics remembers economics internationals students languages daddys teams types oppositions words centres understandings results functions news players eights doctors sevens germanys enters pms stations finals streets trees frances musics hards dates standards animals shops colours loves closes tests contracts armys pictures normals operations hundreds chances hospitals privates computers models informations businessmans centrals workers someones projects windows risks frees managers investors bingos dramatically absolutely crazys oohh rights month sergeants lieutenants terminators robots microprocessors fucks $ mamas users technologyss styless boss jesuss welcomess percentss godss helloss millionss familyss sorryss killss girlfriendss schoolgirlss schoolboyss boyfriends waters dids it's sirs can't lords don't facts writers okay tv pleases haves thats with this buts froms theys shes whichs says wills woulds theirs whats theres gets makes whos interests sees knows times 'm takes thems coulds hims years into thens  mores abouts yours moneys gives just these peoples two also wellss onlys whens mays looks likes such because finds wants betweens afters downs tells backs musts childs overs too three lifes greats wheres womans needs feels systems much ask groups numbers ideas anothers worlds areas shows courses companys problems againsts nevers mosts services hands partys americans highs somethings effects smalls places befores why aways houses differents countrys reallys weeks larges always starts helps nothings homes periods persons fours youngs rooms lines bigs names fives talks markets hours doors lets wars sorts reads mothers polices prices littles todays opens bads programmes minutes moments stops controls class six learns fathers plans products city games foods blues banks blacks towns historys whites an w e r t y u i o p a s d f g h j k l z x c v b n m """
top_2000 = """ made coming going had talking doing oceans does weren't wouldn't killed motorcycle looking maybe helicopters smoked smoking whoo tibetan tibet's taken babe yep let's pioneers juniors beautys residents unknowns appetites shoulds thoses yeah still becomes governments means leaves cases seems sames mights howevers shall whiles keeps points resultings holds nexts follows withouts turns within locals durings brings begins examplers socials states both runs longs sets importants eyes heads questions powers moves pays hears meets levels untils believes unbelievables alreadys impossibles studys lots lives jobs since happens leasts almosts earlys views himself togethers reports bits politicals laters laws produces reasons subjects anythings offers voices kinds actuallys educations falls enoughs buys mains conditions itself agrees sections roads tables soons halfs specials difficults grounds letters clears roles sells sometimes trades watchs agos strongs yesterdays stays waits usually differences wifes sales lights cares qualitys datas unions trues thirds shorts singles joins herselfs walls poors billions deals foreigns productions betters thousands sites hairs prepares ladies pieces fronts evenings royals fines designs pages enjoys individuals sizes fires series naturals wrongs nears futures introduces spaces attentions principless choices steps machines films nice moderns legals energys finally whoms sounds gardens floors myself forgets glass cups husbands christs capitals listen economy finishs duty fights trainers aspects industrials used university deads discussions outside procedures images oils militarys yourself seats miss populars respects fly heavy librarys pupils darks memory cultures bloods stones bars attacks fishs troubles traditionals importances interestings speakers mondays medicals tuesdays tomorrows colds sundays borns fridays highly wednesdays radios birds thursdays sexs fingers messages afternoons drinks races jackie jacks strategys kitchens saturdays sports status beautifuls marry readers rocks newspapers britishs plannings workings paris chinas colleges cashs normallys travels agents presences nons speeds proportions drivers commercials richs distances keys reactions westerns somebodys writers weekends farms connections phones alones flowers battles generations french scotlands somewheres baseballs bags freshs swiss engines tonights egyptians songs forests woods technicals indians dinners audiences paperworks masters religious crys potentials scottishs freedoms gentlemans selections factorys hopeles eggs naives romes decades brights searchs hollands fourth detailed mountains limiteds pensions congratulations greatests springs weathers bedrooms kids pleasures jumpers teachings combines temperatures totally digests dress sums publications iraqis seriously corrects potters phases switzerlandss skys brains perfects photographs ministry anymores readings fasts plates pools generate locations guns shuts journeys historicals japaneses lunch themes characteristics tooths bridges doubles soldiers swedens nurses prioritys wilds fixs slows cements alternatives chemicals jewishs wings basketballs uniteds winners mistakes representations washs trips gates overalls anybodys theatres enemy desks fashions cleans alrights fuels mines constants overtimes hates shoes writings noses origins wales tickets northerns thinks camels somewhats trends swedishs southerns planes openings welshs lessons """
top_5000 = """ rum heart fool hero done gonna told saying said thinking taking gone """
str_hub = " "
past_subtitles = "  "
delayed_text = ""
vol = 1
send_space = 0
press_space = 0

def play_without_ecxeptions(text, extra_exceptions="", exceptions="*♪¤"):
    return "".join(sign for sign in text if sign not in f"{exceptions}{extra_exceptions}")


def top_hub():
    # """
    # >>> top_hub()
    # """
    global str_hub
    file = "C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\tests\\exceptions\\top_hub.txt"
    with open(file, encoding='utf-8') as words:
        str_hub = words.read()


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


def volume(text):
    global vol
    if text and vol:
        keyboard.send("m")
        vol = 0
    elif not text and not vol:
        vol = 1
        keyboard.send("m")



def mouse_move():
    move = 1
    while True:
        move *= -1
        mouse.move(move, move, absolute=False, duration=0.1)

def online_player():
    global press_space, updated_text, mp3_ru_audio, mp3_en_audio, play_track, different, to_play_subtitle, translated, waite, keyboard_send_space, delayed_text, send_space

    waite = False

    prev_subtitle = ""
    keyboard.send('ctrl + a')
    time.sleep(0.3)
    keyboard.send('space')
    time.sleep(0.3)
    move = 1
    play_track = False
    start_time = 0
    pause = 0
    while True:
        move *= -1
        mouse.move(move, move, absolute=False, duration=0.0001)
        keyboard.send('ctrl + c')

        subtitle_lines = pyperclip.paste().splitlines()

        len_subtitle_lines = len(subtitle_lines)
        index = {
                0: 99,
                1: 99,
                2: 2,
                3: 2,
                4: 2,
                5: 2,
                6: 2,
                7: 7,
                8: 7,
                9: 7
                }[len_subtitle_lines if len_subtitle_lines < 10 else 0]
        subtitle_lines = " ".join(subtitle_lines[index:])




        if prev_subtitle != subtitle_lines:
            threading.Thread(
                    target=volume, args=(subtitle_lines,)
                    ).start()


            prev_subtitle = subtitle_lines
            subtitle = en_ru_corrector(subtitle_lines, "ru")



            if subtitle:
                if send_space:
                    keyboard.send("space")
                    press_space = 1
                    while send_space:
                        pass
                threading.Thread(
                                target=execute, args=(subtitle,)
                                ).start()






            else:
                time.sleep(0.1)
        else:
            time.sleep(0.1)
            # empty_text(play_track, start_time)


def execute(subtitle):
    global to_play_subtitle, different, updated_text, send_space, press_space
    send_space = 1
    ru_subtitle = subtitle
    en_subtitle = Translator().translate(subtitle.lower(), 'en', 'ru').text
    subtitle, to_play_subtitle, different = no_repit(en_subtitle)
    updated_text = f'{en_subtitle}\n{ru_subtitle}\n{text_update}\n{text_update}'
    prepare_audio(ru_subtitle, en_subtitle)
    if press_space:
        keyboard.send("space")
        press_space = 0
    send_space = 0



def time_delay(pause, start_time, subtitle):
    while time.time() < start_time:
        if not pause:
            pause = 1
            keyboard.send("space")
    if pause:
        time.sleep(0.2)
        keyboard.send("space")
    start_time = 1 + time.time() + len(subtitle) * len(subtitle) * 0.0007
    return start_time


def empty_text(play_track, start_time):
    global updated_text
    time.sleep(0.1)
    if updated_text != f"{text_update}\n{text_update}\n{text_update}\n{text_update}"  and time.time() > start_time + 2:
        updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"


def old_subtitles_delay(delayed_text):
    global updated_text
    while play_track:
        continue
    time.sleep(1)
    if updated_text == delayed_text:
        updated_text = f"{text_update}\n{text_update}\n{text_update}\n{text_update}"


def prepare_audio( ru_subtitle, en_subtitle):
    global waite, play_track, updated_text, delayed_text, updated_text

    ru_audio_file = gTTS(text=ru_subtitle.lower(), lang='ru')
    ru_audio_file.save("C:\\ANKIsentences\\temporary_ru_audio_file.mp3")
    ru_audio = "C:\\ANKIsentences\\temporary_ru_audio_file.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(ru_audio, "mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

    en_audio_file = gTTS(text=en_subtitle.lower(), lang='en')
    en_audio_file.save("C:\\ANKIsentences\\temporary_en_audio_file.mp3")
    en_audio = "C:\\ANKIsentences\\temporary_en_audio_file.mp3"

    while pygame.mixer.music.get_busy():
        continue



    pygame.mixer.music.load(en_audio, "mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    # pygame.mixer.quit()


def show_subtitle_text():
    font = 20
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry('+60+668')
    root.overrideredirect(True)  # Remove the window frame
    font = ('Arial', font)
    label = tk.Label(
            root, text=updated_text, font=font, fg='white', bg='black'
            )  # Set text color to white and background to black
    label.pack()

    def update_text():
        label.config(text=updated_text)
        root.after(10, update_text)

    update_text()
    root.mainloop()


def top_black_frame():
    top_message = "                                                             "
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.geometry('+0+0')
    root.overrideredirect(True)  # Remove the window frame
    font = ('Arial', 63)
    label = tk.Label(
            root, text=top_message, font=font, fg='white', bg='black'
            )  # Set text color to white and background to black
    label.pack()
    label.config(text=top_message)


def split_text_with_punctuation(text, punctuation='].,;:!?)'):
    # """
    # >>> split_text_with_punctuation('Do you like scary movies ? Mm-hmm.')
    # """
    parts = re.split(
        f"([{punctuation}])", text.replace(" mr.", " mr").replace("Mr.", "Mr").replace(" sir.", " sir").replace(
            "Sir.", "Sir"
            ).replace("*", "")
        )
    parts.append('')
    result = []
    compares = []
    severe = False
    for index in range(0, len(parts), 2):

        compare_count = 0
        compare = parts[index].strip(" -").lower()
        item_count = text.lower().count(compare)

        if compare and compare[0].isnumeric() and result and result[-1][-1] == ":" and result[-1][-2].isnumeric():
            result[-1] = result[-1] + parts[index] + parts[index + 1]
            continue

        if len(compare) == 1 and result and result[-1][-1] == "." == parts[index + 1]:
            result[-1] = result[-1] + parts[index] + "."
            severe = True
            continue
        elif severe:
            severe = False
            result[-1] = result[-1] + parts[index] + parts[index + 1]
            continue

        if item_count < 2:
            result.append(parts[index] + parts[index + 1])
        elif compare not in compares:
            for part in parts:
                if part.strip(" -").lower() == compare:
                    compare_count += 1
            if compare_count == item_count:
                result.append(parts[index] + parts[index + 1])
                compares.append(compare)

    return result


def no_repit(text, test=False):
    # """
    # >>> no_repit(' Mm-hmm.', test=True)
    # """
    global past_subtitles, str_hub
    punctuation = '].,;:!?)'
    start = split_text_with_punctuation(text, punctuation)
    # start = ['my abuela',]
    show_output = []
    play_output = []

    for part in start:

        uniq = 0
        count_of_hard_word = 0
        part_strip_lower = part.strip(punctuation + " '-").lower()
        part_strip_lower_split = part_strip_lower.split()
        len_part_strip_lower_split = len(part_strip_lower_split)
        if part_strip_lower not in past_subtitles:


            for word in part_strip_lower_split:

                word = "".join(
                        letter for letter in word.strip(' -') if letter.isalpha() or letter in "'-"
                        ).removesuffix("'s")

                if word:
                    if word not in top_300 or len_part_strip_lower_split > 8:
                        if word not in top_2000 or len_part_strip_lower_split > 6:
                            past_subtitles_count = past_subtitles.count(word)
                            if word not in top_5000 or not past_subtitles_count or len_part_strip_lower_split > 4:
                                add_hurd_word = past_subtitles_count < 3
                                count_of_hard_word += add_hurd_word
                                if add_hurd_word:
                                    if Translator().translate(word.lower(), 'ru', 'en').text.islower():
                                        play_output.append(part)
                                        uniq = 1
                                        break

        past_subtitles = past_subtitles + part_strip_lower
        if not uniq and count_of_hard_word / len_part_strip_lower_split > 0.5:
            play_output.append(part)
            uniq = 1


        if part.isupper():
            part = part.lower()
        if not uniq:
            part = part.upper().replace(" ", "  ")
        show_output.append(part)

    show = "".join(show_output)
    play = "".join(play_output)
    compare = show.lower() != play.lower() and play != ""
    if not test:
        stat_txt(f"('{text}', ' xxxxxx', '{show}', '{play}', {compare})")  # save all data to stat.txt for statictics

    print((text, " xxxxxx", show, play, compare))

    return show, play, compare


def check_and_add_to_hub(len_part, part, punctuation):
    global str_hub
    if len_part == 1:
        var = part.strip(punctuation + " -").lower()
        if var not in f"{top_2000} {top_300} {str_hub}":
            str_hub = f"{str_hub} {var}"
            file = "C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\tests\\exceptions\\top_hub.txt"
            with open(file, "a", encoding='utf-8') as vars:
                vars.write(f" {var}")


def stat_txt(text):
    file = "C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\tests\\exceptions\\stat.txt"
    with open(file, "a", encoding='utf-8') as vars:
        vars.write(f"\n{text}")





if __name__ == '__main__':
    top_hub()
    threading.Thread(target=online_player).start()
    time.sleep(1)
    # threading.Thread(target=top_black_frame).start()
    # threading.Thread(target=mouse_move).start()
    show_subtitle_text()

    pass
