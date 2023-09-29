import sys


def bfs(starti, startj, endi, endj):
    queue = []
    visited = [[0 for _ in range(M)] for _ in range(N)]

    queue.append((starti, startj))
    visited[starti][startj] = 1

    while queue:
        currenti, currentj = queue.pop(0)

        for deltai, deltaj in ((-1, 0), (1, 0), (0, -1), (0, 1),):
            nexti, nextj = currenti + deltai, currentj + deltaj
            if (0 <= nexti < N and 0 <= nextj < M
                    and arr[nexti][nextj] == 1
                    and visited[nexti][nextj] == 0):
                queue.append((nexti, nextj))
                visited[nexti][nextj] = visited[currenti][currentj] + 1

            if (currenti, currentj) == (endi, endj):
                return visited[endi][endj]


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

res = bfs(0, 0, N - 1, M - 1)
print(res)
