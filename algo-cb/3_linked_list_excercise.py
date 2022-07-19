# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 18:41:54 2022

@author: Vikki
"""
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
class Linkedlist:
    def __init__(self,header = None):
        self.header = header
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

            
    def insert_values(self, ls):
        self.head = None
        for data in ls:
            self.insert_at_end(data)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
            
        itr = self.head
        while itr.next:
            itr = itr.next 

        itr.next = Node(data, None)
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count
    
    def remove_at(self, index):

        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return


        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1
 
    def add_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = itr.next
                itr.next = Node(data, None)
                itr = itr.next
                itr.next = node
                break
    
            itr = itr.next
            count+=1

    def insert_after_value(self, data_after, data_to_insert):

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = itr.next
                itr.next = Node(data_to_insert, None)
                itr = itr.next
                itr.next = node
                break
    
            itr = itr.next

    def find_index(self, data):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data:
                return count
            itr = itr.next
            count +=1
        
    def remove_by_value(self, data):
    # Remove first node that contains data   
        index = self.find_index(data)
        print(data, index)
        if index is not None:
            self.remove_at(index)
        else:
            print("No element is present.")

        
        
if __name__ == "__main__":
    ll = Linkedlist()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    print("-----------------------------")
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
        
