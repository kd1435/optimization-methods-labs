"""
1. Suprogramuokite vienmačio optimizavimo intervalo dalijimo pusiau, auksinio pjūvio ir Niutono metodo algoritmus.

2. Aprašykite tikslo funkciją f(x) = (x^2 − 5)^2 / 4

3. Minimizuokite šią funkciją intervalo dalijimo pusiau ir auksinio pjūvio metodais intervale [0,10] iki tikslumo 10^−4 bei Niutono metodu nuo x0 = 5 kol žingsnio ilgis didesnis už 10^−4.

4. Palyginkite rezultatus: gauti sprendiniai, rastas funkcijos minimumo įvertis, atliktų žingsnių ir funkcijų skaičiavimų skaičius.

5. Vizualizuokite tikslo funkciją ir bandymo taškus.

"""

from math import sqrt
# from typing import Any

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

class ObjectiveFunction:
    def __init__(self) -> None:
        self.calls = 0

    def __call__(self, x: float) -> float:
        self.calls += 1
        return (x**2 - 5)**2 / 4
    
    def reset(self):
        self.calls = 0

def print_variables(**kwargs):
    for name, value in kwargs.items():
        print(f"{name}: {value}")
    print("-------------------------------------------------")
    print()

def bisection_method(objective_function: ObjectiveFunction, interval: tuple[int, int] = (0, 10), tolerance_lipschitz_constant: float = 10**-4):
    objective_function.reset()
    left_bound: float = interval[0]
    right_bound: float = interval[1]
    interval_length: float = right_bound - left_bound

    print("Before initiating the method")
    print("Interval:", [left_bound, right_bound])
    print("Interval length:", interval_length)
    print("-------------------------------------------------")
    print()

    iteration: int = 0
    objective_function_calls: int = 0
    # Do I even need f_min ? 
    # f_min: float | None = None 

    x_middle: float = (left_bound + right_bound) / 2 # 1.
    x1: float | None = None
    x2: float | None = None
    f_x_middle: float = objective_function(x_middle) # 1.
    f_x1: float | None = None
    f_x2: float | None = None
    
    while interval_length > tolerance_lipschitz_constant:
        interval_length = right_bound - left_bound
        
        print("Current iteration:", iteration)
        print("Interval:", [left_bound, right_bound])
        print("Interval length:", interval_length)
        print()
            
        x1 = left_bound + interval_length / 4 # 2.
        f_x1 = objective_function(x1) # 2.
        
        if f_x1 < f_x_middle: # 3. x_middle becomes x_1
            # f_min = f_x1
            right_bound = x_middle # 3.1
            x_middle = x1 # 3.2
            f_x_middle = f_x1 # 3.2
            print_variables(
                # f_min=f_min,
                objective_function_calls=objective_function_calls,
                x1=x1,
                x_middle=x_middle,
                x2=x2,
                f_x1=f_x1,
                f_x_middle=f_x_middle,
                f_x2=f_x2
            )
            interval_length = right_bound - left_bound
            iteration += 1
            continue # 6. is while loop condition

        else: # 2.
            x2 = right_bound - interval_length / 4 # 2.
            f_x2 = objective_function(x2) # 2.
        if f_x2 < f_x_middle: # 4. x_middle becomes x_2
            # f_min = f_x2
            left_bound = x_middle # 4.1 
            x_middle = x2 # 4.2 
            f_x_middle = x2 # 4.2
        else: # 5. x_middle stays x_middle
            x_middle = x_middle
            left_bound = x1 # 5.1 
            right_bound = x2 # 5.1

        # print("objective_function_calls", objective_function_calls)
        # print("x1:", x1)
        # print("x2:", x2)
        # print("x_middle:", x_middle)
        # print("f_x1:", f_x1)
        # print("f_x2:", f_x2)
        # print("f_x_middle:", f_x_middle)
        # print("-------------------------------------------------")
        # print()

        print_variables(
            # f_min=f_min,
            objective_function_calls=objective_function.calls,
            x1=x1,
            x_middle=x_middle,
            x2=x2,
            f_x1=f_x1,
            f_x_middle=f_x_middle,
            f_x2=f_x2
        )
        interval_length = right_bound - left_bound
        iteration += 1

    # TODO: Plot before and after, or with each operation, the graph of the function, each of the points, interval...
    # TODO: Print objective function?

def golden_section_method(objective_function: ObjectiveFunction, interval: tuple[int, int] = (0, 10), tolerance_lipschitz_constant: float = 10**-4):
    objective_function.reset()
    left_bound: float = interval[0]
    right_bound: float = interval[1]
    interval_length: float = right_bound - left_bound # 1.
    
    print("Before initiating the method")
    print("Interval:", [left_bound, right_bound])
    print("Interval length:", interval_length)
    print("-------------------------------------------------")
    print()

    iteration: int = 0
    # Do I even need f_min ? 
    # f_min: float | None = None 
    tau: float = (-1 + sqrt(5)) / 2
    x1: float = (right_bound - tau * interval_length) / 2 # 1.
    x2: float = (left_bound + tau * interval_length) / 2 # 1.
    f_x1: float = objective_function(x1) # 1.
    f_x2: float = objective_function(x2) # 1.
    
    while interval_length > tolerance_lipschitz_constant:
        print("Current iteration:", iteration)
        print("Interval:", [left_bound, right_bound])
        print("Interval length:", interval_length)
        print()
        
        if f_x2 < f_x1: # 2.
            # f_min = f_x1
            left_bound = x1 # 2.1 remove interval [left_bound; x1)
            x1 = x2 # 2.2
            x2 = left_bound + tau * interval_length # 2.3
            f_x2 = objective_function(x2) # 2.3

        else: # 3.
            # f_min = f_x1
            right_bound = x2 # 3.1 remove interval (x2; right_bound]
            x2 = x1 # 3.2
            x2 = left_bound + tau * interval_length # 3.3
            f_x2 = objective_function(x2) # 3.3

        interval_length = right_bound - left_bound # 2.1 / 3.1

        print("objective_function_calls:", objective_function.calls)
        print_variables(
            # f_min=f_min,
            interval_length=interval_length,
            x1=x1,
            x2=x2,
            f_x1=f_x1,
            f_x2=f_x2
        )
        
        iteration += 1

    # TODO: Plot before and after, or with each operation, the graph of the function, each of the points, interval...
    # TODO: Print objective function?

# TODO: Newton optimization method function definition
# Minimizuokite Niutono metodu nuo x0 = 5 kol žingsnio ilgis didesnis už 10^−4.
def newton_method(objective_function: ObjectiveFunction, interval: tuple[int, int] = (0, 10), tolerance_lipschitz_constant: float = 10**-4, x_i: float = 5):
    objective_function.reset()
    left_bound: float = interval[0]
    right_bound: float = interval[1]
    interval_length: float = right_bound - left_bound # 1.
    
    print("Before initiating the method")
    print("Interval:", [left_bound, right_bound])
    print("Interval length:", interval_length)
    print("-------------------------------------------------")
    print()

    iteration: int = 0

    x_iplus1: float | None = None
    
    while interval_length > tolerance_lipschitz_constant:
        print("Current iteration:", iteration)
        print("Interval:", [left_bound, right_bound])
        print("Interval length:", interval_length)
        print()
        
        interval_length = right_bound - left_bound # 2.1 / 3.1
        print_variables(
        )
        
        iteration += 1

    # TODO: Plot before and after, or with each operation, the graph of the function, each of the points, interval...
    # TODO: Print objective function?

f1 = ObjectiveFunction()
# bisection_method(f1)

# f2 = ObjectiveFunction()
# f2.__call__ = lambda x: (x - 3)**2 + 2  # different function
# bisection_method(f2)

# golden_section_method(f1)