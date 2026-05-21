for test_case in range(1, 11):
    TC = int(input())
    search = input()
    target = input()

    answer = target.count(search)

    print(f"#{test_case} {answer}")