T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    
    board = [[0 for _ in range(N)] for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    d = 0
    
    x = 0
    y = 0
    
    board[x][y] = 1
    
    for i in range(2, N ** 2 + 1):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] != 0:
            d = (d + 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
        
        x = nx
        y = ny
        
        board[x][y] = i
    
    print(f"#{test_case}")
    for row in board:
        print(*row)