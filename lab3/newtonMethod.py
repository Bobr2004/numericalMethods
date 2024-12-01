import math
import numpy as np
from tabulate import tabulate


def f1(x, y):
    return x - math.e ** (-y)

def f2(x, y):
    return y - math.e ** x

def get_f_matrix(x, y) -> np.array:
    res = np.array([f1(x, y), f2(x, y)]).T
    print("F:")
    print(tabulate([res], tablefmt="fancy_grid"))
    return res

def get_jacobi_matrix(x, y):
    res = np.array([[1, math.e ** (-y)], [- math.e ** x, 1]])
    print("J:")
    print(tabulate(res, tablefmt="fancy_grid"))
    return res

def update_x(x: np.array) -> np.array:
    return x - np.linalg.inv(get_jacobi_matrix(x[0], x[1])) @ get_f_matrix(x[0], x[1])

def solve(number_of_iterations: int, matrix: np.array) -> np.array:
    x = np.array(matrix)
    print(f"x_{0}:", tabulate([x], tablefmt="fancy_grid"), sep="\n")
    for i in range(number_of_iterations):
        print(f"{i+1} iteration:")
        x = update_x(x)
        print(f"x_{i+1}:", tabulate([x], tablefmt="fancy_grid"), sep="\n")
    return x