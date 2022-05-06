#Dice roller
import random

dice1 = random.randint(1, 6)
dice2 = random.randrange(6) + 1

total = dice1 + dice2
print("You rolled a", dice1, "and a", dice2, "for total of", total)
input("\nPress the enter key to exit.")