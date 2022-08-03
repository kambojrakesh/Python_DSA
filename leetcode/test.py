# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:13:59 2022

@author: Vikki
"""
s = "abca"
res = 0
charSet = set()
l =  0
for i in range(len(s)):
    while s[i] in charSet:
        charSet.remove(s[l])
        l += 1
    
    charSet.add(s[i])
    print(i, l, charSet)
    
    res = max(res, i - l + 1)
print(res)    