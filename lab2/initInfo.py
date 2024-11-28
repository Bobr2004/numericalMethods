def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def print_info():
    print('''Laboratory work #2 in numerical methods by Shovkplias Bohdan from IPS-32 group.
Choose a method for finding an approximate solution:
1. Simple iteration method for the system:
7 2 3 0     X1    32
0 3 2 6   X  X2  = 47
2 5 1 0     X3    23
0 1 4 2     X4    29

2. Square root method for solving the system, finding the determinant and conditioning number:
1 2 0     X1     8
2 2 3   X  X2  = 22  
0 3 2     X3     17

3. Jacobi method for the system:
4 0 1 0     X1     12
0 3 0 2   X  X2  = 19
1 0 5 1     X3  = 27
0 2 1 4     X4  = 30
''')

matrices_a = [
                [
                    [7.0, 2.0, 3.0, 0.0],
                    [2.0, 5.0, 1.0, 0.0],
                    [0.0, 1.0, 4.0, 2.0],
                    [0.0, 3.0, 2.0, 6.0]
                ],

                [
                    [1, 2, 0],
                    [2, 2, 3],
                    [0, 3, 2]
                ],

                [
                    [4.0, 0.0, 1.0, 0.0],
                    [0.0, 3.0, 0.0, 2.0],
                    [1.0, 0.0, 5.0, 1.0],
                    [0.0, 2.0, 1.0, 4.0]
                ]
              ]

matrices_b = [
                [32.0, 23.0, 29.0, 47.0],
                [8.0, 22.0, 17.0],
                [12.0, 19.0, 27.0, 30.0]
             ]
