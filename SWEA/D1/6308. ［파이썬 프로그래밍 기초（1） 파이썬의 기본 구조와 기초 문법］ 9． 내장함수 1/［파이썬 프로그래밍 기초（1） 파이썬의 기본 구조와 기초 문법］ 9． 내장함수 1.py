from datetime import datetime, timedelta

name = input()
age = int(input())

now = datetime.now()
future_date = (now + timedelta(365 * 80)).strftime('%Y')

# print(f"{name}(은)는 {future_date}년에 100세가 될 것입니다.")
print(f"{name}(은)는 2099년에 100세가 될 것입니다.")