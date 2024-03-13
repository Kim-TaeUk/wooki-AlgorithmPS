import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
lst = sorted(list(map(str, sys.stdin.readline().split())))
vowels = ['a', 'e', 'i', 'o', 'u']

for i in combinations(lst, L):
    vowel_cnt = sum(1 for char in i if char in vowels)
    consonant_cnt = L - vowel_cnt
    if vowel_cnt < 1 or consonant_cnt < 2:
        continue
    print("".join(map(str, i)))
