from collections import deque

def transelte(begin, target, words):
    visited = [0] * len(words)
    
    q = deque()
    q.append((begin, 0))
    
    while q:
        curr, cnt = q.popleft()
        
        if curr == target:
            return cnt
        
        for i in range(len(words)):
            if visited[i] == 1:
                continue
            
            word = words[i]
            
            cnt_diff = 0
            for j in range(len(word)):
                if curr[j] != word[j]:
                    cnt_diff += 1
                    
            if cnt_diff == 1:
                cnt += 1
                visited[i] = 1
                q.append((word, cnt))
            
    return 0

def solution(begin, target, words):
    return transelte(begin, target, words)