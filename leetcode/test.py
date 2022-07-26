# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:13:59 2022

@author: Vikki
"""
l1 = [1,2,3]
l2 = [0,5,6]

def linear_merge(list1, list2):
  result = []
  #Look at the two lists so long as both are non-empty.
  #Take whichever element [0] is smaller.
  while list1 and list2: 
    print(list1[0], "-------------------------",list2[0])
    if list1[0] < list2[0]:
        x = list1.pop(0)
        #print(x)
        result.append(x)
    else:
        x1 = list2.pop(0)
        #print(x1)
        result.append(x1)
  #Now tack on what's left
  result.extend(list1)
  result.extend(list2)
  return result

print(linear_merge(l1, l2))