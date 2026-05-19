T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    list_numbers = list(map(int, input().split()))

    answer = [0]

    def dfs(index, current_sum):

        if current_sum > K:
            return

        if index == N:
            if current_sum == K:
                answer[0] += 1
            return

        # 숫자를 넣는 경우
        dfs(index + 1, current_sum + list_numbers[index])

        # 숫자를 안 넣는 경우
        dfs(index + 1, current_sum)

    dfs(0, 0)

    print(f"#{test_case} {answer[0]}")