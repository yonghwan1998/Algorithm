T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    board = []
    result = 0
    
    for _ in range(N):
        board.append(list(map(int, input().split())))
        
    for row in range(N):
        cnt = 0
        
        for col in range(N):
            if board[row][col] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        
        if cnt == K:
            result += 1
                
    for col in range(N):
        cnt = 0
        
        for row in range(N):
            if board[row][col] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        
        if cnt == K:
            result += 1
        
    print(f'#{test_case} {result}')