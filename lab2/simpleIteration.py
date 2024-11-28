import numpy as np
from tabulate import tabulate

def infinity_norm(a: np.ndarray) -> float:
    ans = 0.0
    for i in range(len(a)):
        ans = max(ans, sum(abs(a[i])))
    return ans

def update_values(current_values: np.array, matrix_a: np.array, matrix_b: np.array, tau: float) -> np.array:
    new_values = current_values.copy()
    return new_values - tau * (matrix_a @ current_values - matrix_b)

def solve_eq_simple_iteration(matrix_a: np.array, matrix_b: np.array, epsilon: float = 0.001) -> np.array:
    x = np.zeros(matrix_a.shape[0])
    tau = 2.0 / infinity_norm(matrix_a)
    current_epsilon = 100000
    table = list()
    table.append([0]+list(x)+["-"])
    while current_epsilon >= epsilon:
        new_x = update_values(x, matrix_a, matrix_b, tau)
        current_epsilon = max([abs(new_x[i] - x[i]) for i in range(len(x))])
        x = new_x
        table.append([len(table)]+list(x) + [current_epsilon])

    print(tabulate(table, headers=["№"] + [f"x_{i+1}" for i in range(len(x))] + ["epsilon"], tablefmt="fancy_grid"))
    return x