import numpy as np
from tabulate import tabulate

import init

def get_coefficients(x: float, number_of_points: int) -> np.array:
    ans = np.zeros(number_of_points+1)
    for i in range(number_of_points+1):
        ans[i] = x ** i
    return ans

def get_equation(x: float, number_of_points: int):
    return get_coefficients(x, number_of_points), init.f(x)

def get_matrix_equation(l: float, r: float, number_of_points: int) -> np.array:
    a = list()
    ans = list()
    h = (r - l)/number_of_points
    i = l
    while i <= r:
        cur = get_equation(i, number_of_points)
        ans.append(cur[1])
        a.append(cur[0])
        i += h
    return a, ans

def solve(l: int, r: int, number_of_points: int):
    a, b = get_matrix_equation(l, r, number_of_points)
    a = np.array(a)
    print("Matrix of undetermined coefficients A:")
    print(tabulate(a, tablefmt="fancy_grid"))
    inv_a = np.linalg.inv(np.array(a))
    print(f"Vector of function values: {b}")
    a_copy = a.copy()
    b_copy = np.array(b.copy())
    coefficients_gauss = init.gauss_elimination(a_copy, b_copy.T)

    print("Solution of the system (polynomial coefficients):", coefficients_gauss)

    y_calculated = np.dot(a, coefficients_gauss)
    print("Verification of function values:", y_calculated)

    x = np.array([0, 1, 2, 3, 4])
    y = 3 * x**8 - 2 * x**5 + 3 * x**2 + 1
    print("Resulting polynomial: ", end="")
    for i in range(len(coefficients_gauss)):
        if i > 0:
            if coefficients_gauss[i] > 0:
                print(" + ", end="")
        print(coefficients_gauss[i], end="")
        if i > 0:
            print(f" * x^{i}", end="")
