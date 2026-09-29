def solution(numbers):
    answer = ''
    
    str_numbers = []
    temp = []
    
    for number in numbers:
        str_numbers.append(str(number) * 3)

    str_numbers.sort(reverse=True)
    
    for number in str_numbers:
        temp.append(number[0:len(number) // 3])
    
    answer = "".join(temp)
    
    if answer[0] == '0':
        return '0'
    
    return answer