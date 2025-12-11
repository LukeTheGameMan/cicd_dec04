import math

def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def mult (a, b):
    return a*b

def div (a, b):
    if b == 0:
        raise ZeroDivisionError("ERROR: Divided by zero")
    return a/b

def log (a, b):
    if a <= 0 or b < 1:
        raise Exception("ERROR: Expected positive, non-zero argument and greater-than-1 base")
    return math.log(a, b)

def square (a):
    return a*a

def sin (a, degrees=False):
    if degrees:
        return math.sin(math.radians(a))
    return math.sin(a)

def cos (a, degrees=False):
    if degrees:
        return math.cos(math.radians(a))
    return math.cos(a)

def sqrt (a):
    if a < 0:
        raise Exception("ERROR: Expected non-negative argument")
    return math.sqrt(a)

def perc (a, b):
    if b == 0:
        raise ZeroDivisionError("ERROR: Divided by zero")
    return (a/b) * 100
