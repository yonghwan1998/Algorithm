class Shape:
    def __init__(self, length):
        self.length = length
    def area(self):
        return 0
        
class Square(Shape):
    def area(self):
        return self.length * self.length
    
s = Square(3)

print(f"정사각형의 면적: {s.area()}")