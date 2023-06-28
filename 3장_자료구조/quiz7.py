N = int(input())
M = int(input())
A = list(map(int, input().split()))

i = 0                               # 시작 인덱스
j = N - 1                           # 마지막 인덱스
count = 0                           # 정답 개수

A.sort()                            # 리스트 자동 정렬

while i<j:
    if A[i] + A[j] < M:
        i += 1
    elif A[i] + A[j] > M:
        j -= 1
    else:
        i += 1
        j -= 1
        count += 1

print(count)