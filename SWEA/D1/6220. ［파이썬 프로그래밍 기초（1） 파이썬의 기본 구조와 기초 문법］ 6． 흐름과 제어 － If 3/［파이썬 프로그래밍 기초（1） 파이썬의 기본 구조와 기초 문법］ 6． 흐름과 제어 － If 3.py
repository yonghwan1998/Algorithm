T = int(input())

for test_case in range(1, T + 1):
    c = input()
    judge = ""
    
    if c.isupper():
        judge = "대문자"
    else:
        judge = "소문자"
    print(f"#{test_case} {c} 는 {judge} 입니다.")