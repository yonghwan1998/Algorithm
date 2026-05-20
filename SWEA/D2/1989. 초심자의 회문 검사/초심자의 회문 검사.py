T = int(input())

for test_case in range(1, 1 + T):
    answer = 0

    character = input()
    character_reversed = character[::-1]

    if character == character_reversed:
        answer = 1

    print(f"#{test_case} {answer}")