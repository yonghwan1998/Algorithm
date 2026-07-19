def new_max(*args):
    return max(args)

list_input = [3, 5, 4, 1, 8, 10, 2]
print(f"max(3, 5, 4, 1, 8, 10, 2) => {new_max(*list_input)}")