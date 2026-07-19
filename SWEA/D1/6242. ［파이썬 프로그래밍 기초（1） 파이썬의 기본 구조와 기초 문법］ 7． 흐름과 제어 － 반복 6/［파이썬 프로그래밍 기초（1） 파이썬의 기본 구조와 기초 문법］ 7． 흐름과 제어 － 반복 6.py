input_list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
answer = {}

for c in input_list:
    if c not in answer:
        answer[c] = 1
    else:
        answer[c] += 1

print(answer)