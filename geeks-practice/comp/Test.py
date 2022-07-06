# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 16:11:26 2022

@author: Vikki
"""
s1 = "abcabcbb"
s = list(s1)

sub = []
t = set()
for i  in range(0, len(s)):    
    if s[i] in sub:
        t.add(len(sub)+ 1)
        sub = []            
    sub.append(s[i])



print(len(t))