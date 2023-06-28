import sys
input = sys.stdin.readline
from collections import deque   # 덱을 사용하는 라이브러리 가져오기

N = int(input())
myQueue = deque()

for i in range(1, N+1):     # 덱에 1부터 추가
    myQueue.append(i)

while len(myQueue) > 1:     # 내 덱에 하나가 남을 때까지 반복
    myQueue.popleft()       # 맨 아래 카드를 뽑기 위해 popleft
    myQueue.append(myQueue.popleft())       # 그 다음 아래 카드를 뽑고 맨 위로 추가

print(myQueue.pop())    # 한장이 남았을 때 추출