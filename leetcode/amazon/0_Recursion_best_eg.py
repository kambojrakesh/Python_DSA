# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:13:59 2022

@author: Vikki
"""
res = []
digits = "29"

digitsToChar =  {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}


def beackTrack(i, curStr):
    if len(curStr) == len(digits):
        print("-------------------------", curStr)
        res.append(curStr)
        return
    

    for c in digitsToChar[digits[i]]:
        print(i+1, "=====================", curStr + c)
        beackTrack(i+1, curStr + c)
        
 
if digits:
    beackTrack(0, "")
    
print(res)
