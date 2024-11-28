import numpy as np
from tabulate import tabulate


def update_values(matrix_a: np.ndarray, matrix_b: np.ndarray, x_k: np.array) -> np.array:
    n = x_k.shape[0]
    x_new = np.zeros(n)
    for i in range(n):
        x_new[i] = 1/matrix_a[i][i] * (matrix_b[i] - sum([matrix_a[i][j]*x_k[j] for j in range(n) if j != i]))

    return x_new

def solve_eq_jacobi(matrix_a: np.array, matrix_b: np.array, epsilon: float = 0.001) -> np.array:
    x = np.zeros(matrix_a.shape[0])
    current_epsilon = 100000
    table = list()
    table.append([0]+list(x)+["-"])
    while current_epsilon >= epsilon:
        new_x = update_values(matrix_a, matrix_b, x)
        current_epsilon = max([abs(new_x[i] - x[i]) for i in range(len(x))])
        x = new_x
        table.append([len(table)]+list(x) + [current_epsilon])

    print(tabulate(table, headers=["№"] + [f"x_{i+1}" for i in range(len(x))] + ["epsilon"], tablefmt="fancy_grid"))
    return x