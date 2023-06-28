N = int(input())
A = [int(input()) for _ in range(N)] 

for i in range(N-1):    # N개의 수를 두개씩 비교하면 N-1번 반복하게 됨
    for j in range(N-1-i):  # N-1-i만큼 반복
        if A[j] > A[j+1]: 
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp

for i in range(N):
    print(A[i])