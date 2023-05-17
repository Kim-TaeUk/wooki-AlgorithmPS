def dfs(vertex):
    if vertex == n + 1:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=" ")
        print()
    else:
        ch[vertex] = 1
        dfs(vertex + 1)
        ch[vertex] = 0
        dfs(vertex + 1)


if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n + 1)
    dfs(1)
