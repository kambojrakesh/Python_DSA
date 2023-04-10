from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root):
    # Create a queue for BFS and add the root to it
    #queue = [root]
    dqueue = deque([root])
    # Loop until the queue is empty
    while dqueue:
        # Dequeue a node from the queue
        #node = queue.pop(0)
        node = dqueue.popleft()

        # Visit the node
        print(node.val)

        # Enqueue the left and right children if they exist
        if node.left:
            dqueue.append(node.left)
        if node.right:
            dqueue.append(node.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


bfs(root)
