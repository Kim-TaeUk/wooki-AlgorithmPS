import sys

word = sys.stdin.readline().rstrip()
lst = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
res = 0
for char in word:
    for idx, value in enumerate(lst):
        if char in value:
            res += (idx + 3)

print(res)
