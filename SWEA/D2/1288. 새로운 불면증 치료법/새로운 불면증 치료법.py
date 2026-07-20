T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    set_N = set()
    
    k = 1
    
    while True:
        temp = k * N
        
        for c in str(temp):
            set_N.add(c)
            
        if len(set_N) == 10:
            break
            
        k += 1
            
    print(f"#{test_case} {temp}")