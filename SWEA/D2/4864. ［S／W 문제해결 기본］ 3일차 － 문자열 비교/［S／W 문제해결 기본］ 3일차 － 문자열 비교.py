T = int(input())

for test_case in range(1, 1 + T):
    str1 = input()
    str2 = input()
    
    answer = 0
    
    for i in range(len(str2) - len(str1) + 1):
        if str1 == str2[i:i + len(str1)]:
            answer = 1
            break
            
    print(f"#{test_case} {answer}")