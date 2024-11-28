import numpy as np
from numpy.f2py.auxfuncs import throw_error

from jacobi import solve_eq_jacobi
from simpleIteration import solve_eq_simple_iteration
import initInfo as inInf
from sqrtMethod import solve_eq_sqrt_method

inInf.print_info()
inp = ""
while True:
    try:
        inp = int(input("Enter an integer in the range [1, 3]: "))
        if 1 <= inp <= 3:
            break
        else:
            raise ValueError
    except ValueError:
        print("Invalid input")

precision = 0.001
if inp == 1 or inp == 3:
    precision = input(f"Enter the desired precision in the range from 10^-12 to 1, or press enter to keep the default precision of 0.001: ")
    if precision == "":
        precision = 0.001
    while inInf.is_float(precision) == False or float(precision) > 1 or float(precision) < 1e-12:
        precision = input(f"Enter the desired precision in the range from 10^-12 to 1, or press enter to keep the default precision of 0.001: ")
        if precision == "":
            precision = 0.001
            break
    precision = float(precision)


a = np.array(inInf.matrices_a[inp - 1])
b = np.array(inInf.matrices_b[inp - 1]).T
if inp == 1:
    solve_eq_simple_iteration(a, b, precision)
elif inp == 2:
    solve_eq_sqrt_method(a, b)
elif inp == 3:
    solve_eq_jacobi(a, b, precision)
