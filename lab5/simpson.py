import numpy as np
from numpy import number
from tabulate import tabulate

import init
from init import f

def get_value(a: int, b: int, number_of_intervals: int):
    h = (a+b)/number_of_intervals
    ans = f(a) + f(b)
    for i in range(1, number_of_intervals, 2):
        ans += f(a + i * h) * 4
    for i in range(2, number_of_intervals, 2):
        ans += f(a + i * h) * 2
    return ans*h/3


def solve(a: int, b: int, precision):
    n = b - a
    info = []
    ans = get_value(a, b, n)
    cur_eps = 1000000000
    info.append([0, n, ans, "-"])
    n*=2
    i = 1

    while cur_eps >= precision and i < 10:
        new_ans = get_value(a, b, n)
        cur_eps = abs(ans - new_ans)
        ans = new_ans
        info.append([i, n, ans, cur_eps])
        n *= 2
        i += 1
    print(tabulate(info, tablefmt="latex", headers=["№", "n", "approx_value", "epsilon"]))
    return ans






