from fractions import Fraction

def as_fraction(fl):
    return Fraction(fl).limit_denominator()