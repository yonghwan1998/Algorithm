def is_exist(l, n):
    if n in l:
        return True
    else:
        return False

target_list = [2, 4, 6, 8, 10]
input_list = [5, 10]

print(target_list)
for item in input_list:
    print(f"{item} => {is_exist(target_list, item)}")