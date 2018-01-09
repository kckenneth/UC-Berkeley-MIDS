#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 10:46:34 2018

@author: Kenneth Chen
"""

def min_max(seq):
    
    mid = len(seq)//2
    seq1 = seq[:mid]
    seq2 = seq[mid:]
    
    def mm(seq):
        if seq[0] > seq[1]:
            print('comparison')
            high = seq[0]
            low = seq[1]
        else:
            high = seq[1]
            low = seq[0]
            
        for i in range(2, len(seq)):
            if high > seq[i]:
                print('comparison')
                if seq[i] < low:
                    print('comparison')
                    low = seq[i]
            else:
                high = seq[i]
                if seq[i] < low:
                    print('comparison')
                    low = seq[i]
            
        return high, low
    
    high1, low1 = mm(seq1)
    high2, low2 = mm(seq2)
    
    if high1 > high2:
        print('comparison')
        high = high1
    else:
        high = high2
        
    if low1 < low2:
        print('comparison')
        low = low1
    else:
        low = low2
        
    return high, low