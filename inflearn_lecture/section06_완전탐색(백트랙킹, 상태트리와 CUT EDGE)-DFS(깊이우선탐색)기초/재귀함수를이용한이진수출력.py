def dfs(x):
    if x == 0:
        return
    else:
        dfs(x // 2)
        print(x % 2, end="")


N = int(input())
dfs(N)
