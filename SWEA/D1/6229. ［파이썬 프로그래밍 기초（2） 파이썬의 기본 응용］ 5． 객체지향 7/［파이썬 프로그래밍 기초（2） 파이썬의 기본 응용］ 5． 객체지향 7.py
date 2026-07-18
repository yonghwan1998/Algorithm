class Person:
    def getGender(self):
        return self.gender
    
class Male(Person):
    def __init__(self):
        self.gender = "Male"

class Female(Person):
    def __init__(self):
        self.gender = "Female"
        
m = Male()
f = Female()

print(m.getGender())
print(f.getGender())