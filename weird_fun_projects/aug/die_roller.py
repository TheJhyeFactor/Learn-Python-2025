#this is going to be a simple dice roller
import random


rolls = int(input("please enter in the number of times you want to roll the Dice: "))


def dice_roll(num):
    for i in range(num):
        print(random.randint(1, 6))
        print("There you have it a simple 6 sided dice roll enjoy (;)")



dice_roll(rolls)