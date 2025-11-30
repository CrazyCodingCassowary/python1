import random
p = True
number = str(random.randint(10,20))

print("I will generate a number from 10 to 20, and you have to guess the number one digit at a time")
print("The game ends when you get 1 hero")

while p:
    g = input("Give me your best guess!\n")
    if number == g:
        print("you won the game!")
        print("The number was", number)
        break

    else:
        print("Your guess isn't quite right,try again.\n")


