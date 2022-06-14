from collections import Counter
test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]



res = {key : [key] * val for key, val in Counter(test_list).items()}
print(res)