import random

# A program that enables a user to challenge a computer by guessing a dice roll.
# COMPUTER TURN
computer = random.randint(1, 6)

# YOUR TURN
you = int(input('Guess the number (1-6): '))

# Check if the user's guess matches the computer's dice roll
won = you == computer

print(f'Computer rolled: {computer}')
print(f'You won: {won}')