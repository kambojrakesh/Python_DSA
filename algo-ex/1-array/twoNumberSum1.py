# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 02:40:29 2022

@author: Vikki
"""
def twoNumberSum(array, targetSum):
    # Write your code here.
    #print(array, "===========", targetSum)
    nums={}
    for x in array:
       y = targetSum - x
       print(nums, "--", y)
       
       if y in nums:
           return [x, y]
       else:
           nums[x]=True
    return []

#a = [3, 5, -4, 8, 11, 1, -1, 6]
a = [1,2,3,4]      
print(twoNumberSum(a, 6))