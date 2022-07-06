# R - 3

n = int(input())
set = []

# [A , B]를 입력받아서 정렬
for i in range(n):
    set.append(list(map(int, input().split())))

set = sorted(set, key=lambda x: (x[0]))
# print(set)
X = 0
for i in range(len(set)):  # 반복문 이용해서
    if X >= set[i][0]:  # X >= A이면 B를 더한다
        X += set[i][1]

if X == 0:
    print(-1)
else:
    print(X)
