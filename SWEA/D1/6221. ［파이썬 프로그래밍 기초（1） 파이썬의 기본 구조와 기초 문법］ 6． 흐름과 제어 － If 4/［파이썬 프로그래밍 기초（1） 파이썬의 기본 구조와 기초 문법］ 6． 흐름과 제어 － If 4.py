man = {}
man['Man1'] = input()
man['Man2'] = input()

if man['Man1'] == '가위':
    if man['Man2'] == '가위':
        print(f"Result : Draw")
    elif man['Man2'] == '바위':
        print(f"Result : Man2 Win!")
    elif man['Man2'] == '보':
        print(f"Result : Man1 Win!")
elif man['Man1'] == '바위':
    if man['Man2'] == '가위':
        print(f"Result : Man1 Win!")
    elif man['Man2'] == '바위':
        print(f"Result : Draw")
    elif man['Man2'] == '보':
        print(f"Result : Man2 Win!")
elif man['Man1'] == '보':
    if man['Man2'] == '가위':
        print(f"Result : Man2 Win!")
    elif man['Man2'] == '바위':
        print(f"Result : Man1 Win!")
    elif man['Man2'] == '보':
        print(f"Result : Draw")