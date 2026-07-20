T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    list_input = list(map(int, input().split()))
    
    cnt = M % N
    
    print(f"#{test_case} {list_input[cnt]}")