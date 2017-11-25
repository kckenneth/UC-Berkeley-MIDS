#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 17:07:16 2017

@author: Kenneth Chen
"""

# Winning strategy by recursion        
def strategy(n):
    if (n-1 < 1) and (n/2 < 1):
        return ('cold')
    elif (1 <= n-1 < 2) and (1 <= n/2 < 2):
        return ('hot')
    else:
        subtraction = strategy(n-1)
        division = strategy(n/2)
        if subtraction == 'cold' or division == 'cold':
            return ('hot')
        else:
            return ('cold')
    
# Load data
number = open('input.txt', 'r').read().splitlines()

# Reading the number file
output = []
for i in range(len(number)):
    n = int(number[i])
    output.append(strategy(n))

# Saving the output line by line
with open('output.txt', 'w') as f:
    for s in output:
        f.write(str(s) + '\n')
    
    
        

        
        
        
        
        
    
