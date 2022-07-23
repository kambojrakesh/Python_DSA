# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 18:47:25 2022

@author: Vikki
"""



nums = [-1,0,1,2,-1,-4]
target = 0
nums.sort()
def tes(nums):
    res = []
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        l, r = i + 1,  len(nums) - 1

        while l < r:
            threeSum = nums[l] + nums[r]  + a

            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1

                while nums[l] == nums[l-1] and l < r:
                    l += 1 
    return res

            
print(tes(nums))
        