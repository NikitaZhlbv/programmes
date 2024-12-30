import math

def rounder(number):
    factor = 10 ** 2
    integer_part = int(number * factor)
    fractional_part = number * factor - integer_part
    if fractional_part >= 0.5:
        integer_part += 1
    return integer_part / factor
def mass (radius, height):
    size = height * ((radius**2)* math.pi)
    mass = size * 1000
    mass = rounder(mass)
    return mass
print (mass(10,10))