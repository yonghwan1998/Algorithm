T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    answer = [0, 0, 0, 0, 0]
    
    while n % 11 == 0:
        answer[4] += 1
        n /= 11
        
    while n % 7 == 0:
        answer[3] += 1
        n /= 7
        
    while n % 5 == 0:
        answer[2] += 1
        n /= 5
        
    while n % 3 == 0:
        answer[1] += 1
        n /= 3
        
    while n % 2 == 0:
        answer[0] += 1
        n /= 2
        
    print(f"#{test_case}", end=' ')
    print(*answer)