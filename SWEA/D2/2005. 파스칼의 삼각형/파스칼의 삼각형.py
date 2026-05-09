T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    print(f"#{test_case}")
    
    list_prev = [1]
    list_curr = list()
   
    for n in range(1, N+1):
        for i in range(n):
            if i == 0 or i == n-1:
                list_curr.append(1)
            else:
                list_curr.append(sum(list_prev[i-1:i+1]))
            
        list_prev = list_curr
        
        for number in list_curr:
            print(f"{number}", end=' ')
            
        list_curr = list()
        print()