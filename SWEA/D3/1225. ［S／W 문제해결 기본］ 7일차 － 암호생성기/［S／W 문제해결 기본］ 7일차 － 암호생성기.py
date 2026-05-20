for test_case in range(1, 11):
    tc = int(input())
    list_number = list(map(int, input().split()))

    count = 0
    number_pop = 1

    while number_pop != 0:
        count = count % 5 + 1
        number_pop = list_number.pop(0) - count

        if number_pop <= 0:
            number_pop = 0

        list_number.append(number_pop)

    print(f"#{tc}", end=' ')
    print(*list_number)
