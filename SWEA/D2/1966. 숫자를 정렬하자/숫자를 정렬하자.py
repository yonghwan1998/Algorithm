T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    tc_list = list(map(int, input().split()))
    
    tc_list.sort()
    
    print(f"#{test_case}", end=' ')
    
    for n in range(N):
        print(f"{tc_list[n]}", end= ' ')
    print("\n", end='')