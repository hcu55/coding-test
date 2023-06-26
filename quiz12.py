import sys
input = sys.stdin.readline

N = int(input())
answer = [0] * N
A = list(map(int, input().split()))
Stack =[]
result = ""

for i in range(N):
    # 스택이 비어 있지 않고 현재 수열이 스택 top 인덱스가 가리키는 수열보다 클 경우
    while Stack and A[Stack[-1]] < A[i]:
        answer[Stack.pop()] = A[i]
    Stack.append(i)     # 스택이 비어 있거나 top인덱스가 더 작은 경우에 추가

while Stack:    # 반복문 다 돌고 왔는데 스택에 남아 있는 경우
    answer[Stack.pop()] = -1

for i in range(N):
    sys.stdout.write(str(answer[i]) + " ")