list_input = []

for _ in range(5):
    list_input.append(int(input()))
    
avg_input = sum(list_input) / len(list_input)

print(f"입력된 값 {list_input}의 평균은 {avg_input}입니다.")