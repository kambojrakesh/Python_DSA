# initialize dictionary
test_dict = {(4, 5) : '1', (8, 9) : '2', (10, 11) : '3'}

ls =[True for x in test_dict for i in x if 10 == i]

print(ls)


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

------------------------------------------------------------------------



#Input: [(1, 2, 3, 4, 5, 6), (1, 4),  (3, 5, 3, 4, 5, 6), (5, 7),    (5, 6), (4, 4)]
#Output:{1: [2, 3, 4, 5, 6, 4], 3: (5, 3, 4, 5, 6), 5: [7, 6], 4: [4]}

ls = [(1, 2, 3, 4, 5, 6), (1, 4),  (3, 5, 3, 4, 5, 6), (5, 7),    (5, 6), (4, 4)]

dic = {}
for l in ls:
    if l[0] in dic:
        dic[l[0]] = dic.get(l[0]) + l[1:]
    else:
        dic[l[0]] = l[1:]
        
print(dic)



-----------------------------

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))


# List of strings
l = ['sat', 'bat', 'cat', 'mat']
  
# map() can listify the list of strings individually
test = list(map(list, l))
print(test)

arr = [[1, 2, 3], [4, 5, 6], [2, 1, 2]]

print(sum(list(map(sum, arr))))
print(sum(map(sum,arr)) )


from operator import itemgetter
dict = {'a': 'Geeks', 'b': 'For', 'c': 'geeks'}
print([*dict])

dict = {'a': 'Geeks', 'b': 'For', 'c': 'geeks'}
ls = list(map(itemgetter(1), dict.items()))    
print(ls)

