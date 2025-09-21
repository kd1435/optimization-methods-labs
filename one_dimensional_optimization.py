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

# TODO: Use Dataclass later
# @dataclass
# class BisectionResult:
#     x1 : float
#     x_middle : float 
#     x2 : float
#     interval_length : list[int]

def objective_function(x, objective_function_calls = 0):
    objective_function_calls += 1
    return (x**2 - 5)**2 / 4

# TODO: Define a variable argument function for printing variables
# def print_variables(xargs):
#     print("xargs[1]:", xargs[1])
#     print("-------------------------------------------------")
#     print()

def bisection_method(interval = [0, 10], tolerance_lipschitz_constant = 10**-4):
    left_bound = interval[0]
    right_bound = interval[1]
    interval_length = right_bound - left_bound

    print("Before initiating the method")
    print("Interval:", [left_bound, right_bound])
    print("Interval length:", interval_length)
    print("-------------------------------------------------")

    iteration = 0
    objective_function_calls = 0
    
    while (interval_length > tolerance_lipschitz_constant):
        go_to_section_6 = False
        interval_length = right_bound - left_bound
        
        print("Current iteration:", iteration)
        print("Interval:", [left_bound, right_bound])
        print("Interval length:", interval_length)

        if iteration == 0:
            x1 = left_bound + interval_length / 4 # 1.
            f_x1 = objective_function(x1, objective_function_calls) # 1.
            x_middle = (left_bound + right_bound) / 2 # 2.
            f_x_middle = objective_function(x_middle, objective_function_calls) # 2.

        if (f_x1 < f_x_middle): # 3.
            right_bound = x_middle # 3.1
            x_middle = x1 # 3.2
            f_x_middle = f_x1 # 3.2
            go_to_section_6 = True # 3.3
        elif iteration == 0:
            x2 = right_bound - interval_length / 4
            f_x2 = objective_function(x2)

        if go_to_section_6: # 3.3
            # print_variables(x1)
            interval_length = right_bound - left_bound
            iteration += 1
            continue # 6. inside while loop condition
        elif (f_x2 < f_x_middle): # 4. 
            left_bound = x_middle # 4.1 
            x_middle = x2 # 4.2 
            f_x_middle = x2 # 4.2
        else: # 5.
            left_bound = x1 # 5.1 
            right_bound = x2 # 5.1

        # print_variables(objective_function_calls)
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

bisection_method()