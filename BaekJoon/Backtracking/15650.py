import sys


def func(K, start):  # K개의 수를 선택한 상황에서 arr[K](K+1번째 수)를 정하는 함수
    global is_used
    # base condition
    if K == M:  # M개 골랐으니
        for i in range(M):
            print(arr[i], end=' ')  # 출력하고
        print()
        return  # 종료

    # K != M
    # 이전에 선택한 수 이후부터만 새로운 수를 선택하게 하기 위해 start 도입
    for i in range(start, N + 1):  # start부터 N까지 수를 차례대로 확인
        if not is_used[i]:  # i가 쓰이지 않은 수라면
            arr[K] = i  # arr에 넣고
            is_used[i] = True  # 쓴 수라고 체크하고
            func(K + 1, i + 1)  # 다음 수 찾기 위해 호출

            # 여기 왔다는 건 arr[K] = i로 둔 상태에서 func(K + 1)에 들어갔다가 모든 과정이 끝났다는 뜻이므로
            # 안쓰이고 있다고 명시 -> 상태를 되돌리는!
            is_used[i] = False


N, M = map(int, sys.stdin.readline().split())
arr = [0] * M  # 수열을 담을 배열
is_used = [False] * (N + 1)  # 특정 수가 쓰였는지
func(0, 1)  # start 인덱스는 1부터!
