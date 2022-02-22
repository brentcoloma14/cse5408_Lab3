# Brent Coloma
# CSE 5350
# Assignment 1
# Python template

import math

def f(x):
  return math.sqrt(x) - math.cos(x)

def bisection(a,b):
    # implement Bisection Method Here
    i = 1           # Set i = 1
    TOL = 10^-5     # Tolerance
    N = 10          # Number of iterations/trials.
    FA = f(a)

    while (i <= N):
        p = (a + b) / 2   # Compute p


        FP = f(p)
        if FP == 0 or ((b-a) / 2) < TOL:
            break


        i = i + 1


        if (FA * FP) > 0:
            a = p
            FA = FP
        else:
            b = p

    return ("The value of root is:", p)

root = bisection( 0.0, 1.0)
print (root)
