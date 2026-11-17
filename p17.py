# program to demonstrate n-gram
from nltk import ngrams
sentence = "Artificial Intelligence is the branch of computer science that aims to create intelligent machines."
n=1
unigram = ngrams(sentence.split(), n)
for gram in unigram:
    print(gram)

from nltk import ngrams
sentence = "Artificial Intelligence is the branch of computer science that aims to create intelligent machines."
n=2
bigrams = ngrams(sentence.split(), n)
for gram in bigrams:
    print(gram)
