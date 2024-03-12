from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement

lst = [1, 2, 3, 4]

# 순열 (permutations) - 순서O, 중복X
for i in permutations(lst, 2):
    print(i)
'''
(1, 2), (1, 3), (1, 4)
(2, 1), (2, 3), (2, 4)
(3, 1), (3, 2), (3, 4)
(4, 1), (4, 2), (4, 3)
'''

# 중복 순열 (product) - 순서O, 중복O
for i in product(lst, lst, repeat=1):
    print(i)
'''
(1, 1), (1, 2), (1, 3), (1, 4)
(2, 1), (2, 2), (2, 3), (2, 4)
(3, 1), (3, 2), (3, 3), (3, 4)
(4, 1), (4, 2), (4, 3), (4, 4)
'''

# 조합 (combinations) - 순서X, 중복X
for i in combinations(lst,2):
    print(i)
'''
(1, 2), (1, 3), (1, 4)
(2, 3), (2, 4)
(3, 4)
'''

# 중복 조합 (combinations_with_replacement) - 순서X, 중복O
for i in combinations_with_replacement(lst,2):
    print(i)
'''
(1, 1), (1, 2), (1, 3), (1, 4)
(2, 2), (2, 3), (2, 4)
(3, 3), (3, 4)
(4, 4)
'''