#1) pass by value for function
def fn1(n):
    n = n + 1
    print(n)
    
a = 1
fn1(a)
fn1(a)


#2) pass by reference for function
def fn2(n):
    n[0] = n[0] + 1
    print(n[0])
    
x = [1]    
fn2(x)
fn2(x)

#3) pass by reference for class
class Person:
    def __init__(self, age):
        self.age = age
        
    def addAge(self, number):
        self.age = self.age + number
        
p = Person(30)
print(p.age)
p.addAge(2)
print(p.age)
q = p
q.addAge(3)
print(p.age)
print(q.age)

