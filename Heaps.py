# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:55:11 2019

@author: vasto
"""

import math
class MaxHeap(object):
    
    def __init__(self):
        
        self.tree = []
        
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
    def heap_sort(self):
        return 
heap = MaxHeap()
l = ['cat','bat', 'lab']
for i in l:
    heap.insert(i)
i =0
print(heap.tree)
    
