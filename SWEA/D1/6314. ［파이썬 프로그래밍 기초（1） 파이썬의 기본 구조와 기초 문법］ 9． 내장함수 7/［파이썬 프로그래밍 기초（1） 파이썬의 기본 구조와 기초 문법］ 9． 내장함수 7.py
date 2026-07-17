n_list = [i for i in range(1, 11)]
is_even = lambda n: n % 2 == 0
answer = filter(is_even, n_list)
print(list(answer))