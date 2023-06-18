import sys
input = sys.stdin.readline

n, m = map(int, input().split())             # n: 수열 개수, m: 나누는 수
array = list(map(int, input().split()))      # A: 원본 수열 리스트 저장
sum_array = [0] * n
count = [0] * m                              # 같은 나머지의 인덱스를 카운트하는 리스트
sum_array[0] = array[0]         
answer = 0

for i in range(1, n):
    sum_array[i] = sum_array[i-1] + array[i]

for i in range(n):
    remainder = sum_array[i] % m
    if remainder == 0:
        answer += 1
    count[remainder] +=1 

for i in range(m):
    if count[i] > 1:
        answer += (count[i] * (count[i] - 1) // 2)

print(answer)