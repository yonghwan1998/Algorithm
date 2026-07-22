T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    answer = 0
    
    board = [[0 for _ in range(10)] for _ in range(10)]
    
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        if color == 1:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if board[i][j] == 0:
                        board[i][j] = 1
                    elif board[i][j] == 2:
                        board[i][j] = 3
        elif color == 2:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if board[i][j] == 0:
                        board[i][j] = 2
                    elif board[i][j] == 1:
                        board[i][j] = 3
    
    for i in range(10):
        for j in range(10):
            if board[i][j] == 3:
                answer += 1
    
    print(f"#{test_case} {answer}")