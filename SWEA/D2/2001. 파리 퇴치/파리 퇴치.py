T = int(input())

for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    answer = 0
    
    board = [list(map(int, input().split())) for _ in range(N)]
    
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp = 0
            for k in range(M):
                for l in range(M):
                    temp += board[i + k][j + l]
            answer = max(answer, temp)
    
    print(f"#{test_case} {answer}")