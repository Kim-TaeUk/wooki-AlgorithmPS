from collections import Counter

N, M = map(int, input().split())

list = []
for i in range(1, N + 1):  # list에 나올 수 있는 수 모두 저장
    for j in range(1, M + 1):
        list.append(i + j)

cnt = Counter(list).most_common()
# most_common() 이용 -> tuple로 숫자-횟수로 저장
# 등장한 횟수를 내림차순을 정리함 -> cnt[0][1]에 최대 횟수가 저장되어 있음


res = []
for i in range(len(cnt)):
    if cnt[0][1] == cnt[i][1]:  # 최대 횟수가 같으면, 같은 확률로 등장하는 숫자이니까
        res.append(cnt[i][0])  # res에 append

res.sort()  # 그리고 정렬하여 출력
print(res)

# 최빈값 찾기 위해 Counter 이용함
