import sys


def dfs(current):
    # 단위 작업
    ans_dfs.append(current)
    visited[current] = 1

    for vertex in adj[current]:
        if visited[vertex] == 0:
            dfs(vertex)


def bfs(start):
    # 초기 작업 -> queue 만들기
    queue = []

    # 단위 작업
    queue.append(start)  # 일단 queue에 첫번째 start 넣기
    ans_bfs.append(start)
    visited[start] = 1

    while queue:  # queue가 빌 때까지
        current = queue.pop(0)  # queue에서 하나씩 뽑으면서 쭉쭉

        for vertex in adj[current]:
            if visited[vertex] == 0:
                # 단위 작업
                queue.append(vertex)
                ans_bfs.append(vertex)
                visited[vertex] = 1


N, M, V = map(int, sys.stdin.readline().split())

# adjacent arr 생성
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    adj[s].append(e)
    adj[e].append(s)

# 문제 조건이니까 오름차순 정렬해주기
for i in range(1, N + 1):
    adj[i].sort()

visited = [0] * (N + 1)  # 방문했는지 확인할 visited arr
ans_dfs = []  # 답 넣을 arr
dfs(V)

visited = [0] * (N + 1)  # 방문했는지 확인할 visited arr
ans_bfs = []  # 답 넣을 arr
bfs(V)

print(*ans_dfs)
print(*ans_bfs)
