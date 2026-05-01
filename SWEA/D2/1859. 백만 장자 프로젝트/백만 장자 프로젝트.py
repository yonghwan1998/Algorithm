T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    tc_price = list(map(int, input().split()))
    
    max_price = 0
    total_benefit = 0
    
    for price in reversed(tc_price):
        if(price > max_price):
            max_price = price
        else:
            total_benefit += max_price - price
            
    print(f"#{test_case} {total_benefit}")