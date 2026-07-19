answer = []

for i in range(100, 301):
    cnt_temp = 0
    for c in str(i):
        if int(c) % 2 == 0:
            cnt_temp += 1
            
    if cnt_temp == 3:
        answer.append(i)
        
print(*answer, sep=',')