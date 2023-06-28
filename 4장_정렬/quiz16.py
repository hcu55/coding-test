import sys
input = sys.stdin.readline

N = int(input())
A =[]

for i in range(N):
    A.append((int(input()), i))  # 인덱스 순서를 알기 위해 인덱스 값과 리스트 값 동시 입력 받음

no_sort = 0
sorted_A = sorted(A)    # sort()와 sorted() 차이가 있다.

for i in range(N):
    if no_sort < sorted_A[i][1] - i:    # 정렬 전 index - 정렬 후 index 계산의 최댓값 저장
        no_sort = sorted_A[i][1] - i

print(no_sort + 1)  # 정렬이 다 완료 된 후 한번 더 for문을 돌기 때문에 1을 더해줌