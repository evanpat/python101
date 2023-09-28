class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def description(self):
        print("I'm a Person:", self.first_name, self.last_name)
    
# Inheritance - Student inherits from Person
class Student(Person):
    def __init__(self, first_name, last_name, grade):
        super().__init__(first_name, last_name) 
        self.grade = grade

# to comment: Ctrl-K Ctrl-C
    def description(self):
        print(f"I'm a Student:{self.first_name} {self.last_name}, Grade:{self.grade}")

p = Person("Patrick", "Lai")
s = Student("Alex", "Wong", "F.2")

print(type(p))
print(type(s))

print(p.first_name, p.last_name)
print(s.first_name, s.last_name, s.grade)

# Polymorphism
p.description()
s.description()

Person.description(p)
Student.description(s)

# Shape, Circle, Square, Rectangle, Trapezoid
# Attribute
# Area, Perimeter 