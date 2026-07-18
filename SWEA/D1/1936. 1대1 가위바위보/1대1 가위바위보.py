A, B = map(int, input().split())

# 가위 1, 바위 2, 보 3

if A == 1:
    if B == 2:
        print("B")
    else:
        print("A")
if A == 2:
    if B == 1:
        print("A")
    else:
        print("B")
if A == 3:
    if B == 2:
        print("A")
    else:
        print("B")