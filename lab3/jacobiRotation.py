import math

import numpy as np
from numpy.ma.core import arctan
from tabulate import tabulate


def get_max_element(matrix: np.array):
    ans = (0, 1)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i != j and abs(matrix[i][j]) > matrix[ans[0]][ans[1]]:
                ans = (i, j)
    print(f"a_max = a[{ans[0]}][{ans[1]}] = {matrix[ans[0]][ans[1]]}")
    return ans

def get_angle(matrix: np.array):
    i, j = get_max_element(matrix)
    res = math.pi/4
    if matrix[i][i] != matrix[j][j]:
        res = arctan(2 * matrix[i][j] / (matrix[i][i] - matrix[j][j])) / 2
    print(f"phi_k = {res}")
    return res

def create_u(dimensions: int, phi, i: int, j: int) -> np.array:
    u = np.eye(dimensions)
    u[i][i] = math.cos(phi)
    u[j][j] = math.cos(phi)
    u[j][i] = -math.sin(phi)
    u[i][j] = math.sin(phi)
    print("U:", tabulate(u, tablefmt="fancy_grid"), sep="\n")
    return u

def update_a(a: np.array) -> np.array:
    phi = get_angle(a)
    i, j = get_max_element(a)
    u = create_u(a.shape[0], phi, i, j)
    return u @ a @ u.T

def solve(number_of_iterations: int, matrix: np.array) -> np.array:
    a = np.array(matrix)
    print(f"a_{0}:", tabulate(a, tablefmt="fancy_grid"), sep="\n")
    for i in range(number_of_iterations):
        print(f"{i+1} iteration:")
        a = update_a(a)
        print(f"a_{i+1}:", tabulate(a, tablefmt="fancy_grid"), sep="\n")
    return a



