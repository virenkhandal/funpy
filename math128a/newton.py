import math
from math import e, cos, sin


def derivative(x):
    return (3 * math.cos(3 * x)) + (3 * (math.e ** (-2 * x)) * math.cos(x)) - (6 * (math.e ** (-2 * x)) * math.sin(x)) + (3 * (math.e ** (-1 * x)) * math.sin(2 * x)) - (6 * (math.e ** (-1 * x)) * math.cos(2 * x)) + (3 * (math.e ** (-3 * x)))


def function(x):
    return (math.sin(3 * x)) + (3 * (math.e ** (-2 * x)) * math.sin(x)) - (3 * (math.e ** (-1 * x)) * math.sin(2 * x)) - (math.e ** (-3 * x)) 

def method(p0, TOL, n):
    print("Question: Use the newton method to find the root of " + "x^2 - 10cos(x)" + " with initial approximation " + str(p0) + " with tolerance " + str(TOL) + ".")
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