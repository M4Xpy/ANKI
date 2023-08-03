# import json
# #
# film = "hatico"
# #
# old_srt = f"C:\\Users\\Я\\Desktop\\films\\{film}\\{film}_2.txt"
# new_srt = f"C:\\Users\\Я\\Desktop\\films\\{film}\\{film}_en_ru_align.txt"
#
# all_words = f"C:\\Users\\Я\\Desktop\\films\\ru_words_total_dictionary.json"
# draft = "C:\\Users\\Я\\Desktop\\draft.txt"
#
#
#
# with open(all_words) as words_set_file:
#     all_words_set = json.load(words_set_file)
#     ddd = []
#     for word in all_words_set:
#         if len(word) < 3:
#             ddd.append(word)
#     print(ddd)
#
# x = ['и', 'не',  'в',  'но',  'на',  'ни',  'к', 'до',  'ко', ]
from Source.en_ru_srt_align import has_similar_word

print(has_similar_word('you', ["thee", "you"]))