class Student:
    def __init__(self, korea, english, math):
        self.korea = korea
        self.english = english
        self.math = math
    def returnSum(self):
        return self.korea + self.english + self.math
    
k, e, m = map(int, input().split(', '))
    
s = Student(k, e, m)

print(f'국어, 영어, 수학의 총점: {s.returnSum()}')