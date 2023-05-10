# 재귀함수는 반복문의 대체제
# n중 for문을 이용하려고 할 때 코드 유연성이 떨어질 때가 많음

def dfs(x):
    if x > 0:
        dfs(x - 1)
        print(x, end=" ")


if __name__ == "__main__":
    n = int(input())
    dfs(n)

# stack frame 원리
