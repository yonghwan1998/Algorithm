def square(n):
    return n ** 2

list_input = list(map(int, input().split(', ')))

for n in list_input:
    print(f"square({n}) => {square(n)}")