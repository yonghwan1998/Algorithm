list_answer = []

for i in range(2, 10):
    temp = []
    for j in range(1, 10):
        if (i * j % 3 != 0) and (i * j % 7 != 0):
            temp.append(i * j)
    list_answer.append(temp)
    
print(list_answer)