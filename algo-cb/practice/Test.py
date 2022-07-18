from collections import defaultdict
# initializing dictionary
test_dict = {'gfg' : [1, 2, 3], 'is' : [1, 4], 'best' : [4, 2]} 
# Using defaultdict() + loop
res = defaultdict(list)
for key, val in test_dict.items():
    for ele in val:
        res[ele].append(key)

print(res)
