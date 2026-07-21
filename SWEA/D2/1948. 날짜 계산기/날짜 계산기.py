T = int(input())

month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

for test_case in range(1, 1 + T):
    month_1, day_1, month_2, day_2 = map(int, input().split())
    date_1, date_2 = 0, 0
    answer = 0
    
    for month in range(1, month_1):
        date_1 += month_dict[month]
    for month in range(1, month_2):
        date_2 += month_dict[month]
        
    answer = date_2 - date_1 + (day_2 - day_1 + 1)
    
    print(f"#{test_case} {answer}")