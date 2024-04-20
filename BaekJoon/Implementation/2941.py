import sys

word = sys.stdin.readline().rstrip()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for x in croatia:
    word = word.replace(x, "a")

print(len(word))
