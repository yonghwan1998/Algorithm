T = int(input())

N_list = list()

for test_case in range(1, T + 1):
    N_list.append(test_case)
    
for n in N_list:
    cnt_369 = 0
    n_str = str(n)
    
    for i in range(len(n_str)):
        if n_str[i:i+1] == '3' or n_str[i:i+1] == '6' or n_str[i:i+1] == '9':
            cnt_369 += 1
    
    if cnt_369 == 0:
        print(f"{n_str}", end=' ')
    else:
        for _ in range(cnt_369):
            print(f"-", end='')
        print("", end=' ')