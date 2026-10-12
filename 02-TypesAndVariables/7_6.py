# The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. 
# Write a program that checks whether the vehicle speed entered from the keyboard is correct.

speed = int(input('Enter vehicle speed: '))
# Check if the speed is between 40 and 140 (inclusive)
speed_is_valid = 40 <= speed <= 140
print(f'Speed is valid: {speed_is_valid}')