def pick(index, score, cal):
    global answer

    if cal > L:
        return

    if index == N:
        answer = max(answer, score)
        return

    pick(index + 1, score + arr[index][0], cal + arr[index][1])

    pick(index + 1, score, cal)

T = int(input())

for test_case in range(1, T + 1):
    answer = 0

    N, L = map(int, input().split())
    arr = []

    for _ in range(N):
        arr.append(list(map(int, input().split())))

    pick(0, 0, 0)

    print(f'#{test_case} {answer}')