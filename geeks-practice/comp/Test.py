val = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]


from collections import Counter 
counter = Counter()

dc = {}
for i in val:
    dc[i] = val.count(i)
    
print(dc)


count = {1:8}
for i in val:
    count[i] = count.get(i) 
    
print(count)