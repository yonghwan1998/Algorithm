T = int(input())

for test_case in range(1, T + 1):
    list_row = [[0 for _ in range(9)] for _ in range(9)]
    list_col = [[0 for _ in range(9)] for _ in range(9)]
    list_square = [[] for _ in range(9)]
    
    # list_row 할당
    for n in range(9):
        list_row[n] = list(map(int, input().split()))

    for i in range(9):
        for j in range(9):
            # list_col 할당
            list_col[j][i] = list_row[i][j]
            
            # list_square 할당
            square_index = (i // 3) * 3 + (j // 3) 
            list_square[square_index].append(list_row[i][j])
            
    answer = 1
    for number in range(9):
        if sorted(list_row[number]) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            answer = 0
        if sorted(list_col[number]) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            answer = 0
        if sorted(list_square[number]) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            answer = 0
            
    print(f"#{test_case} {answer}")