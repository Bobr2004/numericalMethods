import numpy as np

import Interpolation
import average_rectangles
import simpson

def print_info():
    print('''Lab Work No. 5 in Numerical Methods by student of group IPS-32, Shovkoplias Bohdan.
Choose a task:
1. Construct a quadrature formula of interpolation type for the approximate integral of the function 3*x^8 - 2*x^5 + 3*x^2 + 1 at integer nodes in the interval [0..4].
2. Approximate the integral of the function 3*x^8 - 2*x^5 + 3*x^2 + 1 using the midpoint rectangle formula.
3. Approximate the integral of the function 3*x^8 - 2*x^5 + 3*x^2 + 1 using Simpson's formula.
''')

while True:
    try:
        inp = int(input("Enter an integer from the range [1, 3]: "))
        if 1 <= inp <= 3:
            break
        else:
            raise ValueError
    except ValueError:
        print("Invalid input")

if inp == 1:
    Interpolation.solve([0, 1, 2, 3, 4])
elif inp == 2:
    average_rectangles.solve(0, 4, 0.001)
else:
    simpson.solve(0, 4, 0.001)
