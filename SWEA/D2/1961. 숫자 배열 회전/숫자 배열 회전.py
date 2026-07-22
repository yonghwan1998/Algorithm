T = int(input())

def rotate_board(board, N):
    rotated_board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated_board[j][N - 1 - i] = board[i][j]
            
    return rotated_board

for test_case in range(1, T + 1):
    N = int(input())
    
    board = []
    
    for _ in range(N):
        board.append(list(map(int, input().split())))

    rotated_board_90 = rotate_board(board, N)
    rotated_board_180 = rotate_board(rotated_board_90, N)
    rotated_board_270 = rotate_board(rotated_board_180, N)
    
    print(f"#{test_case}")
    
    for i in range(N):
        for j in range(N):
            print(rotated_board_90[i][j], end='')
        print('', end=' ')
        for j in range(N):
            print(rotated_board_180[i][j], end='')
        print('', end=' ')
        for j in range(N):
            print(rotated_board_270[i][j], end='')
        print()