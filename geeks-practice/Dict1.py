#https://www.geeksforgeeks.org/python-extract-unique-values-dictionary-values/
from itertools import chain
from nltk import flatten
test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}
#The unique values list is : [1, 2, 5, 6, 7, 8, 10, 11, 12]
l = []

l1 = list(set(flatten(list( value for value in test_dict.values()))))

print(l1)





import itertools
l2 = list( value for value in test_dict.values())

print(list(itertools.chain(*l2)))

