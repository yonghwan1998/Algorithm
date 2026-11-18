from collections import deque

def solution(x, y, n):
    answer = -1
    
    def cal(x, y, n, cnt):
        nonlocal answer
        
        q = deque()
        q.append([x, cnt])
        
        visited = [False] * (y + 1)
        visited[x] = True
        
        while q:
            x, cnt = q.popleft()
            
            if x == y:
                answer = cnt
                return
            
            for nx in (x + n, x * 2, x * 3):
                if nx > y:
                    continue
                
                if visited[nx]:
                    continue
                    
                q.append([nx, cnt + 1])
                visited[nx] = True
            
    cal(x, y, n, 0)
    
    return answer