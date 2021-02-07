import math
from math import e

def function(x):
    return 0.5 * ((x ** 3) + 1)

def method(p0, p1, TOL, n):
    print("Question: Use the false position method to find the root of " + "0.5*(x^3 + 1)" + " with initial approximations " + str(p0) + " and " + str(p1) + " with tolerance " + str(TOL) + " within " + str(n) + " iterations.")
    print("Value at p0: ", function(p0))
    print("Value at p1: ", function(p1))

    i = 2
    q0 = function(p0)
    q1 = function(p1)
    while i <= n:
        p = (q1(p1 - p0))/(q1-q0)
        print("p_" + str(i) + " = " + str(p) + ".")
        if abs(p - p1) < TOL:
            print("Approximation " + str(p) + " found on iteration " + str(i) + ".")
            return
        i = i + 1
        q = function(p)
        if q * q1 < 0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q
    print("Unsuccessful in finding an approximation within " + str(TOL) + " in " + str(n) + " iterations.")
    return

if __name__ == '__main__':
    inital_approximation_1 = float(input("Enter your first initial approximation: "))
    inital_approximation_2 = float(input("Enter your second initial approximation: "))
    tolerance = float(input("Enter your tolerance: "))
    max_iterations = int(input("Enter the maximum number of iterations: "))
    method(inital_approximation_1, inital_approximation_2, tolerance, max_iterations)