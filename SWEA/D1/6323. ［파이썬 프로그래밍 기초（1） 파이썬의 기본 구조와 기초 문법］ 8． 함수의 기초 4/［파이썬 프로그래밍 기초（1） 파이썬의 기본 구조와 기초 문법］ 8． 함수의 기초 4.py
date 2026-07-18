n = int(input())

answer = [1, 1]

for i in range(n - 2):
    answer.append(answer[i] + answer[i+1])
    
print(answer)