import math
from re import split
from fractions import Fraction

def remove_all(list, vals):
    return [elem for elem in list if elem not in vals]

def as_fraction(fl):
    return Fraction(fl).limit_denominator()

def get_units(thing):
    arr = split('([-+]?\d+\.\d+)|([-+]?\d+)', thing)
    return remove_all(arr, [None, ""])

def quadratic(a, b, c):
    disc = (b**2)-(4*a*c)
    if disc < 0:
        return None
    elif disc == 0:
        return -b/(2*a)
    else:
        return (((-b+math.sqrt(disc))/(2*a)),((-b-math.sqrt(disc))/(2*a)))