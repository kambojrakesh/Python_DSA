# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 15:03:20 2022

@author: Vikki
"""
import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + " mil sec")
        return result
    return wrapper