T = int(input())

for test_case in range(1, 1 + T):
    s = input()
    
    storage = []
    
    answer = 1
    
    for c in s:
        if c == '{' or c == '(':
            storage.append(c)
        elif c == ')':
            if not storage:
                answer = 0
                break
            storage_pop = storage.pop()
            if storage_pop != '(':
                answer = 0
                break
        elif c == '}':
            if not storage:
                answer = 0
                break
            storage_pop = storage.pop()
            if storage_pop != '{':
                answer = 0
                break
    if storage:
        answer = 0
                
    print(f"#{test_case} {answer}")