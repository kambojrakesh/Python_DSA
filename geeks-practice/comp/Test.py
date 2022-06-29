test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'geeks' : 5, 'CS' : 6}
 
d = dict()
res = []
i = 0;
for key, v in test_dict.items():
    d[key] = test_dict[key]
    if i % 2 == 0:
        res.append(d)
        d = dict()
        
    i+=1
    
    
print(res)