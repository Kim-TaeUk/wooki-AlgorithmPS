N, K = map(int, input().split())
list = []

cnt = 0  # cnt 도입해서
for i in range(1, N + 1):
    if N % i == 0:
        cnt += 1  # 약수면 cnt 증가시켜 주면서
    if cnt == K:  # K번째이면
        print(i)  # 바로 출력
        break  # break해서 원하는 거 출력하면 굳이 끝까지 안찾아도 됨
else:  # 예외처리는 for - else로 해버리고
    print(-1)

# list에 일일이 약수를 넣고 K번째로 찾아가서 출력하는 것보다
# cnt 도입해서 K번째 찾고 바로 출력하는 것이 더 효율적
# K번째 찾으면 break해서 끝까지 안 찾는 것도 생각하기
# for - else 사용하기
