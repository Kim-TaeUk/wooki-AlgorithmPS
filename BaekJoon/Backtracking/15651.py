import sys


def func(K):
    # base condition
    if K == M:  # M개 골랐으니
        for i in range(M):
            print(arr[i], end=' ')  # 출력하고
        print()
        return  # 종료

    # K != M
    for i in range(1, N + 1):  # 1부터 N까지의 수를 차례대로 확인
        # 중복 허용이기 때문에 is_used로 체크하지 않음!
        arr[K] = i  # arr에 넣고
        func(K + 1)  # 다음 수 찾기 위해 호출


N, M = map(int, sys.stdin.readline().split())
arr = [0] * M  # 수열을 담을 배열
func(0)
