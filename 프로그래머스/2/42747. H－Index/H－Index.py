def solution(citations):
    answer = 0
    
    n = len(citations)
    
    citations.sort(reverse=True)
    
    for i in range(max(citations), 0, -1):
        h = i
        h_over = 0
        
        for citation in citations:
            if citation >= h:
                h_over += 1
            else:
                break
        h_under = n = h_over
        
        if h_over >= h:
            answer = h
            break
    
    return answer