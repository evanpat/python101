import random as r

print("Generating a random secret number (1-100) for you to guess")
random = r.randrange(1, 100)

num = int(input("Guess the number: "))
guessed = False
count = 0

while not guessed:
    count+=1
    if num > random:
        print(f"Your guessed number {num} is greater than the secret number. Guess again")
    elif num < random:
        print(f"Your guessed number {num} is less than the secret number. Guess again")
    else:
        print(f"You guessed it right! The secret number is {random}. You have guessed {count} times.")
        guessed = True

    num = int(input("Guess the number: "))


