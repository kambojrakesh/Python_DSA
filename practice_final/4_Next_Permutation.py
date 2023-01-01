# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 18:23:01 2022

@author: Vikki
"""
#Next Permutation
arr = [1,2,3] 
outp =  [1,3,2]
arr = [2,3,1] 
outp = [3,1,2]
arr = [1,3,2]
outp = [2,1,3]

def next_permutation(nums):
    # Find the rightmost element that is smaller than its successor
    i = len(nums) - 2
    a = i
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
     
    
    if i < 0:
        # nums is already the last permutation
        return False
    
    # Find the successor of nums[i]
    j = len(nums) - 1
    while nums[j] <= nums[i]:
        j -= 1
    
    # Swap nums[i] and nums[j]
    nums[i], nums[j] = nums[j], nums[i]

    # Reverse the suffix starting at nums[i + 1]
    k = i + 1
    l = len(nums) - 1
    while k < l:
        nums[k], nums[l] = nums[l], nums[k]
        k += 1
        l -= 1   
    return nums

arr = [1, 3, 4,7,2]
print(next_permutation(arr))

