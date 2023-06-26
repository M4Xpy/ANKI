words = ['BEHALF', 'BLOODSHED', 'BOISTEROUS', 'BROKEN', 'CATEGORICAL', 'CHAOTIC',
         'COEFFICIENT', 'CONTACT', 'COOKER', 'COOKIE', 'CULTIVATE', 'CULTURAL', 'CULTURE', 'DEFUNCT', 'DEPRESS',
         'DEPRESSED', 'DEPRESSION', 'DESIRABLE', 'DETECTION', 'DETEST', 'DIFFERENCE', 'DIFFERENT', 'DIFFERENTIAL',
         'DIFFERENTIATE', 'DIFFERENTIATION', 'DIFFERENTLY', 'DIFFICULT', 'DIFFICULTY', 'DISCIPLE', 'DISTINGUISHED',
         'DISTRESS', 'DOGGED', 'DYSFUNCTION', 'ECSTATIC', 'EFFICACY', 'EFFICIENCY', 'EFFICIENT', 'EFFICIENTLY',
         'EMPOWER',
         'ENACT', 'ERADICATE', 'ESTABLISHED', 'EXCEPT', 'FACULTY', 'FAREWELL', 'FEUD', 'FEUDAL', 'FINISHED', 'FREAK',
         'FREAKISH', 'FUME', 'FUNCTION', 'FUNCTIONAL', 'HALVE', 'HARMONICA', 'HAWK', 'HERETIC', 'IMPROVE', 'IMPROVED',
         'IMPROVEMENT', 'IMPROVISE', 'IMPUNITY', 'INDIFFERENCE', 'INDIFFERENT', 'INMATE', 'KIOSK', 'LABORIOUS', 'LAN',
         'LAXATIVE', 'LOTION', 'LUGGAGE', 'LUMP', 'MALFUNCTION', 'MARE', 'MATE', 'MERIDIAN', 'MESS', 'MULTICULTURAL',
         'MYTH', 'NATURE', 'NOZZLE', 'OCCULT', 'ORGANIST', 'ORIGINATE', 'OUTSPOKEN', 'OVERWORK', 'PARALLEL',
         'PARALYSIS',
         'PARAPHRASE', 'PAWNBROKER', 'PERCH', 'PHRASEOLOGY', 'PIVOT', 'PLUCK', 'PORTER', 'PRAT', 'PSEUDONYM',
         'PUNISHMENT', 'PUNITIVE', 'PUNY', 'RADICAL', 'REGIMEN', 'RELEGATE', 'RELUCTANCE', 'RELUCTANT', 'RELUCTANTLY',
         'REPHRASE', 'RETRAIN', 'ROLE', 'ROM', 'SATISFACTORY', 'SHRAPNEL', 'SILO', 'SLAM', 'STATISTIC', 'STATISTICAL',
         'STATISTICS', 'STEAMER', 'STOCKBROKER', 'STRESS', 'SUBCULTURE', 'SWIFT', 'SWORD', 'SYNTACTIC', 'TACT',
         'TACTILE',
         'TALLY', 'TEAM-MATE', 'THEFT', 'THRILL', 'TRAINEE', 'TYPOGRAPHICAL', 'Typos', 'VENGEANCE', 'WATERSHED', 'WELL',
         'WELL-BEING', 'WELL-KNOWN', 'WHIM', 'WIMP', 'WINKLE', 'WORK-OUT', 'WORKMANSHIP', 'broke', 'corroboration',
         'enactment', 'feudalism', 'feuding', 'futures', 'hawkish', 'inefficient', 'redundantly', 'silos', 'sledge',
         'speeding', 'sward', 'totality']

text = """

Amidst the bustling city, the PUNKBROKER's kiosk stood, its walls adorned with TYPOGRAPHICAL art. The SILo, a relic of a bygone era, towered nearby, representing the INEFFICIENT systems of the past.

In this vibrant subculture, the SWIFT and BOISTEROUS expressed their creativity through IMPROVISATION. Their art was a symbol of rebellion against the ESTABLISHED norms, a statement of individuality.

The MESS of emotions, from DESPAIR to ECSTASY, filled the air. It was a place where STATISTICAL data merged with the THRILL of the unknown. The city's STATISTICS painted a picture of a DIVERSE society, where the lines between FUNCTIONAL and DYSFUNCTIONAL blurred.

On behalf of the oppressed, a vocal DISCIPLE emerged, an ORGANIST by day, a HERETIC challenging the status quo by night. They sought to RELEGATE the oppressive regime to history and usher in a new era of freedom.

In this realm of words, PHRASEOLOGY took center stage. The power to REPHRASE thoughts and ideas allowed for the diffusion of knowledge and the breaking of chains. The PEN was mightier than the SWORD, and the power of words could bring VENGEANCE or HEALING.

Through diligent TRAINING, a TEAM-MATE honed their skills. The WORKMANSHIP they displayed was evident in their precise movements and efficient execution. They found their own HALVE, striking a balance between dedication and personal well-being.

As the sun set, the city transformed into a playground of lights. The WINKLE in the crowd's eye revealed the WIMP's transformation into a FREAKISH character. The PSEUDONYM they assumed allowed them to roam freely, exploring the MULTICULTURAL flavors the city had to offer.

In the heart of the city, a STOCKBROKER worked tirelessly, their efficiency unmatched. They navigated the complexities of the market, riding the waves of change. Their relentless pursuit of success left no room for INDIFFERENCE.

In the distance, the STEAMER's whistle blew, a symbol of adventure and the unknown. It carried with it the promise of new experiences and the potential for growth. On board, travelers from different walks of life shared stories and insights, broadening their perspectives.

As the journey continued, the passengers found themselves drawn to the melancholic notes of a HARMONICA player. The instrument's TACTILE vibrations resonated deep within their souls, evoking emotions they thought long buried.

The city's streets pulsated with energy, a constant reminder of the DIVERSITY that surrounded them. From the bustling market to the quiet PERCH overlooking the city, each corner held its own story, waiting to be explored.

In this realm of endless possibilities, the power to EMPOWER oneself was within reach. The city's magnetic pull inspired those who dared to challenge the norm and carve their own path. They believed in the potential for IMPROVEMENT and embraced the unknown with open arms.

""".lower().split()
def roote_maker(words_list):
    prefixes = [
            'a', 'anti', 'auto', 'be', 'bi', 'co', 'com', 'con', 'de', 'dis', 'en', 'ex', 'il', 'im', 'in', 'inter',
            'ir', 'mis', 'non', 'over', 'post', 'pre', 'pro', 're', 'sub', 'super', 'trans', 'un'
            ]

    suffixes = [
            'able', 'e', 'ed', 'er', 'es', 'est', 'ful', 'hood', 'ible', 'ie', 'ing', 'ise', 'ism', 'ist', 'ity',
            'ize', 'ize', 'less', 'ly', 'ment', 'ness', 's', 'ship', 'sion', 'tion', 'ward', 'wards'
            ]
    non_prefix = set()
    for word in words_list:
        for _ in prefixes:
            non_prefix.add(word.lower().removeprefix(_))
    roots = set()
    for root in non_prefix:
        for _ in suffixes:
            roots.add(root.removesuffix(_))
    return roots

ss = roote_maker(words)
def corresponding_report(ss, text):
    set_words = set(words)
    set_words = set(map(str.lower, set_words))
    len_set_wards = len(set_words)
    set_words_remainder = set_words
    len_words_remainder = len(set_words_remainder)
    set_text = set(text)
    set_words_remainder.difference_update(set_text)
    len_words_remainder = len(set_words_remainder)
    len_text = len(text)
    len_set_text = len(set_text)
    len_used_wards = len_set_wards - len_words_remainder
    ratio = len_text / len_used_wards
    print(f"{len_used_wards           = }")
    print(f"{len_words_remainder      = }")
    print(f"{len_text                 = }")
    print(f"{len_set_text             = }")
    print(f"{ratio                    = :.3}")
    print(set_words)


if __name__ == '__main__':
    corresponding_report(words, text)
