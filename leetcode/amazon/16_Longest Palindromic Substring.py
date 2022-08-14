# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 23:34:37 2022

@author: Vikki
"""
s = "babad"

res = ""
resLen = 0

for i in range(len(s)):
    #odd len
    l, r = i, i 
    print(l, "-------------------------------------------", r)
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if (r-l+1) > resLen:
            res = s[l:r+1]
            resLen = r - l +1 
        print(l, "==",r)
        l -= 1
        r += 1
    #even len
    l, r = i, i + 1
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if (r-l+1) > resLen:
            res = s[l:r+1]
            resLen = r - l +1 
        l -= 1
        r += 1            
print(res)