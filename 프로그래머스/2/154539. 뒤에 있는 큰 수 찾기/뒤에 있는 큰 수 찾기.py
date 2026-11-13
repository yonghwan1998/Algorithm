def solution(numbers):
    length = len(numbers)
    answer = [-1] * length
    
    stack = []
    
    for i in range(length):
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]
        
        stack.append(i)
    
    return answer