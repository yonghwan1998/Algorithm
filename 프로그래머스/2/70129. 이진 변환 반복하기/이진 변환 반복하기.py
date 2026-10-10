def solution(s):
    answer = [0, 0]
    
    while s != "1":
        len_s = len(s)
        
        s = s.replace("0", "")
        len_remove = len(s)
        answer[1] += len_s - len_remove
        
        s = bin(int(len_remove))[2:]
        
        answer[0] += 1
        
    return answer