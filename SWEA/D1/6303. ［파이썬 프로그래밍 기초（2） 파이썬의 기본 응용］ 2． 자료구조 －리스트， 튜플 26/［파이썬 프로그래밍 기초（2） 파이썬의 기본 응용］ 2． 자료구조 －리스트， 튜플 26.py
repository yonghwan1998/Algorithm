list_a = [1,3,6,78,35,55]
list_b = [12,24,35,24,88,120,155]
answer = []

for i in list_a:
    for j in list_b:
        if i == j:
            answer.append(j)

print(answer)