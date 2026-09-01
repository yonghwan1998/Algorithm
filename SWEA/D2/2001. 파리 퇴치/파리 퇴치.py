T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = []
    cnt_fly = []
    
    for i in range(N):
        board.append(list(map(int, input().split())))
        
    # for문, N - M + 1만큼 반복
    for row in range(N - M + 1):
        for col in range(N - M + 1):
            # board[row][col] 위치에서 이중 for문, M만큼 반복
            temp = 0
            for i in range(M):
                for j in range(M):
                    temp += board[row + i][col + j]
            cnt_fly.append(temp)
    
    result = max(cnt_fly)
    
    print(f'#{test_case} {result}')
