T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    a = input()
    
    list_cnt = [0 for _ in range(10)]
    
    for index in a:
        list_cnt[int(index)] += 1

    max_cnt = 0
    max_index = 0
    for i in range(10):
        if list_cnt[i] >= max_cnt:
            max_cnt = list_cnt[i]
            max_index = i
            
    print(f"#{test_case} {max_index} {max_cnt}")