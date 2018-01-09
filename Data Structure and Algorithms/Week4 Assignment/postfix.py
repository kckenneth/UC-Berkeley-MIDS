#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 20:07:25 2017

@author: Kenneth Chen
"""

from pythonds.basic.stack import Stack

def postfix(CalList):
    operandStack = Stack()
    tokenList = CalList.split()

    for token in tokenList:
        if token.isdigit():
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

# Load data
CalList = open('input.txt', 'r').read().splitlines()

# Reading the file
output = []
for i in range(len(CalList)):
    output.append(postfix(CalList[i]))
    
# Saving the output line by line
with open('output.txt', 'w') as f:
    for s in output:
        f.write(str(s) + '\n')