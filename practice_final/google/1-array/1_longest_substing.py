# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 23:22:49 2022

@author: Vikki
"""
import time
s = "abcabcbb"
#s = "bbbbb"
s = "pwwkew"

dc = {}
start = 0
ln_st = ""

for i, c in enumerate(s):
    if c in dc:
        start = max(start, dc[c]+1)
        
    print(start)
    ln_st = max(ln_st, s[start: i+1], key=len)

    dc[c] = i
    time.sleep(10)
   
print(ln_st)
