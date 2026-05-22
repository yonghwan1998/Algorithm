for _ in range(1, 11):
    TC = int(input())

    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    list_sum = list()

    # row
    for number in arr:
        list_sum.append(sum(number))

    # col
    for i in range(N):
        sum_col = 0
        for j in range(N):
            sum_col += arr[j][i]

        list_sum.append(sum_col)

    # dia_p (positive)
    sum_dia_p = 0
    for i in range(N):
        sum_dia_p += arr[i][i]
    list_sum.append(sum_dia_p)

    # dia_n (negative)
    sum_dia_n = 0
    for i in range(N):
        sum_dia_n += arr[i][N - i - 1]
    list_sum.append(sum_dia_n)

    print(f"#{TC} {max(list_sum)}")