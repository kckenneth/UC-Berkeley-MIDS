#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:04:36 2017

@author: Kenneth Chen
"""

# Words Scramble by recursion
def scramble(W):
    S = list(W)                     # converting str to list
    
    import math
        
    def powerOf2(S):                # check if the length of the words list is power of 2
        logP = math.log2(len(S))
        if (logP).is_integer():     # check if the float from log function is a whole number
            return S
        else:
            S.append('.')           # appending '.' if the length is shorter than the power of 2
            return powerOf2(S)
     
    result = []
    def split(S, start, stop):
        if start < stop-2:          # if the sequence is longer than 2
            mid = (start+stop)//2   # defining the midpoint
            
            S1 = S[start:mid]       # creating the first sequence based on the midpoint
            S2 = S[mid:stop]        # creeting the second sequence based on the midpoint
        
            split(S1, start, mid)   # split the first sequence again
            split(S2, start, mid)   # split the second sequence again
            
            if len(S1) == 2:        # the ultimate sequence length after multiple rounds of splitting
                l1 = [val for pair in zip(S1, S2) for val in pair]  # merge S1 and S2 by element wise
                result.append(l1)   # each sequence will have 4 elements in result list
        return result
    
    def concat(result):             # concatenating every sequence in result by 
        if len(result) >= 2:        # their respective index
            z = int(len(result)-1)
            final = []
            for i in range(0, z, 2):
                final.append([val for pair in zip(result[i], result[i+1]) for val in pair])
            concat(final)
        else:
            scramble = []           # space for the final scrambled words
            while result:
                scramble.extend(result.pop(0))  # joining all elements in result into scramble space 
                global joinedSW
                joinedSW = ''.join(scramble)    # removing all quotes 
        return joinedSW
    
    powerOf2(S)
    split(S, 0, len(S))
    concat(result)
    
    return joinedSW

# Load data
wordsList = open('input.txt', 'r').read().splitlines()

# Reading the words file
output = []
for i in range(len(wordsList)):
    output.append(scramble(wordsList[i]))

# Saving the output line by line
with open('output.txt', 'w') as f:
    for s in output:
        f.write(str(s) + '\n')
        
    
    

