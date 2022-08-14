# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 15:15:14 2022

@author: Vikki
"""


word = "aaaaaaa"
words = ["aaaa","aaa"]

def wordBreak(words, word, out=''):

    if not word:
        return out==word
 
    for i in range(1, len(word) + 1):
        prefix = word[:i]
        print(prefix)
        if prefix in words:
            print("==========================")
            wordBreak(words, word[i:], out + '' + prefix)
            
            
          