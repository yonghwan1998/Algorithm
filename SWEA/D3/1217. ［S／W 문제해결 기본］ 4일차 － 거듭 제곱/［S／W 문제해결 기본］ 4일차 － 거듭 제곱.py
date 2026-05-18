def temp(number, i):
    if i > 1:
        i -= 1
        return number * temp(number, i)
    else:
        return number

for test_case in range(1, 11):
    tc = int(input())

    N, M = map(int, input().split())

    answer = temp(N, M)

    print(f"#{tc} {answer}")