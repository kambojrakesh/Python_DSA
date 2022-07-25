# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 16:32:05 2022

@author: Vikki
"""
token = {")":"(", "]":"[", "}":"{"}

stack = []
s = "()"

def validp(s):
    for c in s:

        if c in token:
            print(token[c], "=======",stack[-1] )  
            if stack and stack[-1] == token[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
            
        
    return True if not stack else False
    
print(validp(s))