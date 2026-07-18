def mul(*args):
    try:
        for item in args:
            if not isinstance(item, (int, float)):
                raise ValueError
    except ValueError:
        print('에러발생')
        return
    
    result = 1
    for num in args:
        result *= num
        
    return result

mul(1, 2, '4', 3)