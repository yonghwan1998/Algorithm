T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    v = 0
    distance = 0
    
    for _ in range(N):
        line = input()

        if line == '0':
            # 현재 속도 유지
            distance += v
        else:
            command, a = map(int, line.split())
            if command == 1:
                # 가속
                v += a
                distance += v
            elif command == 2:
                # 감속
                if v < a:
                    v = 0
                else:
                    v -= a
                    distance += v
    print(f"#{test_case} {distance}")