n = int(input())
answer = ""

while True:
    answer += str(n % 2)
    n = n // 2
    if n == 0:
        break

print(answer)