import sys


def func(cur, tot):
    global cnt
    if cur == N:  # 부분 집합 생성에 모든 원소를 고려해야하기 때문에 cur이 N까지 갔는지 확인해야 함
        if tot == S:
            cnt += 1
        return
    func(cur + 1, tot)  # 현재 원소를 부분 집합에 포함X
    func(cur + 1, tot + lst[cur])  # 현재 원소를 부분 집합에 포함


N, S = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

cnt = 0
func(0, 0)
if S == 0:
    cnt -= 1  # 공집합 제거
print(cnt)
