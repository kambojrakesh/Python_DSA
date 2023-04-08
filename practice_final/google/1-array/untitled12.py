# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 00:36:19 2023

@author: Vikki
"""
token = {")":"(", "]":"[", "}":"{"}

stack = []
s = "())"

def validp(s):
    for c in s:

        if c in token: 
            if stack and stack[-1] == token[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
            
        
    return True if not stack else False
    
print(validp(s))