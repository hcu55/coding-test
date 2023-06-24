checkList = [0] * 4     # 비밀번호 체크 리스트
myList = [0] * 4        # 현재 상태 리스트
checkSecret = 0         # 몇 개의 문자와 관련된 개수를 충족했는지 판단하는 변수

def myadd(c):           # 문자가 들어올 때 호출하는 함수
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c):        # 문자가 삭제될 때 호출되는 함수
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1 
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split())
Result = 0          # 최종 유효한 비밀번호 개수
A = list(input())
checkList = list(map(int, input().split()))

for i in range(4):          # {'A','C','G','T'} 중 최소 개수가 0개 이면 무조건 조건을 만족하므로 checkSecret에 1 더해줌
    if checkList[i] == 0:
        checkSecret += 1

for i in range(P):          # 윈도우 크기만큼 앞에서부터 먼저 탐색
    myadd(A[i])
if checkSecret == 4:    # 만약 체크리스트 결과를 만족하면 최종 개수 +1
    Result += 1

for i in range(P, S):       # 윈도우를 오른쪽으로 이동 시키며 i는 추가 하는 문자열 j는 삭제하는 문자열  
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1

print(Result)