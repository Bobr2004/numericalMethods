import operator

import numpy as np
from tabulate import tabulate
import simpleIteration


def get_matrices(matrix_a : np.array) -> np.array:
    n = matrix_a.shape[0]
    s = np.zeros(matrix_a.shape)
    d = np.zeros(matrix_a.shape)
    for i in range(matrix_a.shape[0]):
        d[i][i] = np.sign(matrix_a[i][i] - sum([s[p][i] ** 2 * d[p][p] for p in range(i)]))
        s[i][i] = np.sqrt(abs(matrix_a[i][i] - sum([s[p][i] ** 2 * d[p][p] for p in range(i)])))
        for j in range(i+1, n):
            s[i][j] = (matrix_a[i][j] - sum([s[p][i]*d[p][p]*s[p][j] for p in range(i)])) / (d[i][i] * s[i][i])

    return s, d

def display_matrices_row_by_row(s, d):
    rows = []
    for i in range(s.shape[0]):
        row = [f"I{i+1}"] + [f"{x:.4f}" for x in s[i]]
        row.append("////////")
        row += [f"I{i+1}"] + [f"{x:.4f}" for x in d[i]]
        rows.append(row)

    print("\nMatrix S and D:")
    print(tabulate(rows, headers=["S"] + [f"J{i+1}" for i in range(s.shape[1])] + ["", "D"] + [f"J{i+1}" for i in range(d.shape[1])], tablefmt="fancy_grid"))

def inverse_triangular_matrix(mt: np.array) -> np.array:
    a = mt.copy()
    result = np.zeros(a.shape)
    n = a.shape[0]
    for i in range(n):
        result[i][i] = 1

    for i in range(n-1, -1, -1):
        divisor = 1/a[i][i]
        a[i] = [a[i][j] * divisor for j in range(n)]
        result[i] = [result[i][j] * divisor for j in range(n)]
        for j in range(0, i):
            multiplier = -a[j][i]
            a[j] = [a[j][k] + a[i][k] * multiplier for k in range(n)]
            result[j] = [result[j][k] + result[i][k] * multiplier for k in range(n)]

    return result

def inverse_matrix(s: np.array, d: np.array) -> np.array:
    s_inv = inverse_triangular_matrix(s)
    d_inv = inverse_triangular_matrix(d)
    return s_inv @ d_inv @ s_inv.T



def solve_eq_sqrt_method(matrix_a : np.array, matrix_b: np.array) -> np.array:
    n = matrix_b.shape[0]
    s, d = get_matrices(matrix_a)
    display_matrices_row_by_row(s, d)

    eq_matrix = s.T @ d
    y = np.zeros(n)
    for i in range(n):
        y[i] = matrix_b[i]
        y[i] -= sum(eq_matrix[i][:i] * y[:i])
        y[i] /= eq_matrix[i][i]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        x[i] -= sum(s[i][i+1:] * x[i+1:])
        x[i] /= s[i][i]

    matrix_a_inv = inverse_matrix(s, d)
    det = 1
    for i in [d[i][i] * s[i][i] ** 2 for i in range(n)]:
        det *= i

    print("Solution:")
    print(tabulate([x], tablefmt="fancy_grid", headers = [f"x_{i+1}" for i in range(n)]))
    print("Determinant:", det)
    print("Inverse matrix:")
    print(tabulate(matrix_a_inv, tablefmt="fancy_grid", floatfmt=".4f"))
    killmepls = simpleIteration.infinity_norm(matrix_a) * simpleIteration.infinity_norm(matrix_a_inv)
    print("Condition number:", killmepls)
    return x, det, killmepls
