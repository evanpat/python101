import random

selectionChoices = ["rock", "paper", "scissors"];
print("Rock beats scissors. Scissors cut paper. Paper covers rock.")

player = ""

while player != "quit":
    player = input("What is your take: ")
    player = player.lower()
    computer = random.choice(selectionChoices)
    print("You selected " + player + ", and the computer selected " + computer + ".")
    
    if player == computer:
      print("Draw!")
    elif player == "rock":
      if computer == "scissors":
        print("Victory!")
      else:
        print("You lose!")
    elif player == "paper":
        if computer == "rock":
          print("Victory!")
        else:
          print("You lose!")
    elif player == "scissors":
        if computer == "paper":
          print("Victory!")
        else:
          print("You lose!")
    else:
      print("Something went wrong...")                
      print()