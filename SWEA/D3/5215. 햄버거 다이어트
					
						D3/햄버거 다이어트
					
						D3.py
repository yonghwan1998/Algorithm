T = int(input())

for test_case in range(1, 1 + T):
    N, L = map(int, input().split())

    answer = 0

    list_ingredients = list()

    for _ in range(N):
        list_ingredients.append(list(map(int, input().split())))

    def dfs(index, curr_score, curr_cal):
        global answer

        if curr_cal > L:
            return

        if index == N:
            answer = max(answer, curr_score)
            return

        # 재료를 고른 경우
        dfs(index + 1, curr_score + list_ingredients[index][0], curr_cal + list_ingredients[index][1])

        # 재료를 안 고른 경우
        dfs(index + 1, curr_score, curr_cal)

    dfs(0, 0, 0)

    print(f"#{test_case} {answer}")