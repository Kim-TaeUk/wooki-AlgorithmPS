import sys
from collections import deque


def dfs(current):
    # 단위 작업
    ans_dfs.append(current)  # 방문한 곳 추가
    visited[current] = True  # 방문 표시!

    for vertex in adj[current]:  # 방문해서
        if not visited[vertex]:  # 방문하지 않은 곳이면
            dfs(vertex)  # 방문! DFS니까


def bfs(start):
    queue = deque()  # 필요한 변수 생성: queue

    queue.append(start)  # queue에 시작 데이터(들) 삽입
    # 단위 작업
    ans_bfs.append(start)  # 방문한 곳 추가
    visited[start] = True

    while queue:  # queue에 데이터가 있는 동안
        current = queue.popleft()  # queue에서 데이터 빼주고

        for vertex in adj[current]:  # 방문해서
            if not visited[vertex]:  # 방문하지 않은 곳이면
                # queue에 삽입하자! BFS니까
                queue.append(vertex)
                ans_bfs.append(vertex)
                visited[vertex] = True


N, M, V = map(int, sys.stdin.readline().split())

# adjacent arr 생성
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    # 양방향이기 때문에 star <-> end 넣어주기
    adj[start].append(end)
    adj[end].append(start)

# 문제 조건대로 오름차순 정렬(<- 정점 번호가 작은 것부터 방문해야하니까)
for i in range(1, N + 1):
    adj[i].sort()

# 방문한 거 체크하는 배열, answer 배열 생성
visited = [False for _ in range(N + 1)]
ans_dfs = []
dfs(V)  # 시작지점 함수에 넣고 시작!

visited = [False for _ in range(N + 1)]
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)
