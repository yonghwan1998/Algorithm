T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    
    list_a = list(map(int, input().split()))
    
    max_a = max(list_a)
    min_a = min(list_a)
    
    print(f"#{test_case} {max_a - min_a}")