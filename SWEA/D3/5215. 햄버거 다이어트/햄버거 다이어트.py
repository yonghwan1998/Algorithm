T = int(input())

for test_case in range(1, 1 + T):
    N, L = map(int, input().split())
    list_ingredients = list()

    for _ in range(N):
        list_ingredients.append(list(map(int, input().split())))

    answer = [0]

    def dfs(index, current_score, current_cal):

        if current_cal > L:
            return

        if index == N:
            answer[0] = max(answer[0], current_score)
            return

        # 재료를 고른 경우
        dfs(index + 1, current_score + list_ingredients[index][0], current_cal + list_ingredients[index][1])

        # 재료를 안 고른 경우
        dfs(index + 1, current_score, current_cal)

    dfs(0, 0, 0)

    print(f"#{test_case} {answer[0]}")