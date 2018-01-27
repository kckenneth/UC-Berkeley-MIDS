#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 10:57:46 2018

@author: Kenneth Chen
"""

# Counting the numbers of equidistant nodes from the given two nodes

def equidistance(nodesList, matrix):
    first_node = int(nodesList[0])
    second_node = int(nodesList[2])
    
    count = 0
    for i in range(len(matrix)):
        if int(matrix[first_node][i]) + int(matrix[second_node][i]) == 2:
            count += 1
            print('This is 1+1')
            print(count)
    
    # This is a list of nodes that has no edges for n1 and n2.
    all_zeroes = []
    for i in range(len(matrix)):
        if int(matrix[first_node][i]) + int(matrix[second_node][i]) == 0:
            if first_node != i and second_node != i:
                all_zeroes.append(i)
    print("This is all_zeroes: ", all_zeroes)
    
    # This is a list of nodes that has an edge for n1 and n2.
    all_ones = []
    for i in range(len(adjmx)):
        if int(matrix[first_node][i]) + int(matrix[second_node][i]) == 2:
            if first_node != i and second_node != i:
                all_ones.append(i)
    print("This is all_ones: ", all_ones)
    
    # This is a list of nodes that has an edge for n1 but not n2.
    first_node_one = []
    for i in range(len(adjmx)):
        if int(matrix[first_node][i]) > int(matrix[second_node][i]):
            if first_node != i and second_node != i:
                first_node_one.append(i)
    
    # This is a list of nodes that has an edge for n2 but not n1.
    second_node_one = []
    for i in range(len(adjmx)):
        if int(matrix[second_node][i]) > int(matrix[first_node][i]):
            if first_node != i and second_node != i:
                second_node_one.append(i)
    
    # Finding secondary edges 
    for i in range(len(all_zeroes)):
        column = []
        for j in range(len(adjmx)):
            if int(matrix[all_zeroes[i]][j]) == 1:
                column.append(j)
                print(column)
                
        if any(map(lambda x: x in column, all_ones)) == True:
            count += 1
            print('This is comparing with all_ones')
            
        elif any(map(lambda x: x in column, first_node_one)) == True and any(map(lambda x: x in column, second_node_one)) == True:
            count += 1
            print('This is comparing with first and second node one')
        elif any(map(lambda x: x in column, first_node_one)) == False and any(map(lambda x: x in column, second_node_one)) == False:
            count += 1          # This is most likely tertiary edges. But instead of finding, I'd assume there will be edges because of most likely connection after 2nd edge. 
            print('Both are false.')
        print('This is a total count: ', count)
                           
    return count


# Load data
nodesList = open('input.txt', 'r').read().splitlines()

f = open('adj.txt', 'r').read().splitlines()
adjmx = [line.split() for line in f]


# Reading the file
output = []
for i in range(len(nodesList)):
    output.append(equidistance(nodesList[i], adjmx))
    
# Saving the output line by line
with open('output.txt', 'w') as f:
    for s in output:
        f.write(str(s) + '\n')
        
        
        

    
    
        
        
        
            
    