import numpy as np

import powerMethod
import jacobiRotation
import newtonMethod
def print_info():
    print('''Lab Work No. 3 in Numerical Methods by student of group IPS-31, Shovkoplias Bohdan.
Select a task:
1. Find the smallest eigenvalue of a matrix using the power method:
    3 1 1 0 
    1 3 0 2 
    1 0 4 1 
    0 2 1 4
2. Find approximations of all eigenvalues of a matrix using the Jacobi rotation method:
    3 1 1 0 
    1 3 0 2 
    1 0 4 1 
    0 2 1 4
3. Solve a system of nonlinear equations using Newton's method:
    x = e^{-y}
    y = e^x.
''')

matrix = [
            [3.0, 1.0, 1.0, 0.0],
            [1.0, 3.0, 0.0, 2.0],
            [1.0, 0.0, 4.0, 1.0],
            [0.0, 2.0, 1.0, 4.0]
          ]
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
    powerMethod.solve(np.array(matrix), 0.001)
elif inp == 2:
    jacobiRotation.solve(5, matrix)
else:
    newtonMethod.solve(5, np.array([1, 1]))
