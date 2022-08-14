# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:13:59 2022

@author: Vikki
"""
s = "abc"

max_len = 1
size = len(s)
dp=[[False]*size for _ in range(size)]
for start in range(size-1,-1,-1):
    for end in range(start,size):
        print(start, end)
        
        
print(dp)