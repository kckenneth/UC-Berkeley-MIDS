#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 17:48:19 2018

@author: lwinchen
"""

#Bucket sort

seq = [10, 2, 3, 15, 4, 8]

def buckSort(seq):
    
    bucket = ['a'] * (max(seq)+1)
    for i in seq:
        bucket[i] = str(i)

    bucket_str_clean = [c for c in bucket if c.isdigit()]
    return [int(c) for c in bucket_str_clean]
    