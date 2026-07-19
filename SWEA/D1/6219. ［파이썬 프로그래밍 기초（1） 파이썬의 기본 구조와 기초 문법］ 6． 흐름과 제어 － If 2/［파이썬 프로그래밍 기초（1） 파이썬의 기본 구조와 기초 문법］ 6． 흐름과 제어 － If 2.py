n = int(input())
cnt = 0

for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
        print(f"{i}(은)는 {n}의 약수입니다.")
        
if cnt == 2:
    print(f"{n}(은)는 1과 {n}로만 나눌 수 있는 소수입니다.")