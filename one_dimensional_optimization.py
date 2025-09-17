"""
1. Suprogramuokite vienmačio optimizavimo intervalo dalijimo pusiau, auksinio pjūvio ir Niutono metodo algoritmus.

2. Aprašykite tikslo funkciją f(x) = (x^2 − 5)^2 / 4

3. Minimizuokite šią funkciją intervalo dalijimo pusiau ir auksinio pjūvio metodais intervale [0,10] iki tikslumo 10^−4 bei Niutono metodu nuo x0 = 5 kol žingsnio ilgis didesnis už 10^−4.

4. Palyginkite rezultatus: gauti sprendiniai, rastas funkcijos minimumo įvertis, atliktų žingsnių ir funkcijų skaičiavimų skaičius.

5. Vizualizuokite tikslo funkciją ir bandymo taškus.

"""

from matplotlib import *
from dataclasses import dataclass

@dataclass
class bisection_variables:
    def __init__(self, interval):
        self.left_bound = interval[0]
        self.right_bound = interval[1]
        self.interval_length = self.right_bound - self.left_bound
        self.x1 = self.left_bound + self.interval_length / 4
        self.x_middle = (self.left_bound + self.right_bound) / 2
        self.f_x1 = 0
        self.f_x_middle = 0
        self.f_x2 = 0

    def (self, )
        
   
    

def objective_function(x):
    return (x**2 - 5)**2 / 4

# print (objective_function(1))

def bisection_method():
    lipschitz_constant = 10**-4 # based on assignment instructions
    interval = [0, 10] # based on assignment instructions

    variables = bisection_variables(interval)

    print("Interval:", [left_bound, right_bound])
    print("Interval length:", interval_length)
    print("x1:", x1)
    print("x2:", x2)
    print("x_middle:", x_middle)
    print("f_x1:", f_x1)
    print("f_x2:", f_x2)
    print("f_x_middle:", f_x_middle)
    print("-------------------------------------------------")
    print()

    # TODO: Optimize the while loop, so that objective function calls are only done when needed
    # and the points x1/x_middle/x2 are only calculated when needed (re-assigned otherwise)

    iteration = 0
    objective_function_calls = 0
    while (interval_length > lipschitz_constant):
        print("Current iteration:", iteration)
        print("Interval:", [left_bound, right_bound])
        print("Interval length:", interval_length)
        
        

        if (variables.f_x1 < variables.f_x_middle):
            right_bound = x_middle
        else: 
            x2 = right_bound - interval_length / 4
            f_x2 = objective_function(x2)

        if (f_x2 < f_x_middle):
            left_bound = x_middle

        else:
            left_bound = x1
            right_bound = x2

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