import sys
input = sys.stdin.readline  # 백준에서 없이 제출하니 시간초과가 나서 붙임

N = int(input())
A = [int(input()) for _ in range(N)]    # 수열 리스트 채우기

stack = []  # 스택
num = 1     # 자연수 1부터 시작
result = True
answer = ""

for i in range(N):
    now_num = A[i]
    if now_num >= num:
        while now_num >= num:    # 현재 수열값 >= 오름차순 자연수: 값이 같아질 때까지 append() 수행
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:       # 현재 수열값 < 자연수 : pop()을 수행해 수열 원소를 꺼냄
        n = stack.pop()
        if n > now_num:     # 스택의 가장 위의 수가 만들어야 하는 수열의 수보다 크면 수열을 출력할 수 없다.
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)
