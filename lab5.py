# -*- coding: utf-8 -*-
"""
Author:Ruben Bustamante
Instructor: Diego Aguirre
TA:Gerarado Barraza
Course: CS 2302
Assigment: lab 5
Date of last modification: 11/11/2019
Purpose of program:using heaps and dict
"""
import time
class Node:
    def __init__(self,key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
        
class LRU:

    def __init__(self, capacity):
        
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next= self.tail
        self.tail.prev = self.head
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1
   
    def remove(self, node):
        prev= node.prev
        next = node.next
        prev.next = next
        next.prev  = prev
        
    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev= node
        node.prev =prev
        node.next = self.tail
        
    def put(self, key, value):
        
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.insert(node)
        self.cache[key]=node
        
        if len(self.cache)> self.capacity:
            node = self.head.next
            self.remove(node)
            del self.cache[node.key]
            
    def size(self):
        return len(self.cache)
    
    def max_capacity(self):
        return self.capacity
        
cache = LRU(1000)
start_time = time.time()
cache.put(5,1)
print('time:', (time.time()-start_time))
cache.put(5,2)
start_time2 = time.time()
print(cache.size())
print('time:', (time.time()-start_time2))
start_time3 = time.time()
print(cache.max_capacity())
print('time:', (time.time()-start_time3))
start_time4 = time.time()
print(cache.get(5))
print('time:', (time.time()-start_time4))