n = int(input())

count = 1                     # 기본적인 최종 값 하나는 포함되기 때문에 1부터 시작
start_index = 1
end_index = 1   
sum = 1                       # 인덱스 처음은 1부터 시작

while end_index != n:
    if sum == n:              # 합이 n과 같은 경우
        end_index += 1
        sum += end_index
        count += 1
    elif sum > n:             # 합이 n보다 큰 경우
        sum -= start_index
        start_index += 1
    else:                     # 합이 n보다 작은 경우
        end_index += 1
        sum += end_index

print(count)