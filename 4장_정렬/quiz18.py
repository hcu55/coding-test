import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
S = [0] * N

for i in range(1, N):                # 0번째는 의미가 없으니 1부터 N까지 
    insert_point = i                 # 삽입 인덱스 번호 초기화
    insert_value = A[i]              # 인덱스 값 초기화
    for j in range(i-1, -1, -1):     # i-1 부터 0까지 뒤에서부터 크기 비교
        if A[j] < A[i]:
            insert_point = j + 1
            break
        if j == 0:                   # 현재 비교하는 인덱스 값이 가장 작을 때
            insert_point = 0 
    for j in range(i, insert_point, -1):    # i부터 inser_point까지 뒤에서 부터 인덱스를 한칸 밀기
        A[j] = A[j-1]
    A[insert_point] = insert_value      # 현재 인덱스 값 삽입 위치에 넣기

S[0] = A[0]     # 0번 인덱스 값은 그대로 넣기

for i in range(1, N):   # 합 배열
    S[i] = S[i-1] + A[i]

sum = 0

for i in range(0, N):   # 합 배열 총합
    sum += S[i]

print(sum)