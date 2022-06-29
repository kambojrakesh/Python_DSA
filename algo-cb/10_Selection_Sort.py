# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:06:51 2022

@author: Vikki
"""
ls = [89, 78, 61, 53, 1, -1, 23, 21, 17, 12, 9, 7, 6, 2, 111]

for j in range(0, len(ls)-1):
    min_index = j
    for i in range(j, len(ls)):
        if ls[min_index] > ls[i]:
            min_index = i


    ls[j], ls[min_index] = ls[min_index] , ls[j]       
  
print(ls)