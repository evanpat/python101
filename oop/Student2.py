
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    
    def get_name(self):
        return self.name

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def get_students(self):
        return self.students

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_score(self):
        value = 0
        for student in self.students:
            value += student.score
        
        return value / len(self.students)


        
s1 = Student("Patrick", 12, 90)
print(s1.get_name())

s2 = Student("Joe", 13, 70)
print(s2.get_name())

c = Course("Maths", 2)
c.add_student(s1)
c.add_student(s2)
#print(len(c.get_students))
print(c.get_average_score())