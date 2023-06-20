import sys
input = sys.stdin.readline

n, m = map(int, input().split())  
print(n)           # n: 리스트 크기, m: 질문 수
A = [[0] * (n+1)]                            # 원본 리스트
D = [[0] * (n+1) for _ in range(n+1)]        # 합 배열

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)
    
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]     # 배열의 합
        
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]  # 구간 합 배열로 질의를 계산
    print(result)