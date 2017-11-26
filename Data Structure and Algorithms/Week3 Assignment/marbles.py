#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 12:03:41 2017

@author: Kenneth Chen
"""

# A Marbles Game
board = input('Please enter your marble board as in "1, 3, 0, 2" without quotation in your choice of dimension. Your sequence can be random but must include 0. ')
board = list(board)
S = [int(s) for s in board if s.isdigit()]
print('{} {} {} {}'.format(*S))  
count = 0

from time import time
start_time = time()

def solve(S):
    global count
    if all(S[i+1] - S[i] == 1 for i in range(len(S)-1)):
        print('Total steps taken: ', count)  
        return        
    elif S[0] > S[1] and S[1] != 0:
        S[0], S[1] = S[1], S[0]             # Switch, S[1] must not be zero.
        count += 1 
        print('{} {} {} {}'.format(*S))
        return solve(S)
    else:
        S = S[1:] + S[:1]                   # Rotate
        count += 1
        print('{} {} {} {}'.format(*S))
        return solve(S)
    
solve(S)

end_time = time()
elapsed = end_time - start_time
print('This is the time taken to run the program: ', elapsed)

