from fractions import Fraction
from re import split

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
        return -b/(2*a*c)
    else:
        return (((-b+disc)/(2*a*c)),((-b-disc)/(2*a*c)))