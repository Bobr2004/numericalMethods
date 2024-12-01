import numpy as np
from tabulate import tabulate
def update_x(x: np.array, a: np.array) -> np.array:
    return a @ x

def infinity_norm(a: np.ndarray) -> float:
    ans = 0.0
    for i in range(len(a)):
        ans = max(ans, sum(list(map(abs, a[i]))))
    return ans

def get_matrix_B(a: np.array) -> np.array:
    return np.eye(a.shape[0])*infinity_norm(a) - a

def solve(matrix : np.array, epsilon: float) -> float:
    norm_a = infinity_norm(matrix)
    print("||A|| = ", norm_a)
    x = np.ones(matrix.shape[0])
    b = get_matrix_B(matrix)
    print(tabulate(b, tablefmt="fancy_grid"))
    eig_old = 0.0000001
    eig = 1488
    table = list()
    table.append(["x_0"] + list(x) + ["-", "-"])
    while True:
        old_x = x.copy()
        x = update_x(b, x)
        eig = x[0]/old_x[0]
        table.append([f"x_{len(table)}"] + list(x) + [f"λ_max_B_{len(table)}: {eig}", f"eps: {abs(eig_old - eig)}"])
        if abs(eig_old - eig) < epsilon:
            break
        eig_old = eig
    print(tabulate(table, tablefmt="fancy_grid"))

    return norm_a - eig
