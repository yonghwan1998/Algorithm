row, column = map(int, input().split(', '))
answer = []

for i in range(row):
    temp = []
    for j in range(column):
        temp.append(i * j)
    answer.append(temp)
    
print(answer)