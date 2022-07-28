from typing import List
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def insert_at_begining(self, data):
        node = ListNode(data, None)
        self.node = node   

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
                
            tail = tail.next
            
            if l1:
                tail.next = l1
            else:
                tail.next = l2
                
            return dummy.next
        
        
l = [[1,4,5],[1,3,4],[2,6]]

l1, l2 = [1,4, 2, 3], [9, 3, 2]
s = Solution()
s.mergeList(l1, l2)