import nltk

def get_word_frequency(word):
    nltk.download('omw-1.4')
    nltk.download('brown')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('punkt')

    from nltk.corpus import wordnet as wn
    from nltk.corpus import brown

    # Get synsets (senses) for the word
    synsets = wn.synsets(word)

    # Extract the senses from synsets
    senses = [synset.definition() for synset in synsets]

    # Count the occurrences of the word in the brown corpus
    count = brown.words().count(word)


    return [count, senses]

# word = "kata".lower()
# senses = get_word_frequency(word)
# print(f"The word '{word}{senses[0]}' has the following senses:")
# for i, sense in enumerate(senses[1], 1):
#     print(f"Sense {i}: {sense}")


import nltk
from nltk.corpus import brown
from nltk.corpus import wordnet as wn

def get_word_sense_frequency(word, sense):
    count = 0
    for sentence in brown.sents():
        for token in sentence:
            if token == word and wn.synsets(token)[0].name() == sense:
                count += 1
    return count

word = "cat"
sense = wn.synsets(word)[0].name()
frequency = get_word_sense_frequency(word, sense)
print(f"The frequency of sense '{sense}' for the word '{word}' in the Brown corpus is {frequency}.")
