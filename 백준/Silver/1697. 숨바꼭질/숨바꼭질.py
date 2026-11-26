from collections import deque

def move(N, K):
    q = deque()
    q.append([N, 0])

    visited = [False] * 100001
    visited[N] = True

    while q:
        n, cnt = q.popleft()

        if n == K:
            return cnt

        for next_n in [n - 1, n + 1, n * 2]:
            if not (0 <= next_n <= 100000):
                continue

            if visited[next_n]:
                continue

            q.append([next_n, cnt + 1])
            visited[n] = True

N, K = map(int, input().split())

answer = move(N, K)

print(answer)