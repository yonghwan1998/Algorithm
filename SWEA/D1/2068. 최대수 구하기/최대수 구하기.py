T = int(input())

for test_case in range(1, 1 + T):
    list_n = list(map(int, input().split()))
    
    print(f"#{test_case} {max(list_n)}")