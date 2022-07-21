# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 01:05:25 2022

@author: Vikki
"""
height = [1,8,6,2,5,4,8,3,7]

i = 0
j = len(height) - 1
area = 0
while i < j:
    left = height[i]
    right = height[j]
    
    m = min(left, right)
    d = j - i
     
    area = max(area, m * d)
    
    if left < right:
        i += 1
    else:
        j -= 1
        
print(area)
    
    