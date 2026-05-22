T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())

    answer = 0

    cnt = 0

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if ((i ** 2) + (j ** 2)) <= N ** 2:
                cnt += 1

    answer = 1 + (N * 4) + (cnt * 4) # 중앙 + (절편 내부 개수 * 4) + (축 위의 개수 * 4)

    print(f"#{test_case} {answer}")