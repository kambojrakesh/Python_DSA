# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 15:10:23 2022

@author: Vikki
"""
s = "loveleetcode"

from collections import Counter

s = Counter(s)
v = False
k1 = -1
for k, v in s.items():
    if v == 1:
        k1 = s.index(k)
        break
print(k1)