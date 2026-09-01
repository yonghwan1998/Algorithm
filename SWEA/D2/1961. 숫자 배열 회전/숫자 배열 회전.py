T = int(input())

def rotate_matrix(N, matrix):
    matrix_new = [[0 for _ in range(N)] for _ in range(N)]

    for row in range(N):
        for col in range(N):
            matrix_new[col][N - row - 1] = matrix[row][col]
    return matrix_new

for test_case in range(1, T + 1):
    
    N = int(input())
    matrix = []
    
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
        
    matrix_90 = rotate_matrix(N, matrix)
    matrix_180 = rotate_matrix(N, matrix_90)
    matrix_270 = rotate_matrix(N, matrix_180)
    
    print(f'#{test_case}')
    for i in range(N):
        print(*matrix_90[i], sep='', end=' ')
        print(*matrix_180[i], sep='', end=' ')
        print(*matrix_270[i], sep='')