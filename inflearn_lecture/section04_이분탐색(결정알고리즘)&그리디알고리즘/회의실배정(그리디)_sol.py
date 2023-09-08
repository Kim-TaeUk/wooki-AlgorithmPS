n = int(input())
meeting = []
for i in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))  # list에 tuple 형태로 넣기

meeting.sort(key=lambda x: (x[1], x[0]))  # 1번째 index가 1순위, 0번째 index가 2순위로

endtime = 0
cnt = 0

for start, end in meeting:
    if start >= endtime:
        endtime = end
        cnt += 1

print(cnt)
