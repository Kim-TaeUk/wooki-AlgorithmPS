N, K = map(int, input().split())
list = []  # 약수를 저장할 list

for i in range(1, N + 1):  # 1부터 N까지 1씩 증가하면서
    if N % i == 0:  # N을 나눴을 때 나머지가 0이면 약수니까
        list.append(i)  # list에 추가

if len(list) < K:  # 약수의 개수가 K보다 작으면
    print(-1)  # -1 출력
else:
    print(list[K - 1])  # K번째 작은 수 출력
