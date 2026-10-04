def search(index, sum):
    global answer

    if index == N:
        if sum == K:
            answer += 1
        return

    if sum > K:
        return

    search(index + 1, sum + A_arr[index])

    search(index + 1, sum)

T = int(input())

for test_case in range(1, T + 1):
    answer = 0

    N, K = map(int, input().split())
    A_arr = list(map(int, input().split()))

    search(0, 0)

    print(f'#{test_case} {answer}')