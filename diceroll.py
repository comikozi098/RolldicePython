# Script lets you roll a 6 sided dice!

import random
print("Let's roll some dice!")

number = random.randint(1, 6)

rollDice = input('Would you like to roll the dice? :- ')

if rollDice == "y":
    print("The dice has rolled a", number)
    rollDice = input("Would you like to roll again? :- ")
else:
    print("Fine what ever.. it would have been", number)
