# -*- coding: utf-8 -*-

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)
            self.max_sum = max(self.max_sum, left_sum + right_sum + node.val)
            
            return max(left_sum, right_sum) + node.val
        
        dfs(root)
        return self.max_sum

    
    
root = [-10,9,20, None ,None,15,7]

root = TreeNode(-10)
root.left = TreeNode(9)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(1)
root.right.right.right.right = TreeNode(1)
mx = Solution().maxPathSum(root)
print(mx)