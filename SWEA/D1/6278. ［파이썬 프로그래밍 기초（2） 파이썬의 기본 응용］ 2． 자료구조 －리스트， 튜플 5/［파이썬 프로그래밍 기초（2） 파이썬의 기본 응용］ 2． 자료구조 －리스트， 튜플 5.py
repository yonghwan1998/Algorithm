ord_list = [1, 1, 3, 3, 4, 6, 8, 8, 9, 10]
n = int(input())

new_list = [i for i in ord_list if i < 8]
print(f"new_list: {new_list}")