class Circle:
    def __init__(self, r):
        self.r = r
    def printArea(self):
        return 3.14 * self.r * self.r
    
c = Circle(2)

print(f"원의 면적: {c.printArea()}")