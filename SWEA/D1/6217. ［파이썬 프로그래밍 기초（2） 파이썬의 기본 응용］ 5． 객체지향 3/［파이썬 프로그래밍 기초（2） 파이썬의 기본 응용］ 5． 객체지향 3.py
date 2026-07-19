class Student:
    def __init__(self, name):
        self.name = name
    def printStudent(self):
        print(f'이름: {self.name}')
        
class GraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major
    def printStudent(self):
        print(f'이름: {self.name}, 전공: {self.major}')
        
s = Student('홍길동')
g = GraduateStudent('이순신', '컴퓨터')

s.printStudent()
g.printStudent()