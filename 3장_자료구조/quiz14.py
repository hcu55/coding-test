from queue import PriorityQueue
import sys
input = sys.stdin.readline
print = sys.stdout.write        

N = int(input())
myQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()        # 우선순위 큐의 값 삭제해서 temp변수에 넣음
            print(str(temp[1])+'\n')    # temp변수에 (x,y) 형태니까 y값인 1번 출력
    else:
        myQueue.put((abs(request), request)) # 절댓값을 기준으로 정렬하고 같으면 음수 우선 정렬하도록 구성