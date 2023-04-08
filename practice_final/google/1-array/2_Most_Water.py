# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:28:13 2022//////////////////

@author: Vikki
"""
height = [1,8,6,2,5,4,8,3,7]
height = [1, 1]

i = 0
j =  len(height) - 1
area = 0

while i < j:
    area = max(area, (j-i) * min(height[i], height[j]))
    if height[i] < height[j]:
        i = i + 1
    else:
        j = j - 1
    
print(area)

