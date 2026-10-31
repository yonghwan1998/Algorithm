def solution(n, words):
    answer = [0, 0]
    
    length = len(words)
    used = {}
    
    for i in range(length):
        
        if used.get(words[i], False) == True:
            answer[0] = i % n + 1
            answer[1] = i // n + 1
            break
            
        if i == length - 1:
            break
            
        if words[i % length][-1] != words[(i + 1) % length][0]:
            answer[0] = (i + 1) % n + 1
            answer[1] = (i + 1) // n + 1
            break
        
        used[words[i]] = True
        
    return answer