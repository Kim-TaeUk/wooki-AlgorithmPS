N, K = map(int, input().split())
list = list(map(int, input().split()))

res = []

for i in range(N):  # 3중 for문으로
    for j in range(i + 1, N):
        for m in range(j + 1, N):
            res.append(list[i] + list[j] + list[m])  # 3장의 카드의 합을 구해서 list res에 append

res.sort(reverse=True)  # 내림차순 정렬하고
set(res)  # set으로 만들고
print(res[K - 1])  # K번째 출력

# 카드니까 중복으로 뽑는게 없는걸 생각 못하고 헤멤

# 풀이에서는 res를 set으로 받고 list로 바꾼 다음에 정렬 -> 순서는 별로 안중요한듯 싶다
