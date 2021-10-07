class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, height: {self.height}"
    
    def getOlder(self, years):
        self.age += years

class Worker(Person):

    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def calc_yearly_salary(self):
        return f"${self.salary * 12}"
    
    def __str__(self):
        text = super(Worker, self).__str__()
        text += f", salary: {self.salary}"
        return text


person1 = Person('jesus', 23, 1.76)
print(person1)

worker1 = Worker('jesus', 23, 1.76, 8000)
print(worker1)
print(worker1.calc_yearly_salary())
# ======================================
print("Vectors")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"

p1 = Point(2,5)
p2 = Point(1,6)

print(p1)
print(p2)
p3 = p1 + p2
p4 = p1 - p2
print(p3)
print(p4)


