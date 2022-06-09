# initialize dictionary
test_dict = {(4, 5) : '1', (8, 9) : '2', (10, 11) : '3'}

ls =[True for x in test_dict for i in x if 10 == i]

print(ls)