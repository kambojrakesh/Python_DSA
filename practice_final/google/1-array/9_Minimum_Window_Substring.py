# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 04:49:02 2023

@author: Vikki
"""

#Minimum Window Substring
s = "aa"
t = "aa"
ls = []
d = {}
r1, r2 = 0, 0
m = len(s)

for i, c in enumerate(s):
    if c in t:
        d[c] = i

    if "".join(sorted(list(d.keys()))) == t:
        v1 = list(d.keys())[len(t)-1]
        v2 = list(d.keys())[0]
        f = d.get(v1 )
        z = d.get(v2)
        m1 = min(m, f-z)
        print(m1)
        if m1 < m:
           r1, r2 = z, f +1
           print(r1, r2)
        d = {}
        m = m1
        
if t == sorted(s):
    print( t)
if len(s) < len(s): 
    print("")  
    
print(s[r1:r2])