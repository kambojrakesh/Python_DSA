
import math    
class Solution:
    def isValidBST(self, root: BST) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.data
            print(val, lower, upper)
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True
    
    
    
    
if __name__=="__main__":
    ls = [10, 5, 1, 7, 40, 50]

    bst = build_tree(ls)
    
    s = Solution()
    print(s.isValidBST(bst))