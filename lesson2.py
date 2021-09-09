name = input("What is your name? ")

while name != "Patrick":
    print("I don't know you")
    name = input("What is your name? ")

print("Hi!", name)
age = int(input("How old are you? "))
if age <= 2:
    print("You are an infant")
elif age >= 2 and age < 5:
    print("You are in kindergarden")
elif age >= 6 and age < 12:
    print("You are in primary school")
elif age >= 12 and age < 17:
    print("You are in high school")
else:
    print("You are too old")
