# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 22:50:26 2022

@author: Vikki
"""
ls = [2,7,11,15, 11]
t = 18
m = {}
for i in range(len(ls)):
    d = t - ls[i]
    
    if ls[i] in m.keys():
       print([m[ls[i]],i])
       
    m[d] =  i
 
    