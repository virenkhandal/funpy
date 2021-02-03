import math
from math import e

sign = lambda x: math.copysign(1, x)

def function(x):
    return (e ** x) - (x ** 2) + (3 * x) - 2

def method(a, b, error):
    print("Question: Use the bisection method to find the root of " + "(e**x) - (x**2) + (3*x) - 2" + " on the interval [" + str(a) + ", " + str(b) + "] within " + str(error) + ".")
    if sign(function(a)) == sign(function(b)):
        print("There is no root in the given interval")
        return None
    else:
        i = 0
        p = a + ((b - a) / 2)
        while (abs(function(p)) > error):
            i += 1
            p = a + ((b - a) / 2)
            curr = function(p)
            if sign(curr) == sign(function(a)):
                a = p
            else:
                b = p
            
        print("We need " + str(i) + " iterations to get a root within " + str(error) + ".")
        print("With this, our root is at " + str(p) + " with a value of " + str(curr) + ".")

if __name__ == '__main__':
    lower_bound = int(input("Enter your lower bound: "))
    upper_bound = int(input("Enter your upper bound: "))
    error = float(input("Enter your error value: "))
    method(lower_bound, upper_bound, error)