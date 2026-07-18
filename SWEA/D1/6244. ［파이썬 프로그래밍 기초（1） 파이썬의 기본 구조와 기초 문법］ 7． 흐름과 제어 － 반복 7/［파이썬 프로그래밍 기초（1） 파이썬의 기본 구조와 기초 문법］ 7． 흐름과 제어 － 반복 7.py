list_input = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
answer = 0

while list_input:
    temp = list_input.pop()
    if temp >= 80:
        answer += temp
    
print(answer)