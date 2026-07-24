T = int(input())

for test_case in range(1, 1 + T):
    N, N_16 = map(str, input().split())
    
    answer = ''
    
    for c in N_16:
        answer += bin(int(c, 16))[2:].zfill(4)
        
    print(f"#{test_case} {answer}")