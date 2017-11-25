#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 16:36:42 2017

@author: Kenneth Chen
"""

x = input('Please enter your phone number: ')
x_sum = sum(int(digit) for digit in str(x))
x = int(x)
y = x - x_sum
while True:
    if y >= 10:
        y_sum = sum(int(digit) for digit in str(y))
        y = y_sum
    else:
        break
    
print('A single digit from the phone number is: ', y)


# Another script with condition just after while
x = input('Please enter your phone number: ')
x_sum = sum(map(int, str(x)))
x = int(x)
y = x - x_sum
while y>= 10:
    y_sum = sum(int(digit) for digit in str(y))
    y = y_sum
    
print('A single digit from the phone number is: ', y)

