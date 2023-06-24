from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
mydeque = deque();
now = list(map(int, input().split()))

for i in range(N):
    # 아이디어 1.나보다 큰 데이터 삭제하기
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i], i))
    # 아이디어 2.슬라이딩 윈도우 벗어난 데이터 삭제
    if mydeque[0][1] <= i - L:      # 윈도우 범위를 벗어나면
        mydeque.popleft()
    print(mydeque[0][0], end=' ')