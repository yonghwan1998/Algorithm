class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
    def printArea(self):
        return self.width * self.heigth
    
r = Rectangle(4, 5)

print(f"사각형의 면적: {r.printArea()}")