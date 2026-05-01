T = int(input())

for test_case in range(1, T + 1):
    amount = int(input())
    
    box = list()
    
    box.append(amount // 50_000)
    amount %= 50_000
    box.append(amount // 10_000)
    amount %= 10_000
    box.append(amount // 5_000)
    amount %= 5_000
    box.append(amount // 1_000)
    amount %= 1_000
    box.append(amount // 500)
    amount %= 500
    box.append(amount // 100)
    amount %= 100
    box.append(amount // 50)
    amount %= 50
    box.append(amount // 10)
    amount %= 10
    
    print(f"#{test_case}")
    for item in box:
        print(item, end=' ' )
        
    print(end='\n')