T = int(input())

for test_case in range(1 , 1 + T):
    N, M = map(int, input().split())
    
    board = [list(map(str, input())) for _ in range(N)]
    board_col = [[row[i] for row in board] for i in range(N)]
    
    answer = ''
    
    for i in range(N):
        for j in range(N - M + 1):
            if M % 2 == 0:
                list_1 = board[i][j:j + M // 2]
                str_1 = ''.join(list_1)
                list_2 = board[i][j + M // 2:j + M]
                str_2 = ''.join(list_2)
                reversed_str_2 = str_2[::-1]
                
                if str_1 == reversed_str_2:
                    answer = str_1 + str_2
                    break
                    
                list_3 = board_col[i][j:j + M // 2]
                str_3 = ''.join(list_3)
                list_4 = board_col[i][j + M // 2:j + M]
                str_4 = ''.join(list_4)
                reversed_str_4 = str_4[::-1]
                
                if str_3 == reversed_str_4:
                    answer = str_3 + str_4
                    break
                    
            else:
                list_1 = board[i][j:j + M // 2 + 1]
                str_1 = ''.join(list_1)
                list_2 = board[i][j + M // 2:j + M]
                str_2 = ''.join(list_2)
                reversed_str_2 = str_2[::-1]
                if str_1 == reversed_str_2:
                    answer = str_1 + str_2[1:]
                    break
                    
                list_3 = board_col[i][j:j + M // 2 + 1]
                str_3 = ''.join(list_3)
                list_4 = board_col[i][j + M // 2:j + M]
                str_4 = ''.join(list_4)
                reversed_str_4 = str_4[::-1]
                if str_3 == reversed_str_4:
                    answer = str_3 + str_4[1:]
                    break
    
    print(f"#{test_case} {answer}")