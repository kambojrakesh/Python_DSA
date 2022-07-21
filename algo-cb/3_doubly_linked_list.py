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

    def insert_at_end(self, data):
        if self.header is None:
            self.header = Node(data, None, None)
            return
            
        itr = self.header
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None, itr)
        
    def insert_at_begining(self, data):
        if self.header is None:
            self.header = Node(data, None, None)
        else:
            node = Node(data, self.header, None)
            self.header.prev = node
            self.header = node
            

    def get_last_node(self):
        itr = self.header
        while itr.next:
            itr = itr.next
        
        return itr
    
    def print_forward(self):
         if self.header is None:
             print("Linked list is empty")
             return
    
         itr = self.header
         llstr = ''
         while itr:
             llstr += str(itr.data) + ' --> '
             itr = itr.next
         print(llstr)
        
    def print_backward(self):
         if self.header is None:
             print("Linked list is empty")
             return
    
         itr = self.get_last_node()
         llstr = ''
         while itr:
             llstr += str(itr.data) + ' --> '
             itr = itr.prev
         print(llstr)
         
         
    def insert_at_end(self, data):
        itr = self.get_last_node()
        itr.next = Node(data, None, itr.prev)
                 
    def insert_at(self, index, data):
        itr = self.header
        i = 0
        while itr:
            if i == index:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            i += 1 
            itr = itr.next
            
if __name__ == "__main__":
    ll = Linkedlist()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(3,"jackfruit")
    ll.print_forward()
    
