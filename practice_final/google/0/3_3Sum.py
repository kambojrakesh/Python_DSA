# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 00:20:09 2023

@author: Vikki
"""
nums = [0,-4,-1,-4,-2,-3,2]#[1,2,-2,-1]
#[[-1,-1,2],[-1,0,1]]
#[-4, -1, -1, 0, 1, 2]
nums  = sorted(nums)

ls1 = []

for k in range(len(nums)):

    if k > 0 and nums[k] == nums[k-1]:
        continue
    
    i = k + 1
    a = nums[k]
    j = len(nums)-1 
    while i < j:
        l = nums[i]
        r = nums[j]
            
        if a + l + r == 0 and [a,l,r] not in ls1:
            ls1.append([a, l, r])
            
        if a + l + r < 0:
            i = i + 1
        else:
            j = j - 1

print(ls1)
    
    
    
