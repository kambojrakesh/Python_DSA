from collections import defaultdict  
test_dict = {'gfg' : {'x' : 5, 'y' : 6}, 'is' : {'x' : 1, 'y' : 4},
                                      'best' : {'x' : 8, 'y' : 3}}
#[(‘x’, (5, 1, 8)), (‘y’, (6, 4, 3))]
res = defaultdict(tuple)
for key, val in test_dict.items():
    for ele in val:
        res[ele] += (val[ele], )
        
print(str(list(res.items())))