import copy

import numpy as np
from scipy.constants import point
from tabulate import tabulate

import init
from init import print_poly


def mult_pol(a: np.array, b: np.array) -> np.array:
    res = np.zeros(len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            res[i+j] += a[i] * b[j]
    return res

def integrate_polynomial(p: np.array) -> np.array:
    for i in range(len(p)):
        p[i] /= i+1

    p = np.insert(p, 0, 0)
    return p

def get_value_for_polynomial(p: np.array, x: float):
    res = 0
    for i in range(len(p)):
        res += p[i] * x ** i
    return res

def get_definitive_integral(integrated_p: np.array, a: int, b: int):
    return get_value_for_polynomial(integrated_p, b) - get_value_for_polynomial(integrated_p, a)

def get_lagrange_polynomial(points, number: int) -> np.array:
    res = [1]
    div = 1
    for i in range(len(points)):
        if i != number:
            res  = mult_pol(res, [-points[i], 1])
            div *= points[number] - points[i]

    print(f"l[{number}]: ("+print_poly(res)+f")/{div}")

    for i in range(len(res)):
        res[i] /= div
    return res

def calculate_approximate_value(w, points):
    approx_f = 0
    for i in range(len(w)):
        approx_f += w[i] * init.f(points[i])

    return approx_f

def calculate_ast(points, w, a, b):
    ans = 0
    while is_accurate(points, w, ans, a, b):
        ans += 1
    return ans


def test_polynomial(points, w, power):
    res = 0
    for i in range(len(w)):
        res += w[i] * pow(points[i], power)

    return res

def is_accurate(points, w, power, a, b):
    test_value = b ** (power + 1) / (power + 1) - a ** (power + 1) / (power + 1)
    poly_value = test_polynomial(points, w, power)
    print(f"step {power}:\nintegral(x^{power}) on [{a}, {b}] = {test_value}")
    print(f"sum(w[i] * f[i]): {poly_value}")
    return abs(test_value - poly_value) < 0.000000001


def solve(points):
    polynomials = []
    integrated_polynomials = []
    w = []
    for i  in range(len(points)):
        l_p = get_lagrange_polynomial(points, i)
        polynomials.append(l_p)
        integrated_polynomials.append(integrate_polynomial(copy.deepcopy(l_p)))
        current_w = get_definitive_integral(integrated_polynomials[-1], points[0], points[-1])
        w.append(current_w)
    print("Integrated polynomials table:")
    print(tabulate(integrated_polynomials, headers=[f"x^{i}" for i in range(len(points) + 1)]))
    print("\n")
    print(tabulate([w], headers=[f"w[{i}]" for i in range(len(points))]))
    print("Finding AST:")
    ast = calculate_ast(points, w, points[0], points[-1]) - 1
    print(f"AST = {ast}")
    print(f"approximate value of integral: {calculate_approximate_value(w, points)}")
    return w, ast, calculate_approximate_value(w, points)



