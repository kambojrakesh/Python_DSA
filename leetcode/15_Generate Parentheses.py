# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 16:20:12 2022

@author: Vikki
"""
stack = []
n = 2
res = []

def back_track(openN, closedN):
    
    if openN== closedN == n:
        print("************",openN,closedN,n)
        res.append("".join(stack))
        
    if openN < n:
        stack.append("(")
        print("------------",stack, openN+1, n)
        back_track(openN+1 , closedN)
        #stack.pop()
        
    if closedN < openN:
        stack.append(")")
        print("============",stack, openN, closedN+1)

        back_track(openN , closedN+1)
        #stack.pop()               
                  
back_track(0, 0)

print(res)    
    