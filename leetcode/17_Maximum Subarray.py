# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:13:59 2022

@author: Vikki
"""
nums = [1]

l, r, m= 0, len(nums), len(nums)

csum = nums[0]
osum = nums[0]


for i in range(1, r):
    if csum >= 0 :
        csum += nums[i]
    else:
        csum = nums[i]
    
    if csum > osum :
        osum = csum


    
print(osum)


###############Best working#######################

osum = 0
csum = nums[0]

for i in nums:
    if osum > 0:
        osum = osum + i 
    else:
        osum = i

    csum = max(osum, csum)

print(csum)