# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 13:16:47 2022

@author: Vikki
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 13:17:14 2022

@author: Vikki
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validBST(tree, low= -math.inf, high=math.inf):
            
            if not tree:
                return True
            
            if tree.val <= low or tree.val >= high:
                return False
            
            print(tree.val)
            
            return validBST(tree.left, low, tree.val) and validBST(tree.right,  tree.val, high)

            
        return validBST(root)
            
        
        
    
    
    
        