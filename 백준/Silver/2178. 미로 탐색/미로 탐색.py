from collections import deque

answer = 0

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

q = deque()
q.append([0, 0, 1])
visited[0][0] = True

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

while q:
    x, y, cnt = q.popleft()

    if x == N - 1 and y == M - 1:
        answer = cnt
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if board[nx][ny] == '0':
            continue

        if visited[nx][ny]:
            continue

        q.append([nx, ny, cnt + 1])
        visited[nx][ny] = True

print(answer)