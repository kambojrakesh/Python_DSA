# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 22:54:06 2023

@author: Vikki
"""
s = "a"
t = "aa"
h = s
d = {}
ls = []

if len(s) < len(t):
    return ""


if len(s) == len(t) & s != t:
    return ""

for i, v in enumerate(s):
    if v in t:
        d[v] = i
    
    if "".join(sorted(list(d.keys()))) == t:
        ls.append(d)
        d = {}
        
for li in ls:
    li1 = list(li.values()) 
    f = li1[0]
    l = li1[len(t) - 1]
    
    if len(s[f:l+1]) < len(h):
        h = s[f:l+1]
        
    
return h    
    
    