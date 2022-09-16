#!/usr/bin/env python
"""
Reducer aggregates word counts by class and emits frequencies
with plus one Laplace Smoothing.

INPUT:
    word \t class \t count
OUTPUT:   
    word \t class_0_count \t class_1_count
    
Instructions:
    Start by copying your unsmoothed reducer code
    (including the rest of the docstring info^^).
    Then make the necessary modifications so that you
    perform Laplace plus-k smoothing. See equation 13.7 
    in Manning, Raghavan and Shutze for details.
    
    Although we'll only look at results for K=1 (plus 1)
    smoothing its a good idea to set K as a variable
    at the top of your script so that its easy to change
    if you want to explore the effect of different 'K's.
    
    Please clearly mark the modifications you make to
    implement smoothing with a comment like:
            # LAPLACE MODIFICATION HERE 
"""
##################### YOUR CODE HERE ####################

import re
import sys

# initialize trackers
# I used ham as c=0 and spam as c=1 to make it short for variable
# these variables represent the total Doc or total Word respectively
hamDoc, spamDoc, hamWord, spamWord = 0,0,0,0
currWord = "*"
currWord_c0_count = 0
currWord_c1_count = 0
vocab_dict = dict()

# read from standard input
for line in sys.stdin:
    # parse input
    # word could be "*", ".", "chinese"
    word, isSpam, count = line.split()
    
    # interger conversion for isSpam, count
    isSpam = int(isSpam)
    count = int(count)
    
    # creating vocabulary dictionary with its associated c=0 and c=1 count
    # dictionary forma
    # {"beijing": [0,1]} 
    # the first value v[0] = 0 (total count of word 'beijing' occurrence in c=0 documents)
    # the second value v[1] = 1 (total count of word 'beijing' occurrence in c=1 documents)
    if word !="*" and word !=".":
        vocab_dict[word] = vocab_dict.get(word, [0, 0])
        for k,v in vocab_dict.items():
            if k == word:
                if isSpam == 1:
                    vocab_dict[k][1] += count
                else:
                    vocab_dict[k][0] += count 
        
    if currWord == word:
        if word == "*":
            # "*" for counting total number of ham or spam documents
            if isSpam == 1:
                spamDoc += count
            else:
                hamDoc += count
        elif word == ".":
            # "." for counting total words from all documents 
            if isSpam == 1:
                spamWord += count
            else:
                hamWord += count
        else: 
            # counting individual word occurrence 
            if isSpam == 1:
                currWord_c1_count += count
            else:
                currWord_c0_count += count
    else: 
        if currWord == "*":
            total_count = hamDoc + spamDoc
            print("{}\t{},{},{},{}".format("ClassPriors", hamDoc, spamDoc, hamDoc/float(total_count), spamDoc/float(total_count))) 
            if isSpam == 1:
                spamWord += count
            else:
                hamWord += count
        elif currWord == ".":
            if isSpam == 1:
                currWord_c1_count += count
            else:
                currWord_c0_count += count
        elif currWord !=".":
            # resetting the current count for next word statistics    
            currWord_c0_count = 0
            currWord_c1_count = 0
            if isSpam == 0:
                currWord_c0_count += count
            else:
                currWord_c1_count += count
        currWord = word
        
            
# emitting every word in vocabulary dictionar with laplace smoothing    
vocab_count = len(vocab_dict)
for k, v in vocab_dict.items():
    word = k
    word_c0_count = v[0]
    word_c1_count = v[1]
    cond_prob_c0 = (word_c0_count + 1)/float(hamWord + vocab_count)
    cond_prob_c1 = (word_c1_count + 1)/float(spamWord + vocab_count)
    print("{}\t{},{},{},{}".format(word, word_c0_count, word_c1_count, cond_prob_c0, cond_prob_c1))


##################### (END) CODE HERE ####################