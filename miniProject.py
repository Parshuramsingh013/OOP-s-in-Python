import random

target = random.randint(1,100)

while True:
    userChoice = int(input("Gauss The Target : "))

    if (userChoice == target):
        print("Success : Target Achieved !!")
        break
    elif (userChoice < target):
        print("Your guess number is too small. Guess the Bigger Number....!")
    else:
        print("Your guess number is too large. Guess the Smaller Number....!")


print("----Game Over----")

