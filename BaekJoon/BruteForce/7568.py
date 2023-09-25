import sys

N = int(sys.stdin.readline().rstrip())

people = []
for _ in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    people.append((weight, height))

for i in range(N):
    cnt = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    print(cnt, end=" ")
