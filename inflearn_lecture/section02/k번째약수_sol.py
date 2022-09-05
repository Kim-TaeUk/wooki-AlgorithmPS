N, K = map(int, input().split())
list = []

cnt = 0
for i in range(1, N + 1):
    if N % i == 0:
        cnt += 1
    if cnt == K:
        print(i)
        break
else:
    print(-1)

# list에 일일이 약수를 넣고 K번째로 찾아가서 출력하는 것보다
# cnt 도입해서 K번째 찾고 바로 출력하는 것이 더 효율적
# K번째 찾으면 break해서 끝까지 안 찾는 것도 생각하기
# for - else 사용하기
