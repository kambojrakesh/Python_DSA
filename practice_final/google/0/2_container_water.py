# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:27:12 2023

@author: Vikki
"""
height = [1,3,2,5,25,24,5]
#Output: 49

i = 0
j = len(height) - 1
area = min(height)
while i < j:
    jj = height[j]
    ii = height[i]
    h = min(jj, ii)
    a =  h * (j -i)
    
    if ii == jj:
        i = i + 1 
    
    if a > area:
        area = a
 
    if height[i] <= jj:
        i = i + 1
    elif height[i] > jj:
        j = j - 1
    
print(area)