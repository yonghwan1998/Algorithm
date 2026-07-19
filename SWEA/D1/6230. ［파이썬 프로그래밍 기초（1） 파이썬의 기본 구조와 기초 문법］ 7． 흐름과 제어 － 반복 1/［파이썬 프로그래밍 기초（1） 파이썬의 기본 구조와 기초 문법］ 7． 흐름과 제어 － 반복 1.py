input_list = [88, 30, 61, 55, 95]
cnt = 1

for item in input_list:
    if item >= 60:
        print(f"{cnt}번 학생은 {item}점으로 합격입니다.")
    elif item < 60:
        print(f"{cnt}번 학생은 {item}점으로 불합격입니다.")
    cnt += 1