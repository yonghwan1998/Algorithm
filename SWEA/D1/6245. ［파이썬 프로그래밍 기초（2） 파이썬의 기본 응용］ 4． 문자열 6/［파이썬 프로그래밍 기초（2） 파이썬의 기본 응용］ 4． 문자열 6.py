balance = 0

for _ in range(3):
    m, a = input().split()
        
    if m == 'D':
        balance += int(a)
    if m == 'W':
        balance -= int(a)
        
print(f"잔액: {balance}")