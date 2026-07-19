s = input()
answer = []

for c in s:
    answer.append(int(ord(c)) - 64)
    
print(*answer)