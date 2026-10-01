from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0] * m for _ in range(n)]
    
    x, y = 0, 0
    
    visited[x][y] = 1
    
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return visited[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if visited[nx][ny] != 0:
                continue

            if maps[nx][ny] == 0:
                continue

            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
        
    return -1

def solution(maps):
    return search(maps)