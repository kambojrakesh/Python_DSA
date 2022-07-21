# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 18:41:54 2022

@author: Vikki
"""
class Node:
    def __init__(self, data, next = None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class Linkedlist:
    def __init__(self,header = None, tail = None):
        self.header = header
        self.tail = tail

            
    def insert_values(self, ls):
        self.header = None
        for data in ls:
            self.insert_at_begining(data)

    def insert_at_begining(self, data):
        
        

        
        
if __name__ == "__main__":
    ll = Linkedlist()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    
