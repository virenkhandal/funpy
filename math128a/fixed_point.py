import math
from math import e

def function(x):
    return math.sqrt(1 + (1/x))

def method(p0, TOL, n, lower_bound, upper_bound):
    print("Question: Use the bisection method to find the root of " + "x^3-x-1" + " with initial approximation " + str(p0) + " with tolerance " + str(TOL) + ".")
    print("Value at p: ", function(p0))

    i = 1
    while i <= n:
        p = function(p0)
        print("p_" + str(i) + " = " + str(p) + ".")
        if abs(p - p0) < TOL and p > lower_bound and p < upper_bound:
            print("Approximation " + str(p) + " found on iteration " + str(i) + ".")
            return
        i = i + 1
        p0 = p
    print("Unsuccessful in finding an approximation within " + str(TOL) + " in " + str(n) + " iterations.")
    return

if __name__ == '__main__':
    inital_approximation = float(input("Enter your initial approximation: "))
    tolerance = float(input("Enter your tolerance: "))
    max_iterations = int(input("Enter the maximum number of iterations: "))
    lower_bound = int(input("Enter your lower bound: "))
    upper_bound = int(input("Enter your upper bound: "))
    method(inital_approximation, tolerance, max_iterations, lower_bound, upper_bound)