# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 12:57:55 2023

@author: Vikki
"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> List:
       dummy = ListNode()
       curr = dummy
       
       carry = 0
       
       while l1 or l2 or carry:
           v1 = l1.val if l1  else None
           v2 = l2.val if l2 else None
           
           val, carry = divmod(v1+v2+carry)
           
           curr.next = ListNode(val)
           curr = curr.next 
           
           l1 = l1.next if l1 else None
           l2 = l2.next if l2 else None
           
           
       return dummy.next
    
    
l1 = list_to_listnode([2, 4, 3])
l2 = list_to_listnode([5, 6, 4])

print(Solution().addTwoNumbers(l1, l2))

