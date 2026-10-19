def solution(k, tangerine):
    answer = 0
    
    count = {}
    
    for t in tangerine:
        count[t] = count.get(t, 0) + 1
        
    sorted_count = sorted(count.values(), reverse=True)
    
    for cnt in sorted_count:
        k -= cnt
        answer += 1
        
        if k <= 0:
            break
        
    return answer