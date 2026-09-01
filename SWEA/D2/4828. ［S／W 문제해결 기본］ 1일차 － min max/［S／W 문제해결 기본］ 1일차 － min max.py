T = int(input())

for test_case in range(1, T + 1):
    result = 0
    
    N = int(input())
    list_a = list(map(int, input().split()))
    
    max_num, min_num = list_a[0], list_a[0]
    
    # for문으로 가장 큰 수와 가장 작은 수를 각각 저장
    for n in list_a:
        if n > max_num:
            max_num = n
        if n < min_num:
            min_num = n
    
    # result에 가장 큰 수 - 가장 작은 수 저장
    result = max_num - min_num
    
    print(f'#{test_case} {result}')