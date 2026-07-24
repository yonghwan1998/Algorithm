T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    
    s = ''
    
    for _ in range(N):
        C, K = map(str, input().split())
        
        for _ in range(int(K)):
            s += C
            
    print(f"#{test_case}")
    for i in range(1, len(s) + 1):
        print(s[i - 1], end='')
        if i % 10 == 0 :
            print()
            
    print()