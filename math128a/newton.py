import math
from math import e, cos, sin


def derivative(x):
    return (2400 * (x ** 3)) - (1650 * (x ** 2)) + (400 * x) - 20


def function(x):
    return  (600 * (x ** 4)) - (550 * (x ** 3)) + (200 * (x ** 2)) - (20 * x) - 1

def method(p0, TOL, n):
    print("Question: Use the newton method to find the root" + " with initial approximation " + str(p0) + " with tolerance " + str(TOL) + ".")
    print("Value at p: ", function(p0))

    i = 1
    while i <= n:
        p = p0 - (function(p0) / derivative(p0))
        print("p_" + str(i) + " = " + str(p) + ".")
        if abs(p - p0) < TOL:
            print("Approximation " + str(p) + " found on iteration " + str(i) + ".")
            return
        i = i + 1
        p0 = p
    print("Unsuccessful in finding an approximation within " + str(TOL) + " in " + str(n) + " iterations.")
    return

if __name__ == '__main__':
    inital_approximation = float(input("Enter your first initial approximation: "))
    tolerance = float(input("Enter your tolerance: "))
    max_iterations = int(input("Enter the maximum number of iterations: "))
    method(inital_approximation, tolerance, max_iterations)