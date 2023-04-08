# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 17:16:59 2023

@author: Vikki
"""
#Longest Substring

s = "pwwkew"
#3
if len(s) == 1:
    print(1)
    
stack = list()
l = 0
for i in s:  
    if i in stack:
        for j in stack.copy(): 
            stack.remove(j)
            if j == i:
                break
              

    stack.append(i)

    if len(stack) > l:
        l = len(stack)    
   
print(l)