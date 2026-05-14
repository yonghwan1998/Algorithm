T = int(input())

for test_case in range(1, T+1):

    tc_bit = list(input())
    answer = 0

    prev_bit = '0'
    curr_bit = '0'

    for bit in tc_bit:

        curr_bit = bit

        if prev_bit != curr_bit:
            answer += 1
            prev_bit = curr_bit

    print(f"#{test_case} {answer}")