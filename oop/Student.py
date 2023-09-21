# object oriented programming

name = ['Patrick', 'Alex', 'Brendan', 'Aidan']
age = [12, 13, 13, 13]
gender = ['M', 'M', 'M', 'M']


# student 1
for i in range(len(name)):
    print (name[i], age[i], gender[i])
    
#variable type - number, string, boolean

## class - Student
## object - s1, s2, s3
## attribute - name, age, gender (variable in class)
## self
## constructor __init__
## method - info() (function in class)

class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def info(self):
        print("Student->", self.name, self.age, self.gender)

s = [Student("Patrick", 12, "M"), 
     Student("Alex", 13, "M"), 
     Student("Brendan", 13, "M"), 
     Student("Aidan", 13, "M")]

for i in range(len(s)):
    s[i].info()
    
  
