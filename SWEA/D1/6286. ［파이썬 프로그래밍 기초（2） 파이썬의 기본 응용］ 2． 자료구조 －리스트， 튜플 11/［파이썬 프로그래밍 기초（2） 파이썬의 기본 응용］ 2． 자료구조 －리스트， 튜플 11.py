answer = [1, 1]

[answer.append(answer[i] + answer[i + 1]) for i in range(8)]
    
print(answer)