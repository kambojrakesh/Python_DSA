# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 02:40:29 2022

@author: Vikki
"""

def twoNumberSum1(array, targetSum):
    # Write your code here.
    #print(array, "===========", targetSum)
    for i in array:
        for j in array:
            #sum1 = i + j
            if i + j == targetSum and  i != j:
                #print(sum1, "---", [i, j])
                return [i, j]
            #prev = i
    return []

a = [3, 5, -4, 8, 11, 1, -1, 6]
def twoNumberSum(array, targetSum):
    for i in range(len(array)):
        f = array[i]
        for j in range(i + 1, len(array)):
            l = array[j]
            if l + f == targetSum:
                return [l, f]

#print(len(a), a[7])        
print(twoNumberSum(a, 10))