# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 03:21:25 2023

@author: Vikki
"""
#Rotate Image
matrix = [[1,2,3],[4,5,6],[7,8,9]]

output = [[7,4,1],[8,5,2],[9,6,3]]
temp1 = 0

l, r= 0, len(matrix) - 1

while l < r:
    for i in range(r):
        top, bottom = l, r
        
        temp1 = matrix[top + i][bottom]
        matrix[top + i][bottom]  = matrix[top][top + i]
        temp2 = matrix[bottom][bottom - i]
        matrix[top][top + i] = matrix[bottom - i][top]


        matrix[bottom][bottom - i]  = temp1
        matrix[bottom - i][top]  = temp2
    
    l = l + 1
    r = r - 1 
    
    
print(matrix)