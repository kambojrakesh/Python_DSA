from operator import itemgetter
test_dict = {'a': 'Geeks', 'b': 'For', 'c': 'geeks'}
# Using chain.from_iterable()
from itertools import chain
from itertools import repeat

res = dict(zip(range(4), repeat(test_dict))) # return 4 same key valu pair for test_dic
print(repeat(test_dict))