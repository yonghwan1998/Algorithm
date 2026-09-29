answer = -1

def search(k, count, dungeons, visited):
    global answer
    
    answer = max(answer, count)
    
    for i in range(len(dungeons)):
        need, use = dungeons[i]
        
        if visited[i] == 0 and k >= need:
            visited[i] = 1
            
            search(k - use, count + 1, dungeons, visited)
            
            visited[i] = 0

def solution(k, dungeons):
    
    visited = [0] * len(dungeons)
    
    search(k, 0, dungeons, visited)
    
    return answer