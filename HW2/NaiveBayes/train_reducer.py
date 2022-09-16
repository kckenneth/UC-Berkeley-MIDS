#!/usr/bin/env python
"""
Reducer aggregates word counts by class and emits frequencies.

INPUT:
    word \t true_class \t count
OUTPUT:
    word \t count_Ham \t count_Spam \t cp_Ham \t cp_Spam

    
Instructions:
    Again, you are free to design a solution however you see 
    fit as long as your final model meets our required format
    for the inference job we designed in Question 8. Please
    comment your code clearly and concisely.
    
    A few reminders: 
    1) Don't forget to emit Class Priors (with the right key).
    2) In python2: 3/4 = 0 and 3/float(4) = 0.75
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

# read from standard input
# remember, the incoming record formats are sorted already

for line in sys.stdin:
    # parse input
    # word could be "*", ".", "chinese"
    word, isSpam, count = line.split()
    
    # interger conversion for isSpam, count
    isSpam = int(isSpam)
    count = int(count)

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
            cond_prob_c0 = currWord_c0_count/float(hamWord)
            cond_prob_c1 = currWord_c1_count/float(spamWord)
            print("{}\t{},{},{},{}".format(currWord, currWord_c0_count, currWord_c1_count, cond_prob_c0, cond_prob_c1))
            currWord_c0_count = 0
            currWord_c1_count = 0
            if isSpam == 0:
                currWord_c0_count += count
            else:
                currWord_c1_count += count
        currWord = word
        
            
# printing the last word                
cond_prob_c0 = currWord_c0_count/float(hamWord)
cond_prob_c1 = currWord_c1_count/float(spamWord)
print("{}\t{},{},{},{}".format(currWord, currWord_c0_count, currWord_c1_count, cond_prob_c0, cond_prob_c1))

##################### (END) CODE HERE ####################