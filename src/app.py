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

