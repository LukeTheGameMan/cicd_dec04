import math

def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def mult (a, b):
    return a*b

def div (a, b):
    if b == 0:
        raise Exception("ERROR: Divided by zero")
    return a/b

def log (a, b):
    if a <= 0 and b < 1:
        raise Exception(f"ERROR: Expected positive, non-zero argument and greater-than-1 base, got {a} and {b}")
    elif a <= 0:
        raise Exception(f"ERROR: Expected positive, non-zero argument, got {a}")
    elif b < 1:
        raise Exception(f"ERROR: Expected greater-than-1 base, got {b}")
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
        raise Exception(f"ERROR: Expected non-negative argument, got {a}")
    return math.sqrt(a)

def perc (a, b):
    if b == 0:
        raise Exception("ERROR: Divided by zero")
    return (a/b) * 100
