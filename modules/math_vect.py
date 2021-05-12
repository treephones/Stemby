import numpy as np
from utils.mathutils import as_fraction

def dot_product(a,b):
    a = np.array(a)
    b = np.array(b)
    return a.dot(b)

def multiply(a, b):
    a = np.array(a)
    b = np.array(b)
    return a*b

def addition(a, b):
    a = np.array(a)
    b = np.array(b)
    return a+b

def subtraction(a, b):
    a = np.array(a)
    b = np.array(b)
    return a-b

def is_orthogonal(a, b): #format vector parameters as a list ([1,2], [2,-1])
    a = np.array(a)
    b = np.array(b)
    return a.dot(b) == 0

def ortho_proj(a,b): #orthogonal projection of b onto a
    a = np.array(a)
    b = np.array(b)

    numerator = a.dot(b)
    denominator = a.dot(a)

    proj = (numerator/denominator)*a
    output = [str(as_fraction(proj[i])) for i in range(len(proj))]
    return output