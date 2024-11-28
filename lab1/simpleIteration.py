import numpy as np
import math
import copy

a = 5.5
b = 6.6


def simple_get_a():
    return a


def simple_get_b():
    return b


def phi(x: float) -> float:
    return -18/(x**2) - 9/x + 8


def derivative(x: float) -> float:
    return 9*(x + 4) / x**3


def get_q() -> float:
    return derivative(a)


def simple_theoretical_iterations(epsilon: float) -> float:
    q = get_q()
    return math.floor(math.log((b - a) / ((1.0 - q) * epsilon)) / math.log(1.0/q)) + 1


def simple_find_answer(precision: float):
    x = []
    f_x = []
    iterations = 1
    x_0 = (a+b) / 2
    x_old = 1000000000
    while abs(x_old - x_0) > precision:
        x.append(x_0)
        f_x.append(phi(x_0) - x_0)
        x_old = copy.deepcopy(x_0)
        x_0 = phi(x_0)
        iterations += 1

    x.append(x_0)
    f_x.append(x_0 - phi(x_0))
    return list(range(1, iterations + 1)), x, f_x


def find_intervals():
    local_a = 5
    local_b = 8
    for local_a in range(5000, 5990):
        for local_b in range(6010, 9000):
            a_n = local_a / 1000
            b_n = local_b / 1000
            x0 = (a_n+b_n)/2
            if abs(phi(x0) - x0) <= (1 - derivative(a_n)) * (b_n - a_n) / 2.0:
                if a % 100 == 0 and b % 100 == 0:
                    print(a_n, b_n, sep=" ")
