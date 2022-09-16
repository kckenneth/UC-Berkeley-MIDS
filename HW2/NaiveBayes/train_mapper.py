#!/usr/bin/env python
"""
Mapper reads in text documents and emits word counts by class.

INPUT:
    ID \t true_class \t subject \t body \n
OUTPUT:
    word \t true_class \t count

    
Instructions:
    You know what this script should do, go for it!
    (As a favor to the graders, please comment your code clearly!)
    
    A few reminders:
    1) To make sure your results match ours please be sure
       to use the same tokenizing that we have provided in
       all the other jobs:
         words = re.findall(r'[a-z]+', text-to-tokenize.lower())
         
    2) Don't forget to handle the various "totals" that you need
       for your conditional probabilities and class priors.
"""
##################### YOUR CODE HERE ####################

import re
import sys

# read from standard input
for line in sys.stdin:
    # parse input and tokenize
    emailID, _class, subject, body = line.lower().split('\t')
    words = re.findall(r'[a-z]+', subject + ' ' + body) 
    
    # for the purpose of counting ham and spam total emails respectively to calculate 'prior probability'
    # "*" is used as "order inversion" which I detailed in this exercise Q.2c (short response)
    # this print is equal to the total number of examples 
    print("{}\t{}\t{}".format("*", _class, 1))    
    
    # mapping individual words 
    for word in words:
        print("{}\t{}\t{}".format(".", _class, 1))         # counting total words 
        print("{}\t{}\t{}".format(word, _class, 1))        # printing individual words
       
"""
For my reference:

You can imagine every "*" emit will be followed by an equal number of "." and "word" in the reducer component. 
In order to calculate the relative frequency and prior probability, the reducer must receive the "*" and "." first so that
it can calculate the relative frequency of each word in their labels. How do we do that? since every "*" emit will be followed by 
"." and "word". 

The trick is to sort the mapper output before we feed them into the reducer. That's why we'd sort it by UNIX. 
We can also give any of the character for "*". But if we give "sum", it will be problematic because by the time we sort by UNIX, 
the "sum" will be somewhere between all the words "chinese", "beijing", "sum", "tokyo" and it defeats the purpose of our desire to 
emitting the total documents information to the reducer in the first place. 

"""

##################### (END) YOUR CODE #####################