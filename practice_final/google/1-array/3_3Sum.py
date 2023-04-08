# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:04:38 2022

@author: Vikki
"""
#area
nums = [-1,0,1,2,-1,-4]
nums = [1,2,-2,-1]
output = [[-1,-1,2],[-1,0,1]]
nums.sort()
res = []

print(nums)
for i, a in enumerate(nums):
    if i > 0 and a == nums[i-1]:
        continue
    
    l, r = i+1,  len(nums) - 1
    print("-----------------------",l, r)
    while l < r: 
        print(nums[l], nums[r])
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
print(res)