input_list = [(90, 80), (85, 75), (90, 100)]
cnt = 1

for item in input_list:
    print(f"{cnt}번 학생의 총점은 {sum(item)}점이고, 평균은 {sum(item) / 2:.1f}입니다.")
    cnt += 1