T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    list_seq = list(map(int, input().split()))

    dp = [1] * N

    for i in range(N):
        for j in range(i):
            if list_seq[j] <= list_seq[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(f"#{test_case} {max(dp)}")