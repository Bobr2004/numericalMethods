import numpy as np

import init
from init import f

def solve(x: np.array) -> np.array:
    n = len(x)
    k = np.zeros(n)
    b = np.zeros(n)
    for i in range(n):
        print(f"f({x[i]}) = {f(x[i])}")

    for i in range(n-1):
        k[i] = (f(x[i+1]) - f(x[i]))/(x[i+1] - x[i])
        b[i] = f(x[i]) - x[i] * k[i]
        print(f"S_{i}(x) = {f(x[i])} + {k[i]}*(x-{x[i]}) = {k[i]}*x+{b[i]}", f"for [{x[i]}, {x[i+1]}]")
    return k, b
