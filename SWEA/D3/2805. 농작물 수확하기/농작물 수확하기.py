T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    center = (N+1) / 2
    answer = 0

    for i in range(1, N+1):
        crops = [int(x) for x in input()]

        temp = abs(center - i) # center 로부터 얼마나 떨어져있는가?

        start = int(temp)
        end = int(N - temp)

        answer += sum(crops[start:end])

    print(f"#{test_case} {answer}")