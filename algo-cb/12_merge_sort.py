# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:09:45 2022

@author: Vikki
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    
    left = arr[:mid]
    right = arr[mid:]
    

    merge_sort(left)
    merge_sort(right)
    return merge_two(left, right, arr)
    
def merge_two(left, right, arr):
    i = j = k = 0


    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k +=1 
        
        
    while i < len(left):
        arr[k] = left[i]
        i+=1
        k+=1

    while j < len(right):
        arr[k] = right[j]
        j+=1
        k+=1
    return arr
    

if __name__ == '__main__':
    test_cases = [
        [11, 9,18,7,12,3,14,6],
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)