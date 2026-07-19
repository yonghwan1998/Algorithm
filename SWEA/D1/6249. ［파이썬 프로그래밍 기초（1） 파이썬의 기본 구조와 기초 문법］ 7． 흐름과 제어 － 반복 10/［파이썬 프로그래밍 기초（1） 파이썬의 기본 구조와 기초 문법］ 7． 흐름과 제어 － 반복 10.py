s = input()
answer = [0 * i for i in range(10)]

for c in s:
    n = int(c)
    
    answer[n] += 1
    
sample = [i for i in range(10)]
print(*sample, sep=' ')
print(*answer, sep=' ')