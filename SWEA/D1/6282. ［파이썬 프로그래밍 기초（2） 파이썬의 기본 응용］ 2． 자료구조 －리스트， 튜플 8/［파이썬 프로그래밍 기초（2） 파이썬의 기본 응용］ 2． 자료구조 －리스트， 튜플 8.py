list_input = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]

is_even = lambda n: n % 2 == 0

answer = filter(is_even, list_input)

print(list(answer))