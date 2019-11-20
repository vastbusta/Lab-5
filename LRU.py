# -*- coding: utf-8 -*-
"""
Author:Ruben Bustamante
Instructor: Diego Aguirre
TA:Gerarado Barraza
Course: CS 2302
Assigment: lab 5 part A
Date of last modification: 11/11/2019
Purpose of program: least reecntly used 
"""
import time
class Node:# node class
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

    def get(self, key):# get the key and returns the value
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1
   
    def remove(self, node):# remove the node 
        prev= node.prev
        next = node.next
        prev.next = next
        next.prev  = prev
        
    def insert(self, node):# insert at the tail
        prev = self.tail.prev
        prev.next = node
        self.tail.prev= node
        node.prev =prev
        node.next = self.tail
        
    def put(self, key, value):# add the new key and value in the cache
        
        if key in self.cache:# if key in cahce it removes it from the list
            self.remove(self.cache[key])
            
        node = Node(key, value)
        self.insert(node)
        self.cache[key]=node
        
        if len(self.cache)> self.capacity:# if current cap is greater rthen max cap
            node = self.head.next
            self.remove(node)# least used element whichis the at the head
            del self.cache[node.key]# delete the old node or pointer
            
    def size(self):# size 
        return len(self.cache)
    
    def max_capacity(self):# return max capacity lru can hold 
        return self.capacity
def main():  
    cache = LRU(1)
    start_time = time.time()
    cache.put(2,1)
    print('time:', (time.time()-start_time))
    cache.put(4,2)
    start_time2 = time.time()
    print("cache size",cache.size())
    print('time:', (time.time()-start_time2))
    start_time3 = time.time()
    print("max capcity",cache.max_capacity())
    print('time:', (time.time()-start_time3))
    start_time4 = time.time()
    print("get", cache.get(4))
    print("get", cache.get(4))
    print('time:', (time.time()-start_time4))
main()