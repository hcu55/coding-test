import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

count = 0

for k in range(N):
    result = arr[k]
    i = 0
    j = N - 1
    while i < j:
        if arr[i] + arr[j] == result:       
            if i != k and j != k:               # i, j가 모두 k가 아닐 때 count 증가 및 while문 종료
                count += 1
                break
            elif i == k:                        # i가 k랑 같은 경우 i 값 증가
                i += 1
            elif j == k:                        # j가 k랑 같은 경우 j 값 감소
                j -= 1
        elif arr[i] + arr[j] < result:
            i += 1
        else:
            j -= 1

print(count)