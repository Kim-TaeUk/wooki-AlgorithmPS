import sys


def func(K, start):
    if K == M:  # M개 골랐으니
        for i in range(M):
            print(arr[i], end=' ')  # 출력하고
        print()
        return

    for i in range(start, N + 1):  # start부터 N까지 수를 차례대로 확인
        arr[K] = i  # arr에 넣고
        func(K + 1, i)  # 다음 수 찾기 위해 호출 - 다음 수를 고른 수 포함해서 찾도록 i로 설정


N, M = map(int, sys.stdin.readline().split())

arr = [0] * M  # 수열을 담을 배열
func(0, 1)
