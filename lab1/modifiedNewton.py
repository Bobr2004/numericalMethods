import copy
a = 4.5
b = 5.4


def f(arg: float) -> float:
    return arg**3 - 5*arg**2 - 4*arg + 20


def derivative(arg: float) -> float:
    return 3*arg**2 - 10*arg - 4


def newton_get_a():
    return a


def newton_get_b():
    return b


def newton_find_answer(precision: float):
    x = []
    f_x = []
    iterations = 1
    x_0 = 5.05
    x_n = x_0
    x_old = 1000000000
    while abs(x_old - x_n) > precision:
        x.append(x_n)
        f_x.append(f(x_n))
        x_old = copy.deepcopy(x_n)
        x_n = x_n - f(x_n) / derivative(x_0)
        iterations += 1

    x.append(x_n)
    f_x.append(f(x_n))
    return list(range(1, iterations + 1)), x, f_x
