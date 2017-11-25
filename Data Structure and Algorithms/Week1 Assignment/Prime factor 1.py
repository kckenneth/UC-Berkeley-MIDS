#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 15:58:27 2017

@author: Kenneth Chen
"""

def primes(n):
    primeFac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primeFac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primeFac.append(n)
    
    primeSet = set(primeFac)
    primeNo = len(primeSet)
    return primeSet, primeNo


# This is 1st assignment
n = 1234567890
primeFac = []
d = 2
while d*d <= n:
    while (n % d) == 0:
        primeFac.append(d)  
        n //= d
    d += 1
if n > 1:
    primeFac.append(n)
    
primeSet = set(primeFac)
print('Number of unique prime factors in 1234567890 is', len(primeSet))
