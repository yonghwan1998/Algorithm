T = int(input())

for test_case in range(1, T + 1):
    result_n, result_cnt = 0, 0
    
    N = int(input())
    a = input()
    
    # dict 만들기 {0: 0, 1: 0, ..., 9: 0}
    dict_a = {}
    for i in range(10):
        dict_a[i] = 0
    
    # for문으로 a 전체 돌면서 하나씩 빼오기
    for item in a:
        # dict에 맞는 거 +1하기
        dict_a[int(item)] = dict_a[int(item)] + 1
    
    # dict 중 가장 큰 수 result에 넣기
    for k, v in dict_a.items():
        if result_cnt <= v:
            result_n = k
            result_cnt = v
    
    print(f'#{test_case} {result_n} {result_cnt}')