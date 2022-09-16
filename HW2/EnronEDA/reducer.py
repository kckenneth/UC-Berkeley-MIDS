#!/usr/bin/env python
"""
Reducer takes words with their class and partial counts and computes totals.
INPUT:
    word \t class \t partialCount 
OUTPUT:
    word \t class \t totalCount  
"""
import re
import sys

# initialize trackers
current_word = None
spam_count, ham_count = 0,0

# read from standard input
for line in sys.stdin:
    # parse input
    word, is_spam, count = line.split('\t')
    
############ YOUR CODE HERE #########

    # aggregating the matched word accordingly into spam and ham
    if word == current_word:
        if int(is_spam) == 1:
            spam_count += int(count)
        else:
            ham_count += int(count)
    else:
        if current_word:
            if spam_count > 0 and ham_count > 0:
                print("{}\t{}\t{}".format(current_word, 1, spam_count))
                print("{}\t{}\t{}".format(current_word, 0, ham_count))
            elif spam_count > 0:
                print("{}\t{}\t{}".format(current_word, 1, spam_count))
            else:
                print("{}\t{}\t{}".format(current_word, 0, ham_count))
            
        current_word = word                 # New word assignment in the reducer
        spam_count, ham_count = 0, 0
        if int(is_spam) == 1:
            spam_count += int(count)
        else:
            ham_count += int(count)

# to avoid printing zero count in both spam and ham emails

if spam_count > 0 and ham_count > 0:
    print("{}\t{}\t{}".format(current_word, 1, spam_count))
    print("{}\t{}\t{}".format(current_word, 0, ham_count))
elif spam_count > 0:
    print("{}\t{}\t{}".format(current_word, 1, spam_count))
else:
    print("{}\t{}\t{}".format(current_word, 0, ham_count))
        
# this is printing even if there's zero count for spam and ham emails.
#print("{}\t{}\t{}".format(current_word, 0, ham_count))
#print("{}\t{}\t{}".format(current_word, 1, spam_count))
    
            
############ (END) YOUR CODE #########