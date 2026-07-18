list_n = [i for i in range(1, 11)]
is_even = lambda x: x % 2 ==0
iter_even = filter(is_even, list_n)
answer = list(map(lambda x: x ** 2, list(iter_even)))

print(answer)