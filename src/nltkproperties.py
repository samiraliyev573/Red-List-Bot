
import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer

# Importing wordnet. Will be used for synonym recognition 
from nltk.corpus import wordnet

from nltk.tokenize import PunktSentenceTokenizer
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

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
    antonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    
    return synonyms

#POS tag list:

#CC coordinating conjunction
#CD cardinal digit
#DT determiner
#EX existential there (like: "there is" ... think of it like "there exists")
#FW foreign word
#IN preposition/subordinating conjunction
#JJ adjective 'big'
#JJR adjective, comparative 'bigger'
#JJS adjective, superlative 'biggest'
#LS list marker 1)
#MD modal could, will
#NN noun, singular 'desk'
#NNS noun plural 'desks'
#NNP proper noun, singular 'Harrison'
#NNPS proper noun, plural 'Americans'
#PDT predeterminer 'all the kids'
#POS possessive ending parent's
#PRP personal pronoun I, he, she
#PRP$ possessive pronoun my, his, hers
#RB adverb very, silently,
#RBR adverb, comparative better
#RBS adverb, superlative best
#RP particle give up
#TO to go 'to' the store.
#UH interjection errrrrrrrm
#VB verb, base form take
#VBD verb, past tense took
#VBG verb, gerund/present participle taking
#VBN verb, past participle taken
#VBP verb, sing. present, non-3d take
#VBZ verb, 3rd person sing. present takes
#WDT wh-determiner which
#WP wh-pronoun who, what
#WP$ possessive wh-pronoun whose
#WRB wh-abverb where, when


def show_part_of_speech(sentence):
    sample_sentence = sentence
    sentence_tokenizer = PunktSentenceTokenizer(sample_sentence)
    tokenized_sentence = sentence_tokenizer.tokenize(sample_sentence)
    
    try:
        for i in tokenized_sentence:
            words = tokenize(i)
            tagged = nltk.pos_tag(words)
            return tagged
    except Exception as e:
        print(str(e))






# put all these words in a bag to be used later
def bag_of_words(tokenized_sentence, all_words):
    # stem every word in the given sentence
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for index, word in enumerate(all_words):
        if word in tokenized_sentence:
            bag[index] = 1.0

    return bag
