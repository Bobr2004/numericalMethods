import numpy as np
import scipy.interpolate as interpolate
import init
from init import first_derivative, print_poly


def get_a_coefficient(points: np.array) -> np.array:
    return [init.f(x) for x in points]

def create_matrix_a(x: np.array) -> np.array:
    n = len(x)
    a = np.zeros((n, n))
    for i in range(n):
        if i > 0:
            a[i][i] += 2*(x[i] - x[i - 1])
            a[i][i-1] = x[i] - x[i - 1]
        if i < n-1:
            a[i][i] += 2*(x[i+1] - x[i])
            a[i][i+1] = x[i + 1] - x[i]

    return a
def get_h(x: np.array) -> np.array:
    return [x[i+1] - x[i] for i in range(len(x)-1)]
def create_matrix_r(x: np.array) -> np.array:
    n = len(x)
    h = get_h(x)
    r = np.zeros(n)
    r[0] = 3 * ((init.f(x[1]) - init.f(x[0]))/h[0] - init.first_derivative(x[0]))
    for i in range(1, n-1):
        r[i] = 3 * ((init.f(x[i+1]) - init.f(x[i]))/h[i] - (init.f(x[i]) - init.f(x[i-1]))/h[i-1])
    r[n-1] = 3 * (init.first_derivative(x[n-1]) - (init.f(x[n-1]) - init.f(x[n-2]))/h[n-2])
    return r

def eq_for_c(x: np.array) -> np.array:
    a = create_matrix_a(x)
    r = create_matrix_r(x)
    print("A: ", a)
    print("r: ", r)
    c = init.gauss_elimination(a, r, False)
    return c

def get_b(x: np.array, c: np.array) -> np.array:
    n = len(x)
    b = np.zeros(n-1)
    h = get_h(x)
    for i in range(n-1):
        b[i] = (init.f(x[i+1]) - init.f(x[i]))/h[i] - h[i]/3*(2*c[i] + c[i+1])
    return b

def get_d(x: np.array, c: np.array) -> np.array:
    n = len(x)
    d = np.zeros(n-1)
    h = get_h(x)
    for i in range(n-1):
        d[i] = (c[i+1]-c[i])/(3 * h[i])
    return d




def test():
    x = np.array([0, 2, 4])  # координати вузлів
    y = 3 * x**8 - 2 * x**5 + 3 * x**2 + 1  # значення функції у вузлах
    # Похідні на краях
    f_prime_0 = 24 * 0**7 - 10 * 0**4 + 6 * 0  # похідна в x=0
    f_prime_n = 24 * 4**7 - 10 * 4**4 + 6 * 4  # похідна в x=4
    cs = interpolate.CubicSpline(x, y, bc_type=((1, f_prime_0), (1, f_prime_n)))
    print(cs.c)


def solve(points: np.array) -> np.array:
    x = np.array(points)
    a = get_a_coefficient(points)
    c = eq_for_c(points)
    b = get_b(points, c)
    d = get_d(points, c)
    print("a:", a, "\nb:", b, "\nc:", c, "\nd:", d)
    for i in range(len(b)):
        print(f"Проміжок [{x[i]}, {x[i+1]}]: {print_poly([a[i], b[i], c[i], d[i]], f"(x-{x[i]})")}")

    return a, b, c, d


