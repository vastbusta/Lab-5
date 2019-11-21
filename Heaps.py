# -*- coding: utf-8 -*-
"""
Author:Ruben Bustamante
Instructor: Diego Aguirre
TA:Gerarado Barraza
Course: CS 2302
Assigment: lab 5 part B
Date of last modification: 11/20/2019
Purpose of program:uses heaps to find the most occurneces of list of strings
"""
import time 
import math
class node:
    def __init__(self, word, count):
        self.word = word
        self.count = count
class MaxHeap(object):
    
    def __init__(self):
        
        self.tree = []
        self.curr_size =0
        
    def is_empty(self):
        
        return len(self.tree) ==0
    
    def parent(self, i):
        
        if i ==0:
            return -math.inf
        
        return self.tree[(i-1)//2]
    
    def left_child(self,i):
        c = 2*i+1
        if c >= len(self.tree):
            return -math.inf
        return self.tree[c]
        
    def right_child(self, i):
        
        c = 2*i+2
        
        if c >=len(self.tree):
            return -math.inf
        return self.tree[c]
    def size(self):
        self.curr_size =len(self.tree)
        return self.curr_size
    
    def insert(self, item):
        
        self.tree.append(item)
        self._percolate_up(len(self.tree)-1)
        
    def _percolate_up(self, i):
        if i ==0:
            return
        parent_index =(i-1)//2
        
        if self.tree[parent_index] < self.tree[i]:
            self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
            self._percolate_up(parent_index)
    def extract_max(self):
        if len(self.tree)<1:
            return None
        if len(self.tree) ==1:
            return self.tree.pop()
        self._percolate_up(0)
        
        return self.tree
    def _percolate_down(self, i):
        if self.tree[i] >= max(self.left_child(i), self.right_child(i)):
            return
        max_child_index = 2*i +1 if self.left_child(i)> self.right_child(i) else  2*i+2
        self.tree[i], self.tree[max_child_index] = self.tree[max_child_index], self.tree[i]
        self._percolate_down(max_child_index)
        
def heap_sort(alist):
    
    h = MaxHeap()
    
    for word in alist:
        h.insert(word)
        
    i = len(alist) - 1
    
    while not h.is_empty():
        
        alist[i] = h.extract_max()
        i -= 1
        
        return alist
    
def count_dict(list_words, k):
        
        my_dict ={}
        heap = MaxHeap()
        freq =[]
        freq2=[]
        for i in range(len(list_words)):# uset dict to count each string and number of times 
            if list_words[i] in my_dict:
                my_dict[list_words[i]]+=1
            else:
                my_dict[list_words[i]]=1
            
        k = max(my_dict.values())# update ky to the max number of occurences

        for key in my_dict.keys():# store keys and values in tree
            heap.insert((key, my_dict[key]))
        
        for key,value in heap.tree:# campare k to the value in the tree
            if k == value:
                freq.append((key,value))
                
            if key not in freq and k !=value:# adds the rest of the list
                freq2.append((key, value))
        freq.sort()
        freq2.sort()     
        return freq, freq2
        
        
def main():
    words = ['cat','lab', 'lab', 'cat', 'bat','dog','bob','bob','i']
    lower_case =[]
    for i in words:# converts all string to lower case 
        lower_case.append(i.lower())
    print(count_dict(lower_case,0))
main()