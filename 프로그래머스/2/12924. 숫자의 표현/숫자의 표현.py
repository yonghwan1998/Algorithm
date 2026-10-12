def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        temp = 0
        
        while temp < n:
            temp += i
            
            if temp == n:
                answer += 1
                
            i += 1
    
    return answer