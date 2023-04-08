# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 16:28:41 2023

@author: Vikki
"""


from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self):
       self.val = None
       self.next = None 
       
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
  

def list_to_listnode(lst: List[int]) -> Optional[ListNode]:
    if not lst:
        return None
    
    head = ListNode(lst[0])
    current_node = head
    
    for val in lst[1:]:
        new_node = ListNode(val)
        current_node.next = new_node
        current_node = new_node
    
    return head

def print_listnode(ln: Optional[ListNode]) -> None:
    while ln:
        print(ln.val, end=' ')
        ln = ln.next
    print()
    
    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Calculate the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        if n >= length:
            return head.next
        
        current = head
        for i in range(length - n - 1):
            current = current.next
            
        current.next = current.next.next
        
        return head
    
head = [1,2]
n = 2
ls = list_to_listnode(head)

print_listnode(Solution().removeNthNode(ls))

















