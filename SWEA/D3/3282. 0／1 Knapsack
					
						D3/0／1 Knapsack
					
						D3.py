T = int(input())

for test_case in range(1, 1 + T):
    N, K = map(int, input().split())

    dp = [0] * (K + 1)

    for _ in range(N):
        V, C = map(int, input().split())

        for volume in range(K, V - 1, -1):
            dp[volume] = max(dp[volume], dp[volume - V] + C)

    print(f"#{test_case} {dp[K]}")