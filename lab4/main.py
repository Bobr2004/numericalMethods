import numpy as np

import unknown_coefficient
import linear_spline
import cubic_spline
def print_info():
    print('''Lab Work No. 4 in Numerical Methods by student of group IPS-32, Shovkoplias Bohdan.
Select a task:
1. Construct a power polynomial using the method of undetermined coefficients at five points for the function 3∗x^8−2∗x^5+3∗x^2+1 on the interval [0..4].
2. Construct a cubic spline for the previous problem using the points x = 0, 2, 4. Augment the system of equations with the values of the actual derivative at the boundaries.
3. Construct a linear spline for the first problem with a distance of 0.5 between the interval division points.
''')

while True:
    try:
        inp = int(input("Enter an integer from the range [1, 3]: "))
        if 1 <= inp <= 3:
            break
        else:
            raise ValueError
    except ValueError:
        print("Invalid input")

if inp == 1:
    unknown_coefficient.solve(0, 4, 4)
elif inp == 2:
    cubic_spline.solve([0, 2, 4])
else:
    linear_spline.solve([i/2 for i in range(9)])
