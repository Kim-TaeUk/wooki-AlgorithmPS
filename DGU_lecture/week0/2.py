import random

N, M = map(int, input().split())

A = sorted(random.sample(range(1, 101), N))
B = sorted(random.sample(range(1, 101), M))
print("집합 A -", ', '.join(map(str, A)))
print("집합 B -", ', '.join(map(str, B)))

union = A + [x for x in B if x not in A]
intersection = [x for x in A if x in B]

print("합집합 -", ', '.join(map(str, sorted(union))))
print("교집합 -", ', '.join(map(str, intersection)))
