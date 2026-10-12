
###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
b = input('b=')
c = input('c=')
a = int(a)
b = int(b)
c = int(c)
volume = a * b * c
surface_area = 2 * (a * b + a * c + b * c)
print(f'The volume of a cuboid with sides {a}, {b}, and {c} is {volume}')
print(f'The surface area of a cuboid with sides {a}, {b}, and {c} is {surface_area}')