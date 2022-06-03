https://www.geeksforgeeks.org/tag/python-dictionary-programs/

https://www.geeksforgeeks.org/python-dictionary-exercise/

https://docs.python.org/3.8/library/stdtypes.html#dict-views

https://docs.python.org/3/library/collections.html


dict = {'ravi': '10', 'rajnish': '9', 'sanjeev': '15', 'yash': '2', 'suraj': '32'}
dict1 = dict.items() --> list( tuple())

dict_items([('ravi', '10'), ('rajnish', '9'), ('sanjeev', '15'), ('yash', '2'), ('suraj', '32')])

Dictionary has O(1) search time complexity whereas List has O(n) time complexity

----------------------------------------------

print(country_code.get('Japan', 'Not Found'))

-------------------------------------------

defd = collections.defaultdict(lambda : 'Key Not found') --> set defaukt key for all absent key

----------------------------------------------

sorted(lis, key=itemgetter('age', 'name')) --> sort dict accoring jto key age and name

-----------------------------------------------


sorted(lis, key = lambda i: i['age'],reverse=True)


-------------------------------------------------


dict2.update(dict1)
dict = dict1 | dict2

res = {**dict1, **dict2}
-----------------------------

