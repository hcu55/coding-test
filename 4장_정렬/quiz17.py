import sys
input = sys.stdin.readline
print = sys.stdout.write

A = list(input())

for i in range(len(A)):
    Max = i     # Max 변수에 첫번째 i 값 임시로 넣음
    for j in range(i+1, len(A)):    # i값 다음의 값부터 비교
        if A[j] > A[Max]:   # j값이 Max값보다 크다면
            Max = j
    if A[i] < A[Max]:       # Max 값을 맨 처음 i값으로 정렬 시켜주는 작업
        temp = A[i]
        A[i] = A[Max]
        A[Max] = temp

for i in range(len(A)):
    print(A[i])