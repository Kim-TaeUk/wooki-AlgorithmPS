import sys


def dfs(current):
    global cnt  # 전역 변수로 생성해주기

    # 들어오면 단위 작업!
    cnt += 1  # 방문 횟수 +1
    visited[current] = 1  # 방문했으니까 체크

    # adjacent arr에서 depth first로 들어가기
    for com in adj[current]:
        if visited[com] == 0:  # 방문 안한 곳이면 거기서 더 들어가기
            dfs(com)


N = int(sys.stdin.readline().rstrip())
pairs = int(sys.stdin.readline().rstrip())

# adjacent arr 생성
adj = [[] for _ in range(N + 1)]

for _ in range(pairs):
    com1, com2 = map(int, sys.stdin.readline().split())
    adj[com1].append(com2)
    adj[com2].append(com1)  # bidirectional 이니까 양쪽 다 추가

cnt = 0
visited = [0] * (N + 1)  # 방문했는지 확인할 visited arr
dfs(1)
print(cnt - 1)
