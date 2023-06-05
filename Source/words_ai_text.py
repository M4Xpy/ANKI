from Source.mp3name_detector import find_in_the

file_path = 'C:\\Users\\Я\\Desktop\\C_M_W    000.txt'



words = {'DISPARATE', 'hooter', 'emitted', 'REMIT', 'CONDEMN', 'GARNISH', 'DISPARITY', 'garnet', 'CRUCIBLE', 'rundown',
         'SCUM', 'TANGENT', 'CONSTRAIN', 'REMISS', 'POTASSIUM', 'LULL', 'TANGO', 'TERMINABLE', 'FLUFF', 'NREMITTING',
         'PEDDLE', 'BLOAT', 'aptly', 'APT', 'INHABITED', 'runt', 'agility', 'FETE', 'SNUB', 'OFFEND', 'DIN', 'SPEW',
         'TANG', 'HAVOC', 'HOOT', 'AGILE', 'SPAR', 'COAX', 'MOT', 'LAX', 'GARNER', 'EMIT', 'FOIL', 'SLUMBER', 'emitter',
         'TANGERINE', 'DISPARAGE', 'remitter', 'TWIT', 'hooting', 'COVET', 'PARABLE', 'GRUB', 'EXCEED', 'DIGRESS',
         'COWER', 'isparaging', 'RUSTLE', 'REMISSION', 'SLUM', 'SLUMP', 'remitted', 'QUILT', 'APTITUDE', 'remittance',
         'SCAM', 'hooters', 'FLEMISH', 'SURCHARGE', 'FLUFFY', 'PEW', 'emitting', 'ALKALINE', 'TANGIBLE', 'GRUBBY'}

text = """

A disparate hooter emitted remit. Condemn garnish, disparity, garnet, crucible, rundown scum. Tangent constrain remiss potassium lull tango terminable fluff nonremittin' peddle bloat. Aptly apt inhabited runt agility fete snub offend din spew tang havoc hoot. Agile spar coax mot lax garner emit foil slumber emitter tangerine disparage remitter twit hootin' covet parable grub exceed digress cower disparagin' rustle remission slum slump remitted quilt aptitude remittance scam hooters Flemish surcharge fluffy pew emitting alkaline tangible grubby.

"""
result = []
for word in words:
    if word.lower() in text or word.title() in text or word.upper() in text:
        pass
    else:
        result.append(word)
print(result)

if __name__ == '__main__':
    print(find_in_the(file_path, content='mp3_words'))