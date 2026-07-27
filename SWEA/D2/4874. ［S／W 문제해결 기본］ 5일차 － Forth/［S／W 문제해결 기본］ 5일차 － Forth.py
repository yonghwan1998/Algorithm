T = int(input())

for test_case in range(1, 1 + T):
    stack = []
    forth = ['+', '-', '*', '/']
    answer = 0
    
    list_input = list(map(str, input().split()))
    
    for c in list_input:
        if c in forth:
            if len(stack) < 2:
                answer = 'error'
                break
                
            str_2 = stack.pop()
            str_1 = stack.pop()
            if c == forth[0]:
                stack.append(int(str_1) + int(str_2))
            elif c == forth[1]:
                stack.append(int(str_1) - int(str_2))
            elif c == forth[2]:
                stack.append(int(str_1) * int(str_2))
            elif c == forth[3]:
                stack.append(int(str_1) / int(str_2))
            else:
                answer = 'error'
                break
        elif c == '.':
            if len(stack) == 1:
                answer = int(stack.pop())
            else:
                answer = 'error'
                break
        else:
            stack.append(c)
            
    print(f"#{test_case} {answer}")