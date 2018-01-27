#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 19:33:00 2018

@author: Kenneth Chen
"""

# Class MyTable

class MyTable:
    """Hash table using ord() for string and modulo operator for hash function."""
    
    def __init__(self, size):
        """Initialization of an empty hash table"""
        self._size = size
        self.keys = [None] * size
        self.values = [None] * size
        
    def _hash_function(self, k):
        """hash function for string"""
        sum = 0
        for word in k: sum += ord(word)         # hash code
        return (sum % self._size)               # compression by hash table size
    
    def _rehash(self, k):
        """linear probing"""
        return ((k+1) % self._size)
        
    def __setitem__(self, k, v):
        self._put(k, v)
    
    def __getitem__(self, k):
        return self._get(k)        
    
    def __delitem__(self, k):
        self._delete(k)
           
    def __len__(self):
        """Return number of items in the hashtable."""
        return len(self.keys)
    
    def _put(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        
        hashvalue = self._hash_function(k)
        
        if self.keys[hashvalue] == None:
            self.keys[hashvalue] = k
            self.values[hashvalue] = v
        else:
            if self.keys[hashvalue] == k:       # if found the match
                self.values[hashvalue] = v      # replace the value
            else:
                nextslot = self._rehash(hashvalue)
                stop = False
                while self.keys[nextslot] != None and self.keys[nextslot] != k and not stop:
                    if nextslot == hashvalue:
                        stop = True
                        raise KeyError('Key Error: MyTable is full.' + repr(k))
                    else:
                        nextslot = self._rehash(nextslot)
                    
                if self.keys[nextslot] == None:
                    self.keys[nextslot] = k
                    self.values[nextslot] = v
                else:
                    self.values[nextslot] = v        # replace

    def _get(self, k):
        startslot = self._hash_function(k)
        
        found = False
        stop = False
        position = startslot
        
        while self.keys[position] != None and not found and not stop:
            if self.keys[position] == k:
                found = True
                value = self.values[position]
            else:
                position = self._rehash(position)
                if position == startslot or self.keys[position] == None:
                    value = "Key not in table."
                    stop = True
        return value

    def _delete(self, k):
        
        startslot = self._hash_function(k)
        
        found = False
        stop = False
        position = startslot
        
        while self.keys[position] != None and not found and not stop:
            if self.keys[position] == k:
                self.keys[position] = 'deleted'
                self.values[position] = 'deleted'
                found = True
            else:
                position = self._rehash(position)
                if position == startslot:
                    stop = True
   
        
    
        
        