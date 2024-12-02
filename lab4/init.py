import numpy as np


def f(x: float) -> float:
    return 3 * (x ** 8) - 2 * (x ** 5) + 3 * (x ** 2) + 1

def first_derivative(x: float) -> float:
    return 24 * (x ** 7) - 10 * (x ** 4) + 6 * x


def gauss_elimination(A, b, comment = True):
    n = len(b)
    if comment:
        print(f"Matrix A:\n{A}\nVector b:\n{b}\n")
    for i in range(n):
        max_row = i + np.argmax(np.abs(A[i:, i]))
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]
        pivot = A[i, i]
        A[i] = A[i] / pivot
        b[i] = b[i] / pivot
        for j in range(i + 1, n):
            factor = A[j, i]
            A[j] -= factor * A[i]
            b[j] -= factor * b[i]
        if comment:
            print(f"Step {i + 1}:\nMatrix A:\n{A}\nVector b:\n{b}\n")

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = b[i] - np.dot(A[i, i + 1:], x[i + 1:])
    return x

def print_poly(coef: np.array, x_form:str = "x") -> str:
    ans="";
    for i in range(len(coef)):
        if i > 0:
            if coef[i] >= 0:
                ans+=" + "
        ans+=str(coef[i])
        if i > 0:
            ans+=f" * {x_form}^{i}"
    return ans