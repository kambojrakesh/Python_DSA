# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 10:05:08 2022

@author: Vikki
"""
def multiply(num1, num2):

    n = len(num1)
    m = len(num2)
    result = [0] * (n + m)
    
    
    
    for i in range(n - 1, -1, -1):
        carry = 0
        for j in range(m - 1, -1, -1):
            
            result[i + j + 1] += int(num1[i]) * int(num2[j]) + carry
            
            carry = result[i + j + 1] // 10
            
            result[i + j + 1] %= 10
            
        result[i] += carry
        
        
    result = "".join(str(d) for d in result)
    result = result.lstrip("0")
    if result == "":
        return "0"
    return result

num1 = "123"
num2 = "456"

print(multiply(num1, num2))