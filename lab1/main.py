from modifiedNewton import *
from simpleIteration import *
from pretty import pretty_table


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


inp = input('''Prepared by a student of group IPS-32, Shovkoplias Bohdan.
Choose a method for finding an approximate solution:
1 - Modified Newton's Method for the equation x^3 - 5x^2 - 4x + 20 = 0
2 - Simple Iteration Method for the equation x^3 - 8x^2 + 9x + 18 = 0
''')
while inp.isnumeric() == False or (int(inp) != 1 and int(inp) != 2):
    inp = input("Enter an integer in the range [1, 2]: ")

inp = int(inp)

if inp == 2:
    a = simple_get_a()
    b = simple_get_b()
else:
    a = newton_get_a()
    b = newton_get_b()

precision = input(
    f"Enter the desired precision in the range from 10^-12 to {(b-a)/2}: ")
while is_float(precision) == False or float(precision) > (b-a)/2 or float(precision) < 1e-12:
    precision = input(
        f"Enter the desired precision in the range from 10^-12 to {(b-a)/2}: ")
precision = float(precision)

if inp == 2:
    iterations, x, f_x = simple_find_answer(precision)
    iterations.insert(0, "n")
    x.insert(0, "x_n")
    f_x.insert(0, "x_n - phi(x_n)")
    print(pretty_table(iterations, x, f_x))
    print("A priori estimate:", simple_theoretical_iterations(precision))
    print("A posteriori estimate:", iterations[-1])
elif inp == 1:
    iterations, x, f_x = newton_find_answer(precision)
    iterations.insert(0, "n")
    x.insert(0, "x_n")
    f_x.insert(0, "f(x_n)")
    print(pretty_table(iterations, x, f_x))
    print("A posteriori estimate:", iterations[-1])
