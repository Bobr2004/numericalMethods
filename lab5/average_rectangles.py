import numpy as np
from numpy import number
from tabulate import tabulate

import init
from init import f

def get_value(a: int, b: int, number_of_intervals: int):
    h = (a+b)/number_of_intervals
    ans = 0
    for i in range(number_of_intervals):
        ans += f(a + i * h + h / 2) * h
    return ans


def solve(a: int, b: int, precision):
    n = b - a
    info = []
    ans = get_value(a, b, n)
    cur_eps = 1000000000
    info.append([0, n, ans, "-"])
    n*=2
    i = 1

    while cur_eps >= precision:
        new_ans = get_value(a, b, n)
        cur_eps = abs(ans - new_ans)
        ans = new_ans
        info.append([i, n, ans, cur_eps])
        n *= 2
        i += 1
    print(tabulate(info, tablefmt="fancy_grid", headers=["№", "n", "approx_value", "epsilon"]))
    return ans






