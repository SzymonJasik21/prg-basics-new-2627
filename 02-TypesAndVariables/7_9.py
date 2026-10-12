import random

# A program that prints the number of dice rolled and the value True if the number rolled is 1 or 6.
dice_rolled = random.randint(1, 6)

special_number = dice_rolled == 1 or dice_rolled == 6

print(f'Dice rolled: {dice_rolled}')
print(f'Special number (1 or 6): {special_number}')