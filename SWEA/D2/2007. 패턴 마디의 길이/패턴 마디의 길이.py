T = int(input())

for test_case in range(1, T + 1):
    s = input()
    
    for length in range(1, 11):
        if s[:length] == s[length:length*2]:
            print(f"#{test_case} {length}")
            break