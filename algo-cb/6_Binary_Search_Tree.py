# BST  </br>
# Insert and Search complexity - O(log n)
# At most two tree node </br>
# Left hand always smaller values  </br>
# Right hand side always higher values </br>
# No duplicates are allowed </br>
# Two traversal search - Breadth first search and depth first search </br>
# Depth first search - In order traversal , Pre order traversal, Post order traversal </br>

class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)

        if val > self.data:
            if self.right:
                self.right.search(val)

        return False

def build_tree(elements):
    root = BST(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__=='__main__':
    elements = [17, 87, 9, 3, 32, 14, 56, 7]

    root = build_tree(elements)
    print(root.in_order_traversal())
    print(root.search(19))