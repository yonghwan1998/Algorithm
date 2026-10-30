def solution(elements):
    answer = 0
    
    length = len(elements)
    answer_set = set()
    
    for i in range(length):
        sum = 0
        for j in range(length):
            sum += elements[(i + j) % length]
            answer_set.add(sum)
        
    answer = len(answer_set)    
    
    return answer