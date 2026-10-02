from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y, board):
    n = len(board)
    m = len(board[0])
    visited = [[0] * m for _ in range(n)]
    
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = 1
    
    while q:
        x, y, cnt = q.popleft()
        
        if board[x][y] == 'G':
            return cnt
        
        for i in range(4):
            nx = x
            ny = y
            
            while True:
                tx = nx + dx[i]
                ty = ny + dy[i]
            
                if not (0 <= tx < n and 0 <= ty < m):
                    break
            
                if board[tx][ty] == 'D':
                    break
                    
                nx = tx
                ny = ty
                
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny, cnt + 1))
        
    return -1

def solution(board):
    n, m = 0, 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                n, m = i, j
                break
    
    return search(n, m, board)