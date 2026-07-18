s = input()

for i in range(len(s)):
    if i % 2 == 0:
        print(s[i:i+1], end='')