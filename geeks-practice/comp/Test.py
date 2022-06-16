test_str = 'gfg is best for geeks'
test_dict = {'geeks' : 1, 'best': 6}
 
res = " ".join(ele  for ele in test_str.split() if ele not in test_dict)
print(res)