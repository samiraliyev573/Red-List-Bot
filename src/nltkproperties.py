
import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer

# Importing wordnet. Will be used for synonym recognition 
from nltk.corpus import wordnet

nltk.download('punkt')

stemmer = PorterStemmer()


# splitting a string into words, punctuation and numbers
def tokenize(sentence):
    return nltk.word_tokenize(sentence)


# generating the root form the words ex: universe - univers, university - univers
def stem(word):
    return stemmer.stem(word.lower())


# synonym recognition command
def synonym_recognition(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    
    return synonyms

def get_synonyms(word1):
    synonymList1 = []
    for data1 in word1:
        wordnetSynset1 = wn.synsets(data1)
        tempList1=[]
        for synset1 in wordnetSynset1:
            synLemmas = synset1.lemma_names()
            for i in xrange(len(synLemmas)):
                word = synLemmas[i].replace('_',' ')
                if word not in tempList1:
                    tempList1.append(word)
        synonymList1.append(tempList1)
    return synonymList1




# put all these words in a bag to be used later
def bag_of_words(tokenized_sentence, all_words):
    # stem every word in the given sentence
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for index, word in enumerate(all_words):
        if word in tokenized_sentence:
            bag[index] = 1.0

    return bag
