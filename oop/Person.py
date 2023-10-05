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

    def description(self):
        print(f"I'm a Student: {self.first_name} {self.last_name}, Grade:{self.grade}")

class Teacher(Person):
    def __init__(self, first_name, last_name, title):
        super().__init__(first_name, last_name) 
        self.title = title
        
    def description(self):
        print(f"I'm a Teacher: {self.first_name} {self.last_name} {self.title}")


p = Person("Person", "A")
s = Student("Alex", "Wong", "F.2")
t = Teacher("Patrick", "Lai", "Coding Teacher")
print(type(p))
print(type(s))
print(type(t))

print(p.first_name, p.last_name)
print(s.first_name, s.last_name, s.grade)
print(t.first_name, t.last_name)
# Polymorphism
p.description()
s.description()
t.description()

Person.description(p)
Student.description(s)
