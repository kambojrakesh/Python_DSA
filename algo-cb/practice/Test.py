

s = "abcabcde"
ll = list(s)
charSet = set()

l = 0
res = []

for r in range(len(s)):
    if ll[r] not in res:
        res.append(ll[l:r])
        
print(res)