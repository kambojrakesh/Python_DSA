# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 13:17:52 2022

@author: Vikki
"""
class BST:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def add_child(self, data):
        if self.data == data:
            return

        if data < self.data:
            if self.left:
                return self.left.add_child(data)
            else:
                self.left = BST(data)

        if data > self.data:
            if self.right:
                return self.right.add_child(data)
            else:
                self.right = BST(data)

    def in_order_traverse(self):
        elements = []

        if self.left and self.data:
            elements += self.left.in_order_traverse()

        elements.append(self.data)

        if self.right and self.data:
            elements += self.right.in_order_traverse()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data and self.left:
                return self.left.search(val)
        if val > self.data and self.right:
                return self.right.search(val)

        return False

    def search_min(self):
        if self.left is None:
            return self.data

        if self.left:
            return self.left.search_min()

    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left and self.data:
            elements.append(self.left.data)
            self.left.in_order_traverse()

        if self.right and self.data:
            elements.append(self.right.data)
            self.right.in_order_traverse()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left and self.data:
            elements += self.left.in_order_traverse()

        if self.right and self.data:
            elements += self.right.in_order_traverse()

        elements.append(self.data)
        return elements

def build_tree(elements):
    root = BST(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

from collections import deque  
from typing import List  
class Solution:
    def levelOrder(self, root: BST) -> List[List[int]]:
        res = []
        q = deque()        
        q.append(root)
        
        
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.data)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if level:
                res.append(level)
        return res
        
    
if __name__=="__main__":
    ls = [3,9,20,null,null,15,7]

    bst = build_tree(ls)
    
    s = Solution()
    print(s.levelOrder(bst))
    