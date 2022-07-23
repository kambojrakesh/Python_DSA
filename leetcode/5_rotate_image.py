# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 10:16:37 2022

@author: Vikki
"""
matrix = [[1,2,3],[4,5,6],[7,8,9]]
o = [[1,2,3],[4,5,6],[7,8,9]]


l, r = 0, len(matrix) - 1 
while l < r:
    for i in range(r - l):
        top, bottom = l, r
        
        topleft = matrix[top][l + i]
    
        matrix[top][l + i] = matrix[bottom - i][l]
        
        matrix[bottom - i][l] = matrix[bottom][r - i]

        matrix[bottom][r - i] = matrix[top +  i][r] 

        matrix[top + i][r] = topleft

    r -= 1
    l += 1
print(matrix)  
print(o)      