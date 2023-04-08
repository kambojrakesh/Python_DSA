# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 15:36:50 2023

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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next 
            else:
                tail.next = list2
                list2 = list2.next 

            tail = tail.next
            
        if list1 :
            tail.next = list1
        elif list2 :
            tail.next = list2
                
        return dummy.next
    
    
    
        
        
list1 = [1,2,4]
list2 = [1,3,4]
#[1,1,2,3,4,4]

l1 = list_to_listnode(list1)
l2 = list_to_listnode(list2)

result = Solution().mergeTwoLists(l1, l2)

print_listnode(result)

















