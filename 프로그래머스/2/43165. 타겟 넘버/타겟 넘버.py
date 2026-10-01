answer = 0

def search(index, total, numbers, target):
    global answer
    
    # 종료 조건
    if index == len(numbers):
        if total == target:
            answer += 1
        
        return
    
    # 더하는 경우
    search(index + 1, total + numbers[index], numbers, target)
    
    # 빼는 경우
    search(index + 1, total - numbers[index], numbers, target)

def solution(numbers, target):
    search(0, 0, numbers, target)
    return answer