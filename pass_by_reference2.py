#pass by value for function
def fn1(n):
    n = n + 1

a = 1
fn1(a)

print (a)


#pass by reference for function
class Person:
    def __init__(self, age):
        self.age = age
    
    def addAge(self):
        self.age = self.age + 1
        
p = Person(3)
print(p.age)
p.addAge()

print(p.age)