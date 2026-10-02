from collections import deque

cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move_to_L(start_x, start_y, maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0] * m for _ in range(n)]
    
    q = deque()
    q.append((start_x, start_y, 0))
    visited[start_x][start_y] = 1
    
    while q:
        x, y, cnt = q.popleft()
        
        if maps[x][y] == 'L':
            return move_to_E(x, y, maps, cnt)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < n and 0 <= ny < m):
                continue
                
            if visited[nx][ny] == 1:
                continue
                
            if maps[nx][ny] != 'X':
                visited[nx][ny] = 1
                q.append((nx, ny, cnt + 1))
                
    return -1
        
def move_to_E(start_x, start_y, maps, cnt):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0] * m for _ in range(n)]
    
    q = deque()
    q.append((start_x, start_y, cnt))
    visited[start_x][start_y] = 1
    
    while q:
        x, y, cnt = q.popleft()
        
        if maps[x][y] == 'E':
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < n and 0 <= ny < m):
                continue
                
            if visited[nx][ny] == 1:
                continue
                
            if maps[nx][ny] != 'X':
                visited[nx][ny] = 1
                q.append((nx, ny, cnt + 1))
    
    return -1

def solution(maps):
    answer = 0
    
    board = []
    
    for map in maps:
        temp = []
        for s in map:
            temp.append(s)
        board.append(temp)

    n, m = 0, 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                n = i
                m = j
                break
        
    answer = move_to_L(n, m, maps)
    
    return answer