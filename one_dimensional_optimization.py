"""
1. Suprogramuokite vienmačio optimizavimo intervalo dalijimo pusiau, auksinio pjūvio ir Niutono metodo algoritmus.

2. Aprašykite tikslo funkciją f(x) = (x^2 − 5)^2 / 4

3. Minimizuokite šią funkciją intervalo dalijimo pusiau ir auksinio pjūvio metodais intervale [0,10] iki tikslumo 10^−4 bei Niutono metodu nuo x0 = 5 kol žingsnio ilgis didesnis už 10^−4.

4. Palyginkite rezultatus: gauti sprendiniai, rastas funkcijos minimumo įvertis, atliktų žingsnių ir funkcijų skaičiavimų skaičius.

5. Vizualizuokite tikslo funkciją ir bandymo taškus.

"""

# TODO: Properly import matplotlib
# from matplotlib import mathtext as mt
# from dataclasses import dataclass

# TODO: Use Dataclass later?
# @dataclass
# class BisectionResult:
#     x1 : float
#     x_middle : float 
#     x2 : float
#     interval_length : list[int]

# TODO: Type hints for function arguments
def objective_function(x, objective_function_calls = 0):
    objective_function_calls += 1
    return (x**2 - 5)**2 / 4

# TODO: Define a variable argument function for printing variables
# def print_variables(xargs):
#     print("xargs[1]:", xargs[1])
#     print("-------------------------------------------------")
#     print()

# TODO: Type hints for function arguments
def bisection_method(interval = [0, 10], tolerance_lipschitz_constant = 10**-4):
    left_bound: float = interval[0]
    right_bound: float = interval[1]
    interval_length = right_bound - left_bound

    print("Before initiating the method")
    print("Interval:", [left_bound, right_bound])
    print("Interval length:", interval_length)
    print("-------------------------------------------------")

    iteration = 0
    objective_function_calls = 0
    x1: float | None = None
    x_middle: float | None = None
    x2: float | None = None
    f_x1: float | None = None
    f_x_middle: float | None = None
    f_x2: float | None = None
    
    while interval_length > tolerance_lipschitz_constant:
        interval_length = right_bound - left_bound
        
        print("Current iteration:", iteration)
        print("Interval:", [left_bound, right_bound])
        print("Interval length:", interval_length)
        
        if x_middle is None:
            x_middle = (left_bound + right_bound) / 2 # 1.
            f_x_middle = objective_function(x_middle, objective_function_calls) # 1.
        x1 = left_bound + interval_length / 4 # 2.
        f_x1 = objective_function(x1, objective_function_calls) # 2.
        
        if f_x1 < f_x_middle: # 3. x_middle becomes x_1
            right_bound = x_middle # 3.1
            x_middle = x1 # 3.2
            f_x_middle = f_x1 # 3.2

            # print_variables(objective_function_calls)
            print("objective_function_calls", objective_function_calls)
            print("x1:", x1)
            print("x2:", x2)
            print("x_middle:", x_middle)
            print("f_x1:", f_x1)
            print("f_x2:", f_x2)
            print("f_x_middle:", f_x_middle)
            print("-------------------------------------------------")
            print()
            interval_length = right_bound - left_bound
            iteration += 1
            continue # 6. is while loop condition

        else: # 2.
            x2 = right_bound - interval_length / 4 # 2.
            f_x2 = objective_function(x2, objective_function_calls) # 2.
        if f_x2 < f_x_middle: # 4. x_middle becomes x_2
            left_bound = x_middle # 4.1 
            x_middle = x2 # 4.2 
            f_x_middle = x2 # 4.2
        else: # 5. x_middle stays x_middle
            left_bound = x1 # 5.1 
            right_bound = x2 # 5.1

        # print_variables(objective_function_calls)
        print("objective_function_calls", objective_function_calls)
        print("x1:", x1)
        print("x2:", x2)
        print("x_middle:", x_middle)
        print("f_x1:", f_x1)
        print("f_x2:", f_x2)
        print("f_x_middle:", f_x_middle)
        print("-------------------------------------------------")
        print()

        interval_length = right_bound - left_bound
        iteration += 1

# TODO: Print objective function?
bisection_method()