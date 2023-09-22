import sys

attend = set()
student = set([x + 1 for x in range(30)])
for _ in range(28):
    attend.add(int(sys.stdin.readline().rstrip()))

print(min(list(student - attend)))
print(max(list(student - attend)))
