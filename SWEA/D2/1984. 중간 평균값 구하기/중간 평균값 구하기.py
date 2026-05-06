T = int(input())

for test_case in range(1, T + 1):
    tc_list = list(map(int, input().split()))
    tc_list.sort()
    
    list_length = len(tc_list)
    
    tc_list.pop(list_length - 1)
    tc_list.pop(0)
    
    list_sum = sum(tc_list)
    
    answer = round(list_sum / (list_length - 2))
    
    print(f"#{test_case} {answer}")