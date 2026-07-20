T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    
    dict_str1 = {k: 0 for k in str1}
    
    for c in str2:
        if c in dict_str1.keys():
            dict_str1[c] = dict_str1.get(c) + 1
    
    answer = max(dict_str1.values())
    print(f"#{test_case} {answer}")