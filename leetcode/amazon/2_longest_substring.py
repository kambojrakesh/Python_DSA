# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 00:15:53 2022

@author: Vikki
"""
s = "Vikki"
charSet = set()
l = 0
res = 0

for r in range(len(s)):
    while s[r] in charSet:
        charSet.remove(s[l])
        l += 1
        
    charSet.add(s[r])
    res = max(res, r - l + 1)
    
    
print(res)
    

    
