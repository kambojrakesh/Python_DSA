# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 15:15:14 2022

@author: Vikki
"""
s = "applepenapple"
b = s
wordDict = ["apple","pen"]
b = s
j = 1
f = ""
l = len(s)+1
for i in range(1, l):  
    v = s[0:j]
    if v in wordDict:
        f = f + v
        s = s.replace(v, '')
        wordDict.remove(v)
        j = 1
    else:
        j += 1

print(b,f)