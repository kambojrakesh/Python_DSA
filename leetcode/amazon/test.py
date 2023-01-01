# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:13:59 2022

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


if __name__=="__main__":
    elements = [17, 14, 7, 11,8, 20, 15, 23, 27, 28]
    root = build_tree(elements)
    elements = root.in_order_traverse()
    print("Inorder : ", elements)
    print(root.search(7))

    print(root.search_min())

    elements = root.pre_order_traversal()
    print("Preorder : ",elements)

    elements = root.post_order_traversal()
    print("Postorder : ",elements)