# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 19:20:04 2022

@author: Vikki
"""
res = []
digits = "29"

digitsToChar =  {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}


def beackTrack(i, curStr):
    if len(curStr) == len(digits):
        res.append(curStr)
        return
    

    for c in digitsToChar[digits[i]]:
        beackTrack(i+1, curStr + c)
        

        
if digits:
    beackTrack(0, "")
    
print(res)
