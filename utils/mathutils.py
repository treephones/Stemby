from fractions import Fraction
from re import split

def remove_all(list, vals):
    return [elem for elem in list if elem not in vals]
def as_fraction(fl):
    return Fraction(fl).limit_denominator()

def get_units(thing):
    arr = split('([-+]?\d+\.\d+)|([-+]?\d+)', thing)
    return remove_all(arr, [None, ""])